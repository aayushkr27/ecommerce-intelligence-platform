
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
SELLERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_sellers_dataset.csv"
)

sellers = pd.read_csv(SELLERS_FILE)

location_columns = [
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state",
]

print("SELLER LOCATION CHECK")
print("=" * 55)
print("Total seller records:", len(sellers))

for column in location_columns:
    values = sellers[column].astype("string").str.strip()
    blank_mask = values.isna() | values.eq("")

    print(f"\nColumn: {column}")
    print("Missing or blank values:", int(blank_mask.sum()))
    print("Distinct non-blank values:", values[~blank_mask].nunique())

print("\nSeller count by state:")
print(
    sellers["seller_state"]
    .value_counts()
    .sort_index()
    .to_string()
)
