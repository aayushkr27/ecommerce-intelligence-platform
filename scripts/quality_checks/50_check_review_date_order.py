
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

creation = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

answer = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

invalid_chronology = answer < creation

print("REVIEW DATE CHRONOLOGY CHECK")
print("=" * 55)
print("Total review rows:", len(reviews))
print("Answer timestamps before creation dates:", invalid_chronology.sum())

if invalid_chronology.any():
    print("\nExample records with unexpected chronology:")
    print(
        reviews.loc[
            invalid_chronology,
            [
                "review_id",
                "order_id",
                "review_creation_date",
                "review_answer_timestamp",
            ],
        ].head(10).to_string(index=False)
    )
else:
    print("\nPASS: No answer timestamps precede creation dates.")
