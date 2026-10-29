
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Count orders in each status.
status_counts = (
    orders["order_status"]
    .value_counts()
    .rename_axis("order_status")
    .reset_index(name="order_count")
)

# Calculate each status's share of all orders.
status_counts["percentage"] = (
    status_counts["order_count"]
    / len(orders)
    * 100
).round(2)

print("ORDER STATUS DISTRIBUTION")
print("=" * 50)
print(status_counts.to_string(index=False))

print("\nTotal orders:", len(orders))
print("Sum of status counts:", status_counts["order_count"].sum())
