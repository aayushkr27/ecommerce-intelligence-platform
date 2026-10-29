
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

missing_report = pd.DataFrame({
    "missing_count": geo.isna().sum(),
    "missing_percentage": (
        geo.isna().mean() * 100
    ).round(2)
})

print("GEOLOCATION TABLE — RAW PROFILE")
print("=" * 55)
print("Rows:", len(geo))
print("Columns:", len(geo.columns))

print("\nColumn names:")
print(geo.columns.tolist())

print("\nData types:")
print(geo.dtypes.to_string())

print("\nMissing values report:")
print(missing_report.to_string())

print("\nTotal missing cells:", int(geo.isna().sum().sum()))
