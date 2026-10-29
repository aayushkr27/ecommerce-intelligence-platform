
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
CUSTOMERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_customers_dataset.csv"
)

customers = pd.read_csv(CUSTOMERS_FILE)

missing_report = pd.DataFrame({
    "missing_count": customers.isna().sum(),
    "missing_percentage": (
        customers.isna().mean() * 100
    ).round(2)
})

print("CUSTOMERS TABLE — RAW PROFILE")
print("=" * 55)
print("Rows:", len(customers))
print("Columns:", len(customers.columns))

print("\nColumn names:")
print(customers.columns.tolist())

print("\nData types:")
print(customers.dtypes.to_string())

print("\nMissing values report:")
print(missing_report.to_string())

print("\nTotal missing cells:", int(customers.isna().sum().sum()))
