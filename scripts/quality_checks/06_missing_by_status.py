
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Create a flag: True when the customer delivery date is missing.
orders["delivery_date_missing"] = (
    orders["order_delivered_customer_date"].isna()
)

# Count orders and missing delivery dates for each status.
report = (
    orders.groupby("order_status")
    .agg(
        total_orders=("order_id", "count"),
        missing_delivery_dates=("delivery_date_missing", "sum")
    )
    .reset_index()
)

# Calculate the percentage missing within each status.
report["missing_percentage"] = (
    report["missing_delivery_dates"]
    / report["total_orders"]
    * 100
).round(2)

print("MISSING CUSTOMER DELIVERY DATES BY ORDER STATUS")
print("=" * 65)
print(report.to_string(index=False))
