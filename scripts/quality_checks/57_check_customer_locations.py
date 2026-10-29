
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

location_columns = [
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state",
]

print("CUSTOMER LOCATION CHECK")
print("=" * 55)
print("Total customer records:", len(customers))

for column in location_columns:
    values = customers[column].astype("string").str.strip()
    blank_mask = values.isna() | values.eq("")

    print(f"\nColumn: {column}")
    print("Missing or blank values:", int(blank_mask.sum()))
    print("Distinct non-blank values:", values[~blank_mask].nunique())

print("\nDistinct customer states:")
print(
    customers["customer_state"]
    .value_counts()
    .sort_index()
    .to_string()
)
