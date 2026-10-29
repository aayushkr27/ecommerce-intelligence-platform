
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

date_columns = [
    "review_creation_date",
    "review_answer_timestamp",
]

print("REVIEW DATE VALIDATION")
print("=" * 55)
print("Total review rows:", len(reviews))

for column in date_columns:
    parsed_dates = pd.to_datetime(reviews[column], errors="coerce")

    invalid_dates = (
        parsed_dates.isna() & reviews[column].notna()
    ).sum()

    print(f"\nColumn: {column}")
    print("Missing values:", reviews[column].isna().sum())
    print("Invalid date values:", invalid_dates)

    if parsed_dates.notna().any():
        print("Earliest date:", parsed_dates.min())
        print("Latest date:", parsed_dates.max())

print("\nNo source records have been modified.")
