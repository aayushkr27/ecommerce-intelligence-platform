
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

zero_payments = payments[payments["payment_value"] == 0]

print("ZERO-VALUE PAYMENT INVESTIGATION")
print("=" * 55)
print("Zero-value payment rows:", len(zero_payments))
print("Distinct orders affected:", zero_payments["order_id"].nunique())

print("\nPayment types among zero-value records:")
print(zero_payments["payment_type"].value_counts().to_string())

print("\nZero-value payment records:")
print(
    zero_payments[
        [
            "order_id",
            "payment_sequential",
            "payment_type",
            "payment_installments",
            "payment_value",
        ]
    ].to_string(index=False)
)
