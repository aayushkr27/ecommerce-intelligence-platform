
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

zero_freight = items[items["freight_value"] == 0]

print("ZERO-FREIGHT INVESTIGATION")
print("=" * 50)
print("Rows with zero freight:", len(zero_freight))
print("Distinct orders affected:", zero_freight["order_id"].nunique())
print("Distinct products affected:", zero_freight["product_id"].nunique())
print("Distinct sellers affected:", zero_freight["seller_id"].nunique())

print("\nFirst 10 zero-freight records:")
print(
    zero_freight[
        ["order_id", "order_item_id", "product_id", "seller_id", "price", "freight_value"]
    ].head(10).to_string(index=False)
)
