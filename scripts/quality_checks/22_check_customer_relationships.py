
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

orders = pd.read_csv(
    RAW_DATA_DIR / "olist_orders_dataset.csv",
    usecols=["customer_id"]
)

customers = pd.read_csv(
    RAW_DATA_DIR / "olist_customers_dataset.csv",
    usecols=["customer_id"]
)

valid_customer_ids = set(customers["customer_id"].dropna())

unmatched_orders = orders[
    orders["customer_id"].isna()
    | ~orders["customer_id"].isin(valid_customer_ids)
]

print("CUSTOMER RELATIONSHIP CHECK")
print("=" * 50)
print("Total orders:", len(orders))
print("Unique customer IDs in customer table:", len(valid_customer_ids))
print("Orders with missing or unmatched customer IDs:", len(unmatched_orders))

if unmatched_orders.empty:
    print("\nPASS: All order customer IDs match the customers table.")
else:
    print("\nWARNING: Some customer references need investigation.")
