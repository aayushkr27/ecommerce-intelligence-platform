
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

reviews_per_order = reviews.groupby("order_id").size()
multiple_order_ids = reviews_per_order[reviews_per_order > 1].index

sample_order_id = multiple_order_ids[0]

print("MULTIPLE REVIEWS FOR ONE ORDER")
print("=" * 55)
print("Sample order ID:", sample_order_id)

sample = reviews[reviews["order_id"] == sample_order_id]

print("\nReview records for this order:")
print(
    sample[
        [
            "review_id",
            "order_id",
            "review_score",
            "review_comment_title",
            "review_creation_date",
            "review_answer_timestamp",
        ]
    ].to_string(index=False)
)

print("\nDistinct values per column:")
print(sample.nunique(dropna=False).to_string())
