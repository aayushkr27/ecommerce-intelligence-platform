
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

orders = pd.read_csv(
    RAW_DATA_DIR / "olist_orders_dataset.csv",
    usecols=["order_id", "order_status"]
)

items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv",
    usecols=["order_id"]
)

orders_with_items = set(items["order_id"].dropna())

orders_without_items = orders[
    ~orders["order_id"].isin(orders_with_items)
]

print("ORDERS WITHOUT ITEM RECORDS")
print("=" * 50)
print("Total orders:", len(orders))
print("Orders represented in items:", len(orders_with_items))
print("Orders without item records:", len(orders_without_items))

print("\nOrder status distribution for orders without items:")
print(
    orders_without_items["order_status"]
    .value_counts()
    .to_string()
)
