
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

zip_codes = customers["customer_zip_code_prefix"].astype("string").str.strip()

print("CUSTOMER ZIP-CODE PREFIX CHECK")
print("=" * 55)
print("Total customer records:", len(customers))
print("Missing ZIP prefixes:", zip_codes.isna().sum())
print("Prefixes not exactly 5 digits:", (~zip_codes.str.fullmatch(r"\d{5}")).sum())
print("Minimum numeric prefix:", customers["customer_zip_code_prefix"].min())
print("Maximum numeric prefix:", customers["customer_zip_code_prefix"].max())

print("\nFirst 10 distinct prefixes:")
print(zip_codes.dropna().drop_duplicates().head(10).to_list())
