
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

values = pd.to_numeric(payments["payment_value"], errors="coerce")

print("PAYMENT VALUE CHECK")
print("=" * 50)
print("Total payment rows:", len(payments))
print("Missing payment values:", payments["payment_value"].isna().sum())
print(
    "Invalid numeric values:",
    (values.isna() & payments["payment_value"].notna()).sum()
)
print("Negative values:", (values < 0).sum())
print("Zero values:", (values == 0).sum())
print("Minimum value:", values.min())
print("Maximum value:", values.max())
