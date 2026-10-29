
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

print("ORDER ITEMS KEY CHECK")
print("=" * 50)

# Check missing identifiers.
print("Missing order IDs:", items["order_id"].isna().sum())
print("Missing item numbers:", items["order_item_id"].isna().sum())

# Check whether the expected composite key is unique.
key_columns = ["order_id", "order_item_id"]

duplicate_mask = items.duplicated(
    subset=key_columns,
    keep=False
)

print("Total item rows:", len(items))
print("Unique order-item combinations:",
      items[key_columns].drop_duplicates().shape[0])
print("Rows involved in duplicate keys:", duplicate_mask.sum())

if duplicate_mask.any():
    print("\nExample duplicate keys:")
    print(items.loc[duplicate_mask, key_columns]
          .sort_values(key_columns)
          .head(10)
          .to_string(index=False))
else:
    print("\nPASS: No duplicate order-item keys found.")
