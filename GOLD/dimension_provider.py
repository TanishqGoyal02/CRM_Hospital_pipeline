# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_provider
# MAGIC (
# MAGIC ProviderID string,
# MAGIC FirstName string,
# MAGIC LastName string,
# MAGIC DeptID string,
# MAGIC NPI long,
# MAGIC datasource string
# MAGIC );
# MAGIC
# MAGIC
# MAGIC
# MAGIC insert into gold.dim_provider
# MAGIC select 
# MAGIC ProviderID ,
# MAGIC FirstName ,
# MAGIC LastName ,
# MAGIC concat(DeptID,'-',datasource) deptid,
# MAGIC NPI ,
# MAGIC datasource 
# MAGIC from silver.providers
# MAGIC where is_quarantined=false;
# MAGIC
# MAGIC
