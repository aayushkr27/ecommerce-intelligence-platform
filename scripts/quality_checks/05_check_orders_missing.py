
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"
)

orders = pd.read_csv(ORDERS_FILE)

# Count missing values in each column.
missing_counts = orders.isna().sum()

# Calculate the percentage of missing values.
missing_percentages = (
    orders.isna().mean() * 100
).round(2)

# Combine the results into one report.
report = pd.DataFrame({
    "missing_count": missing_counts,
    "missing_percentage": missing_percentages
})

print("MISSING VALUES REPORT — ORDERS")
print("=" * 50)
print(report.to_string())

print("\nTotal missing cells:", int(orders.isna().sum().sum()))
