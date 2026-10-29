
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

# Count rows that are identical across every column.
exact_duplicate_mask = reviews.duplicated(keep=False)

# Count extra copies beyond the first occurrence.
exact_duplicate_extras = reviews.duplicated(keep="first").sum()

print("EXACT DUPLICATE REVIEW ROW CHECK")
print("=" * 55)
print("Total review rows:", len(reviews))
print("Rows involved in exact duplicate groups:", exact_duplicate_mask.sum())
print("Extra exact duplicate rows:", exact_duplicate_extras)

print("\nExample exact duplicate rows:")
print(
    reviews.loc[exact_duplicate_mask]
    .sort_values("review_id")
    .head(10)
    .to_string(index=False)
)

print("\nReview ID uniqueness after this check is NOT assumed.")
print("No records have been deleted or modified.")
