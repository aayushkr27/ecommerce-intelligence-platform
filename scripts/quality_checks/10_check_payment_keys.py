
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PAYMENTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_payments_dataset.csv"
)

payments = pd.read_csv(PAYMENTS_FILE)

print("PAYMENT TABLE KEY CHECK")
print("=" * 50)

print("Total payment rows:", len(payments))
print("Missing order IDs:", payments["order_id"].isna().sum())
print(
    "Missing payment sequence numbers:",
    payments["payment_sequential"].isna().sum()
)

key_columns = ["order_id", "payment_sequential"]

duplicate_mask = payments.duplicated(
    subset=key_columns,
    keep=False
)

print(
    "Unique order-payment combinations:",
    payments[key_columns].drop_duplicates().shape[0]
)
print("Rows involved in duplicate keys:", duplicate_mask.sum())

if duplicate_mask.any():
    print("\nExample duplicate keys:")
    print(
        payments.loc[duplicate_mask, key_columns]
        .sort_values(key_columns)
        .head(10)
        .to_string(index=False)
    )
else:
    print("\nPASS: No duplicate order-payment keys found.")
