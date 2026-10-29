
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

print("CUSTOMER IDENTIFIER ANALYSIS")
print("=" * 50)

print("Total customer records:", len(customers))
print("Unique customer_id values:", customers["customer_id"].nunique())
print("Unique customer_unique_id values:", customers["customer_unique_id"].nunique())

print(
    "Customer records beyond unique people:",
    len(customers) - customers["customer_unique_id"].nunique()
)

print("\nExample records:")
print(
    customers[
        ["customer_id", "customer_unique_id", "customer_city"]
    ].head(10).to_string(index=False)
)
