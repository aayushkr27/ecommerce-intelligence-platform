
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

payment_summary = (
    payments["payment_type"]
    .value_counts(dropna=False)
    .rename_axis("payment_type")
    .reset_index(name="payment_rows")
)

payment_summary["percentage"] = (
    payment_summary["payment_rows"] / len(payments) * 100
).round(2)

print("PAYMENT TYPE DISTRIBUTION")
print("=" * 50)
print(payment_summary.to_string(index=False))

print("\nTotal payment rows:", len(payments))
print("Sum of payment-type counts:", payment_summary["payment_rows"].sum())
