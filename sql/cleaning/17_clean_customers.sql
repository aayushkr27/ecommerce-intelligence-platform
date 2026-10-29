
USE olist_analytics;

CREATE TABLE clean_customers AS
SELECT
    customer_id,
    customer_unique_id,
    LPAD(TRIM(customer_zip_code_prefix), 5, '0')
        AS customer_zip_code_prefix,
    NULLIF(TRIM(customer_city), '') AS customer_city,
    NULLIF(TRIM(customer_state), '') AS customer_state
FROM stg_customers;


SELECT
    COUNT(*) AS total_customer_records,
    COUNT(DISTINCT customer_id) AS unique_customer_ids,
    COUNT(DISTINCT customer_unique_id) AS unique_customers,
    SUM(CHAR_LENGTH(customer_zip_code_prefix) <> 5
        OR customer_zip_code_prefix IS NULL) AS invalid_zip_prefixes
FROM clean_customers;

DESCRIBE clean_customers;
