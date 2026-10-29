
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

duplicates = reviews.loc[duplicate_mask].sort_values("review_id")

print("DUPLICATE REVIEW ID INVESTIGATION")
print("=" * 60)
print("Rows involved in duplicate IDs:", len(duplicates))
print("Distinct duplicated IDs:", duplicates["review_id"].nunique())

print("\nFirst 15 rows involved in duplicate IDs:")
print(
    duplicates[
        [
            "review_id",
            "order_id",
            "review_score",
            "review_comment_title",
            "review_creation_date",
        ]
    ].head(15).to_string(index=False)
)

print("\nNumber of rows per duplicated review ID:")
print(
    duplicates.groupby("review_id").size()
    .value_counts()
    .sort_index()
    .rename_axis("rows_per_review_id")
    .rename("number_of_review_ids")
    .to_string()
)
