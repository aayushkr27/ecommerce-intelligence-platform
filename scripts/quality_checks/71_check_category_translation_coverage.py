
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_DIR / "data" / "raw"

products = pd.read_csv(RAW_DIR / "olist_products_dataset.csv")
translations = pd.read_csv(
    RAW_DIR / "product_category_name_translation.csv"
)

product_categories = set(
    products["product_category_name"].dropna().unique()
)
translated_categories = set(
    translations["product_category_name"].dropna().unique()
)

untranslated = product_categories - translated_categories
unused_translations = translated_categories - product_categories

print("CATEGORY TRANSLATION COVERAGE CHECK")
print("=" * 55)

print("Unique non-null product categories:", len(product_categories))
print("Translated Portuguese categories:", len(translated_categories))
print("Categories without translations:", len(untranslated))
print("Translation categories not used by products:", len(unused_translations))

print("\nCategories without translations:")
print(sorted(untranslated) if untranslated else "None")

print("\nTranslations not used by products:")
print(sorted(unused_translations) if unused_translations else "None")

print("\nNo source records have been modified.")
