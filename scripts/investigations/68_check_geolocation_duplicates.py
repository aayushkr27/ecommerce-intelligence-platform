
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

duplicate_mask = geo.duplicated(keep=False)
extra_duplicate_rows = geo.duplicated(keep="first")

print("GEOLOCATION EXACT DUPLICATE CHECK")
print("=" * 55)
print("Total geolocation rows:", len(geo))
print("Rows involved in exact duplicate groups:", duplicate_mask.sum())
print("Extra exact duplicate rows:", extra_duplicate_rows.sum())
print("Unique ZIP prefixes:", geo["geolocation_zip_code_prefix"].nunique())

print("\nSample exact duplicate rows:")
if extra_duplicate_rows.any():
    print(geo.loc[duplicate_mask].head(10).to_string(index=False))
else:
    print("No exact duplicate rows found.")

print("\nNo records have been deleted or modified.")
