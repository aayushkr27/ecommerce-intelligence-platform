
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

sequence = pd.to_numeric(
    payments["payment_sequential"],
    errors="coerce"
)

print("PAYMENT SEQUENCE CHECK")
print("=" * 50)
print("Total payment rows:", len(payments))
print("Missing sequence values:", sequence.isna().sum())
print("Invalid numeric values:", (
    sequence.isna() & payments["payment_sequential"].notna()
).sum())
print("Zero or negative sequences:", (sequence <= 0).sum())

print("\nPayment rows by sequence number:")
print(
    sequence.value_counts()
    .sort_index()
    .rename_axis("payment_sequential")
    .rename("payment_rows")
    .to_string()
)
