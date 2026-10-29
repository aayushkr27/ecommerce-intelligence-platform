
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

# Count customer records associated with each unique customer.
records_per_customer = (
    customers.groupby("customer_unique_id")
    .size()
    .rename("record_count")
)

print("CUSTOMER RECORD COUNT DISTRIBUTION")
print("=" * 50)

print("\nNumber of unique customers by record count:")
print(
    records_per_customer.value_counts()
    .sort_index()
    .rename_axis("record_count")
    .rename("unique_customers")
    .to_string()
)

print("\nTotal unique customers:", len(records_per_customer))
print(
    "Customers with multiple records:",
    (records_per_customer > 1).sum()
)
print(
    "Maximum records for one unique customer:",
    records_per_customer.max()
)
