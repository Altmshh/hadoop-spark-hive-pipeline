import os
import pandas as pd

print("Starting Silver Layer Transformation & Cleaning...")

# Define paths
bronze_dir = "data/bronze/sales_domain"
silver_dir = "data/silver/sales_domain"
os.makedirs(silver_dir, exist_ok=True)

# 1. Process Sales Pipeline Table
pipeline_path = os.path.join(bronze_dir, "sales_pipeline.parquet")
if os.path.exists(pipeline_path):
    df_pipeline = pd.read_parquet(pipeline_path)
    
    # Clean data types and missing values
    df_pipeline['engage_date'] = pd.to_datetime(df_pipeline['engage_date'], errors='coerce')
    df_pipeline['close_date'] = pd.to_datetime(df_pipeline['close_date'], errors='coerce')
    df_pipeline['close_value'] = df_pipeline['close_value'].fillna(0)
    df_pipeline['account'] = df_pipeline['account'].fillna('Unknown Account')
    
    # Save to Silver Zone
    df_pipeline.to_parquet(os.path.join(silver_dir, "sales_pipeline_cleaned.parquet"), index=False)
    print("Sales Pipeline cleaned and saved to Silver zone.")

# 2. Process Accounts Table
accounts_path = os.path.join(bronze_dir, "accounts.parquet")
if os.path.exists(accounts_path):
    df_accounts = pd.read_parquet(accounts_path)
    df_accounts['subsidiary_of'] = df_accounts['subsidiary_of'].fillna('Independent')
    
    df_accounts.to_parquet(os.path.join(silver_dir, "accounts_cleaned.parquet"), index=False)
    print("Accounts cleaned and saved to Silver zone.")

print("Silver Layer transformation completed successfully!")