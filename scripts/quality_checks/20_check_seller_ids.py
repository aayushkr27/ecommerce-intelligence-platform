
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv"
)

sellers = pd.read_csv(
    RAW_DATA_DIR / "olist_sellers_dataset.csv"
)

print("SELLER ID CHECK")
print("=" * 50)
print("Total order item rows:", len(items))
print("Missing seller IDs in items:", items["seller_id"].isna().sum())
print("Unique seller IDs in seller table:", sellers["seller_id"].nunique())

# Check whether item seller IDs exist in the seller table.
valid_seller_ids = set(sellers["seller_id"].dropna())

unmatched_items = items[
    items["seller_id"].isna()
    | ~items["seller_id"].isin(valid_seller_ids)
]

print("Item rows with missing or unmatched seller IDs:", len(unmatched_items))

if unmatched_items.empty:
    print("\nPASS: All order item seller IDs match the seller table.")
else:
    print("\nWARNING: Some seller references need investigation.")
