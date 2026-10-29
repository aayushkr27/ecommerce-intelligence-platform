
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
SELLERS_FILE = (
    PROJECT_DIR / "data" / "raw" / "olist_sellers_dataset.csv"
)

sellers = pd.read_csv(SELLERS_FILE)

states = sellers["seller_state"].astype("string").str.strip()

invalid_mask = ~states.str.fullmatch(r"[A-Z]{2}").fillna(False)

print("SELLER STATE CODE VALIDATION")
print("=" * 50)
print("Total seller records:", len(sellers))
print("Missing state codes:", states.isna().sum())
print("Invalid state-code formats:", invalid_mask.sum())

if invalid_mask.any():
    print("\nInvalid values:")
    print(states[invalid_mask].value_counts().to_string())

print("\nDistinct state codes:", states.nunique())

if states.notna().all() and not invalid_mask.any():
    print("\nPASS: All seller state codes have valid two-letter formats.")
else:
    print("\nWARNING: Investigate missing or invalid state codes.")
