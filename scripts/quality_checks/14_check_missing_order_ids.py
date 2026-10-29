
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

missing_ids = orders["order_id"].isna().sum()
blank_ids = (
    orders["order_id"]
    .astype("string")
    .str.strip()
    .eq("")
    .sum()
)

print("ORDER ID COMPLETENESS CHECK")
print("=" * 50)
print("Total rows:", len(orders))
print("Missing order IDs:", missing_ids)
print("Blank order IDs:", blank_ids)

if missing_ids == 0 and blank_ids == 0:
    print("\nPASS: Every row has a non-blank order ID.")
else:
    print("\nWARNING: Some rows have missing or blank order IDs.")
