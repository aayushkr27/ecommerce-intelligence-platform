
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
SELLERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_sellers_dataset.csv"
)

sellers = pd.read_csv(SELLERS_FILE)

duplicate_mask = sellers.duplicated(
    subset=["seller_id"],
    keep=False
)

print("SELLER TABLE KEY CHECK")
print("=" * 50)
print("Total seller rows:", len(sellers))
print("Missing seller IDs:", sellers["seller_id"].isna().sum())
print("Unique seller IDs:", sellers["seller_id"].nunique())
print("Rows involved in duplicate seller IDs:", duplicate_mask.sum())

if sellers["seller_id"].notna().all() and not duplicate_mask.any():
    print("\nPASS: Seller IDs are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate seller IDs.")
