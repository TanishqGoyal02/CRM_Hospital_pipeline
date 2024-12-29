# Databricks notebook source
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, DateType, BooleanType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ICD Code Extraction") \
    .getOrCreate()

# Authentication details
client_id = 'client_id'
client_secret = 'client_secret'
auth_url = 'https://icdaccessmanagement.who.int/connect/token'

# Current date for timestamping
current_date = datetime.now().date()

# Obtain access token
auth_response = requests.post(auth_url, data={
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
})
if auth_response.status_code == 200:
    access_token = auth_response.json().get('access_token')
else:
    raise Exception(f"Failed to obtain access token: {auth_response.status_code} - {auth_response.text}")

# Set headers for API requests
headers = {
    'Authorization': f'Bearer {access_token}',
    'API-Version': 'v2',
    'Accept-Language': 'en',
}

# Function to fetch ICD codes
def fetch_icd_codes(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

# Recursive function to extract codes
def extract_codes(url):
    data = fetch_icd_codes(url)
    codes = []
    if 'child' in data:
        for child_url in data['child']:
            codes.extend(extract_codes(child_url))
    else:
        if 'code' in data and 'title' in data:
            codes.append({
                'icd_code': data['code'],
                'icd_code_type': 'ICD-10',
                'code_description': data['title']['@value'],
                'inserted_date': current_date,
                'updated_date': current_date,
                'is_current_flag': True
            })
    return codes

# Fetch and process ICD codes
root_url = 'https://id.who.int/icd/release/10/2019/A00-A09'
icd_codes = extract_codes(root_url)

# Define schema for Spark DataFrame
schema = StructType([
    StructField("icd_code", StringType(), True),
    StructField("icd_code_type", StringType(), True),
    StructField("code_description", StringType(), True),
    StructField("inserted_date", DateType(), True),
    StructField("updated_date", DateType(), True),
    StructField("is_current_flag", BooleanType(), True)
])

# Create Spark DataFrame
df = spark.createDataFrame(icd_codes, schema=schema)

# Save to Parquet format
output_path = "/mnt/bronze/icd_codes/"
df.write.format("parquet").mode("overwrite").save(output_path)
print(f"Data saved to {output_path}")
