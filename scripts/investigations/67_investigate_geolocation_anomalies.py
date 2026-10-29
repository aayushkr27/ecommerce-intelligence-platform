
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
GEO_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
)

geo = pd.read_csv(GEO_FILE)

brazil_mask = (
    geo["geolocation_lat"].between(-34, 6)
    & geo["geolocation_lng"].between(-74, -34)
)

anomalies = geo.loc[~brazil_mask].copy()

print("GEOLOCATION ANOMALY INVESTIGATION")
print("=" * 55)
print("Anomalous rows:", len(anomalies))
print("Distinct ZIP prefixes affected:",
      anomalies["geolocation_zip_code_prefix"].nunique())
print("Distinct cities affected:",
      anomalies["geolocation_city"].nunique())
print("Distinct states affected:",
      anomalies["geolocation_state"].nunique())

print("\nAnomalies by state:")
print(anomalies["geolocation_state"].value_counts().to_string())

print("\nAnomalies by ZIP prefix:")
print(
    anomalies.groupby("geolocation_zip_code_prefix")
    .size()
    .sort_values(ascending=False)
    .head(15)
    .to_string()
)

print("\nFull anomaly sample:")
print(anomalies.to_string(index=False))

print("\nNo rows have been deleted or modified.")
