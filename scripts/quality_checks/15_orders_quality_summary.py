
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Check order ID completeness and uniqueness.
missing_order_ids = orders["order_id"].isna().sum()
blank_order_ids = (
    orders["order_id"]
    .astype("string")
    .str.strip()
    .eq("")
    .sum()
)
duplicate_order_ids = orders["order_id"].duplicated().sum()

# Check purchase timestamp validity.
purchase_dates = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)
invalid_purchase_dates = purchase_dates.isna().sum()

# Summarise missing values in the table.
missing_cells = orders.isna().sum().sum()

checks = [
    ("Total rows", len(orders)),
    ("Missing order IDs", missing_order_ids),
    ("Blank order IDs", blank_order_ids),
    ("Duplicate order IDs", duplicate_order_ids),
    ("Invalid purchase timestamps", invalid_purchase_dates),
    ("Total missing cells", missing_cells),
]

print("ORDERS TABLE — DATA QUALITY SUMMARY")
print("=" * 55)

for check_name, result in checks:
    print(f"{check_name}: {result}")

print("\nSummary completed.")
