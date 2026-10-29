
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

for file_path in sorted(RAW_DATA_DIR.glob("*.csv")):
    df = pd.read_csv(file_path, nrows=5)

    print("\n" + "=" * 70)
    print("FILE:", file_path.name)
    print("COLUMNS:", len(df.columns))
    print("COLUMN NAMES:", df.columns.tolist())
