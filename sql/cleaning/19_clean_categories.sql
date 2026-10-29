
USE olist_analytics;

CREATE TABLE clean_category_translation AS
SELECT
    NULLIF(TRIM(product_category_name), '')
        AS product_category_name,
    NULLIF(TRIM(product_category_name_english), '')
        AS product_category_name_english
FROM stg_category_translation;


SELECT
    COUNT(*) AS total_translations,
    COUNT(DISTINCT product_category_name) AS unique_categories,
    SUM(product_category_name IS NULL) AS missing_source_categories,
    SUM(product_category_name_english IS NULL) AS missing_english_names
FROM clean_category_translation;
