
USE olist_analytics;

SELECT
    COUNT(*) AS total_sellers,
    COUNT(DISTINCT seller_id) AS unique_seller_ids,
    SUM(seller_id IS NULL OR seller_id = '') AS missing_seller_ids,
    SUM(seller_zip_code_prefix IS NULL
        OR seller_zip_code_prefix = '') AS missing_zip_codes,
    SUM(seller_city IS NULL OR seller_city = '') AS missing_cities,
    SUM(seller_state IS NULL OR seller_state = '') AS missing_states
FROM stg_sellers;
