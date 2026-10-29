
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

records_per_person = customers.groupby("customer_unique_id").size()

print("CUSTOMER UNIQUE ID CHECK")
print("=" * 50)
print("Total customer records:", len(customers))
print("Missing customer_unique_id values:",
      customers["customer_unique_id"].isna().sum())
print("Distinct customer_unique_id values:",
      customers["customer_unique_id"].nunique())
print("Customer records beyond unique people:",
      len(customers) - customers["customer_unique_id"].nunique())
print("Unique customers with multiple records:",
      (records_per_person > 1).sum())
print("Maximum records for one unique customer:",
      records_per_person.max())

print("\nDistribution of records per unique customer:")
print(
    records_per_person.value_counts()
    .sort_index()
    .rename_axis("records_per_customer")
    .rename("number_of_unique_customers")
    .to_string()
)
