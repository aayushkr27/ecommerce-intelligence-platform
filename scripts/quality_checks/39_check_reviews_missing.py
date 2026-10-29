
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
REVIEWS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_order_reviews_dataset.csv"
)

reviews = pd.read_csv(REVIEWS_FILE)

missing_report = pd.DataFrame({
    "missing_count": reviews.isna().sum(),
    "missing_percentage": (
        reviews.isna().mean() * 100
    ).round(2)
})

print("REVIEWS TABLE — MISSING VALUES")
print("=" * 55)
print("Rows:", len(reviews))
print("Columns:", len(reviews.columns))
print(missing_report.to_string())

print(
    "\nTotal missing cells:",
    int(reviews.isna().sum().sum())
)
