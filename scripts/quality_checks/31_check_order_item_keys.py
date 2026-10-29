
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

print("ORDER ITEM TABLE KEY CHECK")
print("=" * 50)
print("Total item rows:", len(items))
print("Missing order IDs:", items["order_id"].isna().sum())
print("Missing order item IDs:", items["order_item_id"].isna().sum())

duplicate_mask = items.duplicated(
    subset=["order_id", "order_item_id"],
    keep=False
)

print("Rows involved in duplicate composite keys:", duplicate_mask.sum())

if (
    items["order_id"].notna().all()
    and items["order_item_id"].notna().all()
    and not duplicate_mask.any()
):
    print("\nPASS: Order-item composite keys are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate composite keys.")
