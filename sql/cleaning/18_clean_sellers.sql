
USE olist_analytics;

CREATE TABLE clean_sellers AS
SELECT
    seller_id,
    LPAD(TRIM(seller_zip_code_prefix), 5, '0')
        AS seller_zip_code_prefix,
    NULLIF(TRIM(seller_city), '') AS seller_city,
    NULLIF(TRIM(seller_state), '') AS seller_state
FROM stg_sellers;


SELECT
    COUNT(*) AS total_sellers,
    COUNT(DISTINCT seller_id) AS unique_seller_ids,
    SUM(CHAR_LENGTH(seller_zip_code_prefix) <> 5
        OR seller_zip_code_prefix IS NULL) AS invalid_zip_prefixes
FROM clean_sellers;

DESCRIBE clean_sellers;
