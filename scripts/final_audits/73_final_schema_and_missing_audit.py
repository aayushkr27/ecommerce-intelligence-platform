
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_DIR / "data" / "raw"

files = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "product_category_name_translation.csv",
]

print("FINAL SCHEMA AND MISSING-VALUE AUDIT")
print("=" * 70)

for filename in files:
    path = RAW_DIR / filename

    if not path.exists():
        print(f"\nFILE MISSING: {filename}")
        continue

    df = pd.read_csv(path)

    print(f"\nFILE: {filename}")
    print("-" * 70)
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Total missing cells:", int(df.isna().sum().sum()))
    print("Exact duplicate rows:", int(df.duplicated().sum()))

    summary = pd.DataFrame({
        "column": df.columns,
        "data_type": [str(df[c].dtype) for c in df.columns],
        "missing_count": [int(df[c].isna().sum()) for c in df.columns],
        "missing_percent": [
            round(df[c].isna().mean() * 100, 2)
            for c in df.columns
        ],
    })

    print(summary.to_string(index=False))

print("\nAudit complete. Raw source files were not modified.")
