
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

print("ORDER ITEM VALUE CHECK")
print("=" * 50)

for column in ["price", "freight_value"]:
    values = pd.to_numeric(items[column], errors="coerce")

    print(f"\nColumn: {column}")
    print("Missing values:", values.isna().sum())
    print("Invalid numeric values:", (values.isna() & items[column].notna()).sum())
    print("Negative values:", (values < 0).sum())
    print("Zero values:", (values == 0).sum())
    print("Minimum value:", values.min())
    print("Maximum value:", values.max())
