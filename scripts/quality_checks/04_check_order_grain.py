
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

items = pd.read_csv(
    RAW_DATA_DIR / "olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    RAW_DATA_DIR / "olist_order_payments_dataset.csv"
)

# Count item rows per order.
item_counts = (
    items.groupby("order_id")
    .size()
    .reset_index(name="item_rows")
)

# Count payment rows per order.
payment_counts = (
    payments.groupby("order_id")
    .size()
    .reset_index(name="payment_rows")
)

# Find orders with multiple rows in both tables.
comparison = item_counts.merge(
    payment_counts,
    on="order_id",
    how="inner"
)

multiple_both = comparison[
    (comparison["item_rows"] > 1)
    & (comparison["payment_rows"] > 1)
]

print("Orders with multiple item rows:", 
      (item_counts["item_rows"] > 1).sum())

print("Orders with multiple payment rows:", 
      (payment_counts["payment_rows"] > 1).sum())

print("Orders with multiple rows in BOTH tables:",
      len(multiple_both))

print("\nExample orders:")
print(multiple_both.head(10).to_string(index=False))
