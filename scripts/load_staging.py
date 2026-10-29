
import csv
import getpass
from pathlib import Path

import mysql.connector

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

# Expected row counts from Module 1 profiling
DATASETS = [
    ("olist_customers_dataset.csv", "stg_customers", 99441),
    ("olist_geolocation_dataset.csv", "stg_geolocation", 1000163),
    ("olist_orders_dataset.csv", "stg_orders", 99441),
    ("olist_order_items_dataset.csv", "stg_order_items", 112650),
    ("olist_order_payments_dataset.csv", "stg_order_payments", 103886),
    ("olist_order_reviews_dataset.csv", "stg_order_reviews", 99224),
    ("olist_products_dataset.csv", "stg_products", 32951),
    ("olist_sellers_dataset.csv", "stg_sellers", 3095),
    (
        "product_category_name_translation.csv",
        "stg_category_translation",
        71,
    ),
]

BATCH_SIZE = 2000


def main():
    print("Olist CSV-to-MySQL staging loader")
    print(f"CSV folder: {RAW_DIR}")

    if not RAW_DIR.is_dir():
        raise FileNotFoundError(f"Raw data folder not found: {RAW_DIR}")

    # Check that every source file exists before connecting.
    for filename, _, _ in DATASETS:
        if not (RAW_DIR / filename).is_file():
            raise FileNotFoundError(f"Missing CSV: {filename}")

    password = getpass.getpass("Enter MySQL root password: ")

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=password,
        database="olist_analytics",
    )

    try:
        cursor = connection.cursor()

        # Check all tables before inserting anything.
        print("\nChecking target tables...")
        table_counts = {}

        for _, table, expected in DATASETS:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            existing = cursor.fetchone()[0]
            table_counts[table] = existing

            if existing not in (0, expected):
                raise RuntimeError(
                    f"{table} contains {existing} rows; expected either "
                    f"0 (empty) or {expected} (complete). "
                    "Import stopped to avoid duplicate data."
                )

        print("Pre-check passed. Starting imports...\n")

        for filename, table, expected in DATASETS:
            existing = table_counts[table]

            # Makes reruns safe if a table was already fully imported.
            if existing == expected:
                print(f"SKIP {table}: already has {expected:,} rows")
                continue

            file_path = RAW_DIR / filename
            print(f"Loading {filename} -> {table}")

            inserted = 0
            batch = []

            try:
                with file_path.open(
                    "r", encoding="utf-8-sig", newline=""
                ) as csv_file:
                    reader = csv.reader(csv_file)

                    # First row contains column names.
                    header = next(reader, None)
                    if not header:
                        raise ValueError(f"{filename} is empty")

                    placeholders = ", ".join(["%s"] * len(header))
                    sql = (
                        f"INSERT INTO `{table}` "
                        f"VALUES ({placeholders})"
                    )

                    for row in reader:
                        if len(row) != len(header):
                            raise ValueError(
                                f"{filename}: row {inserted + 2} has "
                                f"{len(row)} fields; expected {len(header)}"
                            )

                        # Convert empty CSV fields to SQL NULL.
                        values = tuple(
                            None if value == "" else value
                            for value in row
                        )
                        batch.append(values)

                        if len(batch) >= BATCH_SIZE:
                            cursor.executemany(sql, batch)
                            inserted += len(batch)
                            batch.clear()

                    if batch:
                        cursor.executemany(sql, batch)
                        inserted += len(batch)

                if inserted != expected:
                    raise ValueError(
                        f"{filename}: imported {inserted:,} rows; "
                        f"expected {expected:,}"
                    )

                connection.commit()
                print(f"OK   {table}: {inserted:,} rows imported\n")

            except Exception:
                connection.rollback()
                raise

        print("Verifying final SQL row counts...")
        for _, table, expected in DATASETS:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            actual = cursor.fetchone()[0]
            status = "PASS" if actual == expected else "CHECK"
            print(f"{status}: {table}: {actual:,} / {expected:,}")

        print("\nImport process finished.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()
