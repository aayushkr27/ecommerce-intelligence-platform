
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
REPORT_DIR = PROJECT_DIR / "data" / "processed"

ORDERS_FILE = RAW_DATA_DIR / "olist_orders_dataset.csv"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

orders = pd.read_csv(ORDERS_FILE)

purchase_dates = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

checks = {
    "total_rows": len(orders),
    "missing_order_ids": int(orders["order_id"].isna().sum()),
    "blank_order_ids": int(
        orders["order_id"].astype("string").str.strip().eq("").sum()
    ),
    "duplicate_order_ids": int(orders["order_id"].duplicated().sum()),
    "invalid_purchase_timestamps": int(purchase_dates.isna().sum()),
    "total_missing_cells": int(orders.isna().sum().sum()),
}

report = pd.DataFrame(
    list(checks.items()),
    columns=["check_name", "result"]
)

output_file = REPORT_DIR / "orders_quality_report.csv"
report.to_csv(output_file, index=False)

print("Report saved successfully.")
print("Output path:", output_file)
print("\nReport preview:")
print(report.to_string(index=False))
