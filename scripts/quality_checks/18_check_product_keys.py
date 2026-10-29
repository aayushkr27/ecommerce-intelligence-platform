
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
PRODUCTS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_products_dataset.csv"
)

products = pd.read_csv(PRODUCTS_FILE)

print("PRODUCT TABLE KEY CHECK")
print("=" * 50)
print("Total product rows:", len(products))
print("Missing product IDs:", products["product_id"].isna().sum())
print("Unique product IDs:", products["product_id"].nunique())

duplicate_mask = products.duplicated(
    subset=["product_id"],
    keep=False
)

print("Rows involved in duplicate product IDs:", duplicate_mask.sum())

if not duplicate_mask.any() and products["product_id"].notna().all():
    print("\nPASS: Product IDs are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate product IDs.")
