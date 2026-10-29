
USE olist_analytics;

SELECT
    COUNT(*) AS total_customer_records,
    COUNT(DISTINCT customer_id) AS unique_customer_ids,
    COUNT(DISTINCT customer_unique_id) AS unique_customers,
    SUM(customer_id IS NULL OR customer_id = '') AS missing_customer_ids,
    SUM(customer_unique_id IS NULL
        OR customer_unique_id = '') AS missing_unique_customer_ids,
    SUM(customer_zip_code_prefix IS NULL
        OR customer_zip_code_prefix = '') AS missing_zip_codes,
    SUM(customer_city IS NULL OR customer_city = '') AS missing_cities,
    SUM(customer_state IS NULL OR customer_state = '') AS missing_states
FROM stg_customers;
