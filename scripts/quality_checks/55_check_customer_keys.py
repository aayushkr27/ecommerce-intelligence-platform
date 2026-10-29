
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

duplicate_mask = customers.duplicated(
    subset=["customer_id"],
    keep=False
)

print("CUSTOMER TABLE KEY CHECK")
print("=" * 50)
print("Total customer rows:", len(customers))
print("Missing customer IDs:", customers["customer_id"].isna().sum())
print("Unique customer IDs:", customers["customer_id"].nunique())
print("Rows involved in duplicate customer IDs:", duplicate_mask.sum())

if customers["customer_id"].notna().all() and not duplicate_mask.any():
    print("\nPASS: Customer IDs are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate customer IDs.")
