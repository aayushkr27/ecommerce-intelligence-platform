
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

scores_per_order = (
    reviews.groupby("order_id")["review_score"]
    .nunique()
)

multiple_review_orders = (
    reviews.groupby("order_id").size()
    .loc[lambda counts: counts > 1]
    .index
)

multiple_orders_scores = scores_per_order.loc[multiple_review_orders]

print("SCORE CONSISTENCY FOR MULTIPLE-REVIEW ORDERS")
print("=" * 55)
print("Orders with multiple review rows:", len(multiple_review_orders))
print(
    "Multiple-review orders with one distinct score:",
    (multiple_orders_scores == 1).sum()
)
print(
    "Multiple-review orders with different scores:",
    (multiple_orders_scores > 1).sum()
)
print(
    "Maximum distinct scores for one order:",
    multiple_orders_scores.max()
)
