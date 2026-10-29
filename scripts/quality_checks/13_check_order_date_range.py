
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Convert the purchase timestamp from text to datetime.
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

print("ORDER PURCHASE DATE RANGE")
print("=" * 50)
print("Earliest purchase:", orders["order_purchase_timestamp"].min())
print("Latest purchase:", orders["order_purchase_timestamp"].max())
print(
    "Missing or invalid purchase timestamps:",
    orders["order_purchase_timestamp"].isna().sum()
)
