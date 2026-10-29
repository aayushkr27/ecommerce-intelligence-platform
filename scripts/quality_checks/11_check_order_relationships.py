
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

orders = pd.read_csv(
    RAW_DATA_DIR / "olist_orders_dataset.csv",
    usecols=["order_id"]
)

items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv",
    usecols=["order_id"]
)

payments = pd.read_csv(
    RAW_DATA_DIR / "olist_order_payments_dataset.csv",
    usecols=["order_id"]
)

# Collect all valid order IDs.
valid_order_ids = set(orders["order_id"])

# Find records that reference a nonexistent order.
orphan_items = items[
    ~items["order_id"].isin(valid_order_ids)
]

orphan_payments = payments[
    ~payments["order_id"].isin(valid_order_ids)
]

print("ORDER RELATIONSHIP CHECK")
print("=" * 50)
print("Orders in main table:", len(orders))
print("Item rows without a matching order:", len(orphan_items))
print("Payment rows without a matching order:", len(orphan_payments))

if orphan_items.empty and orphan_payments.empty:
    print("\nPASS: All item and payment order IDs exist in the orders table.")
else:
    print("\nWARNING: Some records reference missing orders.")
