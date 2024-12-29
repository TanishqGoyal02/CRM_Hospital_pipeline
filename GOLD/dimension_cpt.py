# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS gold;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_cpt_code
# MAGIC (
# MAGIC cpt_codes string,
# MAGIC procedure_code_category string,
# MAGIC procedure_code_descriptions string,
# MAGIC code_status string,
# MAGIC refreshed_at timestamp
# MAGIC );
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC insert into gold.dim_cpt_code
# MAGIC select 
# MAGIC cpt_codes,
# MAGIC procedure_code_category,
# MAGIC procedure_code_descriptions ,
# MAGIC code_status,
# MAGIC current_timestamp() as refreshed_at
# MAGIC  from silver.cptcodes
# MAGIC  where is_quarantined=false and is_current=true;
# MAGIC
# MAGIC
# MAGIC select * from gold.dim_cpt_code;
