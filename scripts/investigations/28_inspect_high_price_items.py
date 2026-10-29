
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

top_prices = items.nlargest(10, "price")

print("TOP 10 HIGHEST-PRICED ORDER ITEMS")
print("=" * 65)
print(
    top_prices[
        ["order_id", "order_item_id", "product_id", "seller_id", "price", "freight_value"]
    ].to_string(index=False)
)

print("\nOverall price statistics:")
print(items["price"].describe().round(2).to_string())
