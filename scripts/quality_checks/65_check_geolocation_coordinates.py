
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

invalid_lat = ~geo["geolocation_lat"].between(-90, 90)
invalid_lng = ~geo["geolocation_lng"].between(-180, 180)

print("GEOLOCATION COORDINATE VALIDATION")
print("=" * 55)
print("Total geolocation rows:", len(geo))
print("Missing latitude values:", geo["geolocation_lat"].isna().sum())
print("Missing longitude values:", geo["geolocation_lng"].isna().sum())
print("Invalid latitude values:", invalid_lat.sum())
print("Invalid longitude values:", invalid_lng.sum())

print("\nLatitude range:")
print("Minimum:", geo["geolocation_lat"].min())
print("Maximum:", geo["geolocation_lat"].max())

print("\nLongitude range:")
print("Minimum:", geo["geolocation_lng"].min())
print("Maximum:", geo["geolocation_lng"].max())

if not invalid_lat.any() and not invalid_lng.any():
    print("\nPASS: All coordinates fall within valid global ranges.")
else:
    print("\nWARNING: Investigate out-of-range coordinates.")
