
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

scores = pd.to_numeric(
    reviews["review_score"],
    errors="coerce"
)

invalid_mask = (
    scores.isna()
    | ~scores.between(1, 5)
    | (scores % 1 != 0)
)

print("REVIEW SCORE VALIDATION")
print("=" * 50)
print("Total review rows:", len(reviews))
print("Missing scores:", reviews["review_score"].isna().sum())
print("Invalid numeric values:", (
    scores.isna() & reviews["review_score"].notna()
).sum())
print("Scores outside 1–5 or non-integer:", invalid_mask.sum())

print("\nScore distribution:")
print(
    scores.value_counts(dropna=False)
    .sort_index()
    .rename_axis("review_score")
    .rename("review_count")
    .to_string()
)

if not invalid_mask.any():
    print("\nPASS: All review scores are integers between 1 and 5.")
else:
    print("\nWARNING: Investigate invalid review scores.")
