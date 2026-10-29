
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

zip_codes = (
    customers["customer_zip_code_prefix"]
    .astype("string")
    .str.strip()
    .str.zfill(5)
)

print("CUSTOMER ZIP-CODE FORMATTING VERIFICATION")
print("=" * 55)
print("Total customer records:", len(customers))
print("Prefixes not exactly 5 digits:", (~zip_codes.str.fullmatch(r"\d{5}")).sum())
print("Minimum formatted prefix:", zip_codes.min())
print("Maximum formatted prefix:", zip_codes.max())

print("\nFirst 10 formatted prefixes:")
print(zip_codes.drop_duplicates().head(10).to_list())

print("\nOriginal source data remains unchanged.")
