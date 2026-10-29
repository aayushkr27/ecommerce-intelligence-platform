
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv",
    usecols=["product_id"]
)

products = pd.read_csv(
    RAW_DATA_DIR / "olist_products_dataset.csv",
    usecols=["product_id"]
)

# Collect valid product IDs.
valid_product_ids = set(products["product_id"].dropna())

# Find item rows whose product ID isn't in the products table.
orphan_items = items[
    items["product_id"].isna()
    | ~items["product_id"].isin(valid_product_ids)
]

print("PRODUCT RELATIONSHIP CHECK")
print("=" * 50)
print("Total order item rows:", len(items))
print("Unique product IDs in product table:", len(valid_product_ids))
print("Item rows with missing or unmatched product IDs:", len(orphan_items))

if orphan_items.empty:
    print("\nPASS: All order item product IDs match the products table.")
else:
    print("\nWARNING: Some order items have missing or unmatched products.")
