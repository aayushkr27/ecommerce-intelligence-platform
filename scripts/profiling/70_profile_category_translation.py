
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
FILE_PATH = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "product_category_name_translation.csv"
)

df = pd.read_csv(FILE_PATH)

print("PRODUCT CATEGORY TRANSLATION PROFILE")
print("=" * 55)

print("\nShape:")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate full rows:", df.duplicated().sum())

print("\nDuplicate Portuguese category names:",
      df["product_category_name"].duplicated().sum())

print("\nDuplicate English category names:",
      df["product_category_name_english"].duplicated().sum())

print("\nUnique Portuguese categories:",
      df["product_category_name"].nunique())

print("\nUnique English categories:",
      df["product_category_name_english"].nunique())

print("\nFirst 10 rows:")
print(df.head(10).to_string(index=False))

print("\nNo source records have been modified.")
