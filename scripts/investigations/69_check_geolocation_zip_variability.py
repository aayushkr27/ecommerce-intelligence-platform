
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

zip_summary = (
    geo.groupby("geolocation_zip_code_prefix")
    .agg(
        total_rows=("geolocation_zip_code_prefix", "size"),
        distinct_coordinates=(
            "geolocation_lat",
            "count"
        ),
    )
)

# Count unique latitude-longitude pairs per ZIP prefix.
coordinate_counts = (
    geo.drop_duplicates(
        subset=[
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
        ]
    )
    .groupby("geolocation_zip_code_prefix")
    .size()
)

zip_summary["distinct_coordinate_pairs"] = coordinate_counts

print("GEOLOCATION ZIP-PREFIX VARIABILITY CHECK")
print("=" * 55)
print("Total geolocation rows:", len(geo))
print("Unique ZIP prefixes:", geo["geolocation_zip_code_prefix"].nunique())
print(
    "ZIP prefixes with multiple coordinate pairs:",
    (zip_summary["distinct_coordinate_pairs"] > 1).sum()
)
print(
    "Maximum coordinate pairs for one ZIP prefix:",
    zip_summary["distinct_coordinate_pairs"].max()
)

print("\nDistribution of coordinate pairs per ZIP prefix:")
print(
    zip_summary["distinct_coordinate_pairs"]
    .value_counts()
    .sort_index()
    .rename_axis("coordinate_pairs")
    .rename("zip_prefix_count")
    .to_string()
)

print("\nTop 10 ZIP prefixes by distinct coordinate pairs:")
print(
    zip_summary.sort_values(
        "distinct_coordinate_pairs",
        ascending=False
    ).head(10).to_string()
)

print("\nNo records have been deleted or modified.")
