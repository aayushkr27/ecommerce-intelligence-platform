
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Find delivered orders without a customer delivery date.
exceptions = orders[
    (orders["order_status"] == "delivered")
    & (orders["order_delivered_customer_date"].isna())
]

columns_to_show = [
    "order_id",
    "order_status",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

print("DELIVERED ORDERS WITH MISSING CUSTOMER DELIVERY DATE")
print("=" * 70)
print("Number of exceptions:", len(exceptions))

print("\nException records:")
print(exceptions[columns_to_show].to_string(index=False))
