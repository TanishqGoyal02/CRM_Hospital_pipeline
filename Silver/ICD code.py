# Databricks notebook source
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("ICD Code Processing").getOrCreate()

# Step 1: Read ICD extracts from the bronze layer
bronze_path = "/mnt/bronze/icd_codes/"
df = spark.read.format("parquet").load(bronze_path)

# Create a temporary view for staging ICD codes
df.createOrReplaceTempView("staging_icd_codes")

# Step 2: Create the silver table if it doesn't exist
spark.sql("""
CREATE TABLE IF NOT EXISTS silver.icd_codes (
    icd_code STRING,
    icd_code_type STRING,
    code_description STRING,
    inserted_date DATE,
    updated_date DATE,
    is_current_flag BOOLEAN
)
USING DELTA
""")



# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO silver.icd_codes AS target
# MAGIC USING staging_icd_codes AS source
# MAGIC ON target.icd_code = source.icd_code
# MAGIC WHEN MATCHED AND target.code_description != source.code_description
# MAGIC   THEN UPDATE SET
# MAGIC     target.code_description = source.code_description,
# MAGIC     target.updated_date = source.updated_date,
# MAGIC     target.is_current_flag = False
# MAGIC WHEN NOT MATCHED THEN
# MAGIC   INSERT (
# MAGIC     icd_code,
# MAGIC     icd_code_type,
# MAGIC     code_description,
# MAGIC     inserted_date,
# MAGIC     updated_date,
# MAGIC     is_current_flag
# MAGIC   )
# MAGIC   VALUES (
# MAGIC     source.icd_code,
# MAGIC     source.icd_code_type,
# MAGIC     source.code_description,
# MAGIC     source.inserted_date,
# MAGIC     source.updated_date,
# MAGIC     source.is_current_flag
# MAGIC   )
