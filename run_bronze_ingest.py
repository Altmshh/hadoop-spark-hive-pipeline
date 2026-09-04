import os
import pandas as pd

bronze_dir = "data/bronze/sales_domain"
os.makedirs(bronze_dir, exist_ok=True)

files = ["accounts.csv", "products.csv", "sales_pipeline.csv", "sales_teams.csv"]

for file in files:
    file_path = os.path.join("data", file)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        table_name = file.replace(".csv", "")
        output_path = os.path.join(bronze_dir, f"{table_name}.parquet")
        df.to_parquet(output_path, index=False)
        print(f"Successfully ingested {file} into Bronze Zone Parquet format.")

print("Bronze ingestion completed successfully!")