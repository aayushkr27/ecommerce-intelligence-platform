
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

reviews_per_order = reviews.groupby("order_id").size()

print("REVIEWS PER ORDER CHECK")
print("=" * 50)
print("Total review rows:", len(reviews))
print("Distinct orders in reviews:", reviews["order_id"].nunique())
print("Orders with one review row:", (reviews_per_order == 1).sum())
print("Orders with multiple review rows:", (reviews_per_order > 1).sum())
print("Maximum review rows for one order:", reviews_per_order.max())

print("\nDistribution of review rows per order:")
print(
    reviews_per_order.value_counts()
    .sort_index()
    .rename_axis("review_rows_per_order")
    .rename("number_of_orders")
    .to_string()
)
