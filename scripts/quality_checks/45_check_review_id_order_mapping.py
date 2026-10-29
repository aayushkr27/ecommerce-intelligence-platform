
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

orders_per_review = (
    reviews.groupby("review_id")["order_id"]
    .nunique()
)

review_ids_with_multiple_orders = orders_per_review[
    orders_per_review > 1
]

print("REVIEW ID TO ORDER MAPPING CHECK")
print("=" * 55)
print("Total review rows:", len(reviews))
print("Distinct review IDs:", reviews["review_id"].nunique())
print("Review IDs linked to multiple orders:", len(review_ids_with_multiple_orders))
print(
    "Maximum distinct orders linked to one review ID:",
    orders_per_review.max()
)

print("\nDistribution of orders per review ID:")
print(
    orders_per_review.value_counts()
    .sort_index()
    .rename_axis("distinct_orders_per_review_id")
    .rename("number_of_review_ids")
    .to_string()
)

print("\nNo records have been modified or deleted.")
