# Hospital CRM Data Pipeline

Welcome to the Hospital CRM Data Pipeline project! I built this project as a robust, end-to-end solution to manage healthcare data efficiently using modern Azure technologies. It follows the Medallion architecture (Bronze–Silver–Gold) and incorporates parallel processing, secure practices, and advanced data modeling techniques. This README outlines how I structured the pipeline, the tools I used, and my inspiration behind the project.

<img width="1033" alt="Screenshot 2024-12-29 at 2 36 25 PM" src="https://github.com/user-attachments/assets/484fd320-1262-434b-a725-4ea046de2021" />
(Refrence: https://www.youtube.com/watch?v=d3Vw3VtKDnc&t=18881s)


## Table of Contents
	1.	Introduction
	2.	How It Works
	3.	Technology Stack
	4.	Medallion Architecture
	5.	Snowflake Schema Design
	6.	Slowly Changing Dimensions (SCD2)
	7.	Security Features
	8.	References

## **Introduction**

This project was created to address the complexities of managing and analyzing healthcare data in a secure, scalable, and efficient way. My goal was to extract healthcare datasets (like CPT and NPI codes), transform them into actionable insights, and store them in a structured, analytics-ready format.

I designed the pipeline to:
	•	Extract data through APIs and ingest it into the Bronze layer in Parquet format.
	•	Transform the raw data into the Silver layer, applying data cleansing and validation.
	•	Aggregate and refine the data into a Gold layer following a Snowflake schema for advanced analytics.

By using Azure Data Factory and Azure Databricks, I ensured seamless orchestration and scalability.

## **How It Works**

### **Data Flow**:
	1.	Data Extraction
I retrieved CPT (Current Procedural Terminology) and NPI (National Provider Identifier) data via REST APIs. The extracted data is ingested into the Bronze layer in Parquet format.
	2.	Data Transformation
Using Azure Databricks, I cleaned and standardized the data, storing it as Delta tables in the Silver layer.
	3.	Data Aggregation
In the Gold layer, I designed Fact and Dimension tables using a Snowflake schema. This final layer is curated for reporting, analytics, and machine learning applications.
	4.	Parallel Processing
To improve performance, I enabled parallel pipeline execution using Azure Data Factory, ensuring timely processing of large datasets.
	5.	Audit and Logging
I implemented a logging mechanism to track both full and incremental data loads, ensuring transparency and traceability.

Technology Stack

For this project, I used:
	•	Azure Data Factory (ADF): To orchestrate data pipelines and schedule jobs.
	•	Azure Databricks: For data processing and transformation using Spark.
	•	Azure Key Vault: To securely store API keys, connection strings, and secrets.
	•	Git CI/CD: To manage version control and automate deployments.
	•	Delta Tables: To manage data lineage and support incremental loads.
	•	Medallion Architecture: For progressive refinement of data (Bronze → Silver → Gold).

Medallion Architecture

Bronze Layer (Raw Data)

<img width="599" alt="Screenshot 2024-12-29 at 2 31 19 PM" src="https://github.com/user-attachments/assets/13ef55cc-0480-42d5-b190-a83f6f2e5c6d" />  


I stored the raw data retrieved from APIs in Parquet format to preserve fidelity and ensure reprocessability.

Silver Layer (Validated Data)

<img width="318" alt="Screenshot 2024-12-29 at 5 23 22 AM" src="https://github.com/user-attachments/assets/c6e6420b-6dac-483f-8547-0f8263f93460" />  


This layer holds partially curated data. Here, I applied validation, cleansing, and deduplication to make the data consistent.

Gold Layer (Curated Data)

In this layer, I structured the data into Fact and Dimension tables using a Snowflake schema, making it ready for business intelligence and analytics.

Snowflake Schema Design

To optimize for analytics and reporting, I implemented a Snowflake schema:
	•	Fact Tables: Store transactional data like patient visits or billing details.
	•	Dimension Tables: Contain reference data such as providers, departments, and procedures.

This schema design ensures fast and efficient queries for advanced analytics.

## Slowly Changing Dimensions (SCD2)

I implemented Type 2 Slowly Changing Dimensions in the Gold layer to track historical changes in dimension data. This approach preserves the full history of changes and uses active/inactive flags to maintain a complete lineage.

## Security Features

I prioritized security throughout the project by:
	•	Integrating Azure Key Vault: All secrets and credentials (e.g., API keys, connection strings) are stored securely.
	•	Implementing Firewall Access Policies: To restrict access to authorized IP addresses and services only.
	•	Audit Logging: Comprehensive audit logs track all data pipeline activities for compliance and monitoring.

<img width="562" alt="Screenshot 2024-12-29 at 2 30 21 PM" src="https://github.com/user-attachments/assets/20522af7-14bd-40e3-af04-5de66e654d1f" />


## References

This project was inspired by the End-to-End Azure Data Engineering Project by Sumit Sir on YouTube. I learned many best practices from this tutorial, which helped shape my approach to designing the pipeline. You can explore the tutorial here:
End-to-End Azure Data Engineering Project by Sumit Sir

Thank you for taking the time to learn about my project! Feel free to reach out if you have any questions or suggestions.
