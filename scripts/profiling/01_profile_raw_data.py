
from pathlib import Path
import pandas as pd

# Find the project folder automatically.
PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

# The nine expected Olist CSV files.
csv_files = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "product_category_name_translation.csv",
]

print("=" * 60)
print("OLIST RAW DATA PROFILING")
print("=" * 60)
print(f"Project folder: {PROJECT_DIR}")
print(f"Raw data folder: {RAW_DATA_DIR}")

# Check whether the raw data folder exists.
if not RAW_DATA_DIR.exists():
    raise FileNotFoundError(
        f"Raw data folder not found: {RAW_DATA_DIR}"
    )

# Inspect each CSV without changing the original file.
for filename in csv_files:
    file_path = RAW_DATA_DIR / filename

    print(f"\nFile: {filename}")

    if not file_path.exists():
        print("STATUS: FILE MISSING")
        continue

    df = pd.read_csv(file_path, nrows=5)

    # Read the complete file to count its rows.
    row_count = sum(
        1 for _ in open(file_path, encoding="utf-8")
    ) - 1

    print(f"Rows: {row_count:,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")

print("\nProfiling completed.")
