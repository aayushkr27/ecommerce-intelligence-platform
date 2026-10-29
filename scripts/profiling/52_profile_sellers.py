
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
SELLERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_sellers_dataset.csv"
)

sellers = pd.read_csv(SELLERS_FILE)

missing_report = pd.DataFrame({
    "missing_count": sellers.isna().sum(),
    "missing_percentage": (
        sellers.isna().mean() * 100
    ).round(2)
})

print("SELLERS TABLE — RAW PROFILE")
print("=" * 55)
print("Rows:", len(sellers))
print("Columns:", len(sellers.columns))
print("\nColumn names:")
print(sellers.columns.tolist())

print("\nData types:")
print(sellers.dtypes.to_string())

print("\nMissing values report:")
print(missing_report.to_string())

print("\nTotal missing cells:", int(sellers.isna().sum().sum()))
