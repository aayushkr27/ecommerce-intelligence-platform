
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PRODUCTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_products_dataset.csv"
)

products = pd.read_csv(PRODUCTS_FILE)

missing_report = pd.DataFrame({
    "missing_count": products.isna().sum(),
    "missing_percentage": (
        products.isna().mean() * 100
    ).round(2)
})

print("PRODUCTS TABLE — MISSING VALUES")
print("=" * 55)
print("Rows:", len(products))
print("Columns:", len(products.columns))
print(missing_report.to_string())

print(
    "\nTotal missing cells:",
    int(products.isna().sum().sum())
)
