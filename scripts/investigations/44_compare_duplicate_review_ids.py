
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

duplicate_ids = reviews.loc[
    reviews.duplicated(subset=["review_id"], keep=False),
    "review_id"
].unique()

sample_id = duplicate_ids[0]

print("DUPLICATED REVIEW ID COMPARISON")
print("=" * 55)
print("Sample review ID:", sample_id)

sample = reviews[reviews["review_id"] == sample_id]

print("\nAll records for this review ID:")
print(sample.to_string(index=False))

print("\nNumber of distinct values in each column:")
print(sample.nunique(dropna=False).to_string())
