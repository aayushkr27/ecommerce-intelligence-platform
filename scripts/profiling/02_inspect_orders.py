
from pathlib import Path
import pandas as pd

# Locate the project and source file.
PROJECT_DIR = Path(__file__).resolve().parents[2]
ORDERS_FILE = PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"

# Read the orders table.
orders = pd.read_csv(ORDERS_FILE)

# Display the table structure.
print("TABLE: OLIST ORDERS")
print("-" * 50)

print("\nShape (rows, columns):")
print(orders.shape)

print("\nColumn names:")
print(orders.columns.tolist())

print("\nFirst five records:")
print(orders.head())

print("\nData types:")
print(orders.dtypes)
