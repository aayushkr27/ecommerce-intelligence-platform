
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

duplicate_mask = payments.duplicated(
    subset=["order_id", "payment_sequential"],
    keep=False
)

print("PAYMENT COMPOSITE-KEY CHECK")
print("=" * 50)
print("Total payment rows:", len(payments))
print("Missing order IDs:", payments["order_id"].isna().sum())
print("Missing sequence values:", payments["payment_sequential"].isna().sum())
print("Rows involved in duplicate composite keys:", duplicate_mask.sum())

if (
    payments["order_id"].notna().all()
    and payments["payment_sequential"].notna().all()
    and not duplicate_mask.any()
):
    print("\nPASS: Payment composite keys are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate composite keys.")
