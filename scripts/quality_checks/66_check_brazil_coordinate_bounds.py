
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

# Approximate bounding box for Brazil; used for anomaly screening.
brazil_mask = (
    geo["geolocation_lat"].between(-34, 6)
    & geo["geolocation_lng"].between(-74, -34)
)

outside_mask = ~brazil_mask

print("BRAZIL GEOGRAPHIC BOUNDS CHECK")
print("=" * 55)
print("Total geolocation rows:", len(geo))
print("Rows within approximate Brazil bounds:", brazil_mask.sum())
print("Rows outside approximate Brazil bounds:", outside_mask.sum())
print(
    "Percentage outside bounds:",
    round(outside_mask.mean() * 100, 2)
)

if outside_mask.any():
    print("\nFirst 10 rows outside the bounds:")
    print(
        geo.loc[
            outside_mask,
            [
                "geolocation_zip_code_prefix",
                "geolocation_lat",
                "geolocation_lng",
                "geolocation_city",
                "geolocation_state",
            ],
        ].head(10).to_string(index=False)
    )

print("\nSource data remains unchanged.")
