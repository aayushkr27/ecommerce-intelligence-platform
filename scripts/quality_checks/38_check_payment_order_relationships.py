
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

payments = pd.read_csv(
    RAW_DATA_DIR / "olist_order_payments_dataset.csv",
    usecols=["order_id"]
)

orders = pd.read_csv(
    RAW_DATA_DIR / "olist_orders_dataset.csv",
    usecols=["order_id"]
)

valid_order_ids = set(orders["order_id"].dropna())

unmatched_payments = payments[
    payments["order_id"].isna()
    | ~payments["order_id"].isin(valid_order_ids)
]

print("PAYMENT-ORDER RELATIONSHIP CHECK")
print("=" * 50)
print("Total payment rows:", len(payments))
print("Unique orders in orders table:", orders["order_id"].nunique())
print("Payment rows with missing or unmatched order IDs:", len(unmatched_payments))

if unmatched_payments.empty:
    print("\nPASS: All payment order IDs match the orders table.")
else:
    print("\nWARNING: Some payment records reference missing orders.")
