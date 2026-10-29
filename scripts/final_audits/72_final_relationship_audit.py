
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_DIR / "data" / "raw"

def load_csv(filename):
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

# Load the source tables
orders = load_csv("olist_orders_dataset.csv")
items = load_csv("olist_order_items_dataset.csv")
payments = load_csv("olist_order_payments_dataset.csv")
reviews = load_csv("olist_order_reviews_dataset.csv")
products = load_csv("olist_products_dataset.csv")
sellers = load_csv("olist_sellers_dataset.csv")
customers = load_csv("olist_customers_dataset.csv")
translations = load_csv("product_category_name_translation.csv")

print("FINAL CROSS-TABLE RELATIONSHIP AUDIT")
print("=" * 65)

# 1. Check whether expected primary/composite keys are unique
key_checks = [
    ("Orders", orders, ["order_id"]),
    ("Order items", items, ["order_id", "order_item_id"]),
    ("Payments", payments, ["order_id", "payment_sequential"]),
    ("Products", products, ["product_id"]),
    ("Sellers", sellers, ["seller_id"]),
    ("Customers", customers, ["customer_id"]),
    ("Category translations", translations, ["product_category_name"]),
]

print("\n1. KEY UNIQUENESS CHECKS")
print("-" * 65)

for name, df, key_columns in key_checks:
    missing_key_rows = df[key_columns].isna().any(axis=1).sum()
    duplicate_key_rows = df.duplicated(
        subset=key_columns, keep=False
    ).sum()

    print(f"\n{name}")
    print("  Key columns:", key_columns)
    print("  Rows with missing key values:", missing_key_rows)
    print("  Rows involved in duplicate key groups:", duplicate_key_rows)

# 2. Check foreign-key relationships
print("\n\n2. FOREIGN-KEY RELATIONSHIP CHECKS")
print("-" * 65)

relationships = [
    (
        "orders.customer_id -> customers.customer_id",
        orders, "customer_id", customers, "customer_id"
    ),
    (
        "items.order_id -> orders.order_id",
        items, "order_id", orders, "order_id"
    ),
    (
        "items.product_id -> products.product_id",
        items, "product_id", products, "product_id"
    ),
    (
        "items.seller_id -> sellers.seller_id",
        items, "seller_id", sellers, "seller_id"
    ),
    (
        "payments.order_id -> orders.order_id",
        payments, "order_id", orders, "order_id"
    ),
    (
        "reviews.order_id -> orders.order_id",
        reviews, "order_id", orders, "order_id"
    ),
]

for label, child, child_col, parent, parent_col in relationships:
    parent_ids = set(parent[parent_col].dropna().unique())
    child_ids = child[child_col]

    missing_values = child_ids.isna().sum()
    unmatched_mask = child_ids.notna() & ~child_ids.isin(parent_ids)
    unmatched_rows = int(unmatched_mask.sum())
    unmatched_ids = int(child_ids[unmatched_mask].nunique())

    print(f"\n{label}")
    print("  Rows in referencing table:", len(child))
    print("  Missing foreign-key values:", missing_values)
    print("  Unmatched rows:", unmatched_rows)
    print("  Distinct unmatched IDs:", unmatched_ids)

    if unmatched_ids:
        print("  Sample unmatched IDs:",
              child_ids[unmatched_mask].drop_duplicates().head(5).tolist())

# 3. Explain the known order coverage difference
print("\n\n3. ORDER COVERAGE SUMMARY")
print("-" * 65)

order_ids = set(orders["order_id"].dropna().unique())
item_order_ids = set(items["order_id"].dropna().unique())

orders_without_items = order_ids - item_order_ids

print("Total orders:", len(order_ids))
print("Distinct orders represented in items:", len(item_order_ids))
print("Orders without item records:", len(orders_without_items))

print("\nStatuses of orders without item records:")
if orders_without_items:
    missing_item_orders = orders[
        orders["order_id"].isin(orders_without_items)
    ]
    print(missing_item_orders["order_status"].value_counts().to_string())
else:
    print("None")

print("\nNo source records have been deleted or modified.")
