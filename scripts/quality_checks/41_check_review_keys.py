
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

duplicate_mask = reviews.duplicated(
    subset=["review_id"],
    keep=False
)

print("REVIEW TABLE KEY CHECK")
print("=" * 50)
print("Total review rows:", len(reviews))
print("Missing review IDs:", reviews["review_id"].isna().sum())
print("Unique review IDs:", reviews["review_id"].nunique())
print("Rows involved in duplicate review IDs:", duplicate_mask.sum())

if (
    reviews["review_id"].notna().all()
    and not duplicate_mask.any()
):
    print("\nPASS: Review IDs are present and unique.")
else:
    print("\nWARNING: Investigate missing or duplicate review IDs.")
