
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

reviews = pd.read_csv(
    RAW_DATA_DIR / "olist_order_reviews_dataset.csv",
    usecols=["review_id", "order_id"]
)

orders = pd.read_csv(
    RAW_DATA_DIR / "olist_orders_dataset.csv",
    usecols=["order_id"]
)

valid_order_ids = set(orders["order_id"].dropna())

unmatched_reviews = reviews[
    reviews["order_id"].isna()
    | ~reviews["order_id"].isin(valid_order_ids)
]

print("REVIEW-ORDER RELATIONSHIP CHECK")
print("=" * 55)
print("Total review rows:", len(reviews))
print("Distinct orders in orders table:", orders["order_id"].nunique())
print("Reviews with missing or unmatched order IDs:", len(unmatched_reviews))

if unmatched_reviews.empty:
    print("\nPASS: All review order IDs match the orders table.")
else:
    print("\nWARNING: Some reviews reference missing orders.")
