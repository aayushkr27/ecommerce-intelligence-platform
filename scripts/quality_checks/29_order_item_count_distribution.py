
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ITEMS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_items_dataset.csv"
)

items = pd.read_csv(ITEMS_FILE)

# Count item rows within each order.
items_per_order = (
    items.groupby("order_id")
    .size()
    .rename("item_count")
)

print("ORDER ITEM COUNT DISTRIBUTION")
print("=" * 50)

print("\nNumber of orders by item count:")
print(
    items_per_order.value_counts()
    .sort_index()
    .rename_axis("items_per_order")
    .rename("number_of_orders")
    .to_string()
)

print("\nOrders represented in items table:", len(items_per_order))
print("Average item rows per order:", round(items_per_order.mean(), 2))
print("Maximum item rows in one order:", items_per_order.max())
