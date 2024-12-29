# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS audit;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS audit.load_logs (
# MAGIC      data_source STRING,
# MAGIC      tablename STRING,
# MAGIC      numberofrowscopied INT,
# MAGIC      watermarkcolumnname STRING,
# MAGIC      loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC TRUNCATE TABLE audit.load_logs;
