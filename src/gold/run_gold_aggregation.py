import os
import pandas as pd

print("Starting Gold Layer Aggregations...")

# Define paths
silver_dir = "data/silver/sales_domain"
gold_dir = "data/gold/sales_domain"
os.makedirs(gold_dir, exist_ok=True)

# Load Silver datasets
df_pipeline = pd.read_parquet(os.path.join(silver_dir, "sales_pipeline_cleaned.parquet"))
df_accounts = pd.read_parquet(os.path.join(silver_dir, "accounts_cleaned.parquet"))

# 1. Join Pipeline with Accounts to get Sector info
df_merged = df_pipeline.merge(df_accounts, on="account", how="left")

# 2. Aggregate Total Close Value by Sector and Deal Stage
df_sector_sales = df_merged.groupby(['sector', 'deal_stage'])['close_value'].sum().reset_index()
df_sector_sales.to_parquet(os.path.join(gold_dir, "gold_sales_by_sector.parquet"), index=False)
print("Gold aggregate: Sales by Sector created successfully.")

# 3. Aggregate Top Products by Total Revenue (Won deals)
df_won = df_merged[df_merged['deal_stage'] == 'Won']
df_product_perf = df_won.groupby('product')['close_value'].sum().reset_index().sort_values(by='close_value', ascending=False)
df_product_perf.to_parquet(os.path.join(gold_dir, "gold_product_performance.parquet"), index=False)
print("Gold aggregate: Product Performance created successfully.")

print("Gold Layer aggregations completed successfully!")