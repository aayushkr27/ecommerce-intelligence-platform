
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Count all rows that have an order_id already seen before.
duplicate_mask = orders.duplicated(
    subset=["order_id"],
    keep=False
)

duplicates = orders[duplicate_mask]

print("ORDER ID DUPLICATE CHECK")
print("=" * 50)
print("Total order rows:", len(orders))
print("Unique order IDs:", orders["order_id"].nunique())
print("Rows involved in duplicate IDs:", len(duplicates))
print(
    "Number of duplicated order IDs:",
    orders.loc[duplicate_mask, "order_id"].nunique()
)

if duplicates.empty:
    print("\nPASS: No duplicate order IDs found.")
else:
    print("\nDuplicate order records:")
    print(duplicates.sort_values("order_id").to_string(index=False))
