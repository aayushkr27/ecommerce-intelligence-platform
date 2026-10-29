
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
SELLERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_sellers_dataset.csv"
)

sellers = pd.read_csv(SELLERS_FILE)

zip_codes = (
    sellers["seller_zip_code_prefix"]
    .astype("string")
    .str.strip()
    .str.zfill(5)
)

print("SELLER ZIP-CODE FORMATTING CHECK")
print("=" * 55)
print("Total seller records:", len(sellers))
print("Missing ZIP prefixes:", sellers["seller_zip_code_prefix"].isna().sum())
print(
    "Prefixes not exactly 5 digits:",
    (~zip_codes.str.fullmatch(r"\d{5}")).sum()
)
print("Minimum formatted prefix:", zip_codes.min())
print("Maximum formatted prefix:", zip_codes.max())

print("\nFirst 10 formatted prefixes:")
print(zip_codes.drop_duplicates().head(10).to_list())

print("\nOriginal source data remains unchanged.")
