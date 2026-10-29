
USE olist_analytics;

SELECT
    COUNT(*) AS total_translation_rows,
    COUNT(DISTINCT product_category_name)
        AS unique_portuguese_categories,
    SUM(product_category_name IS NULL
        OR product_category_name = '') AS missing_source_categories,
    SUM(product_category_name_english IS NULL
        OR product_category_name_english = '') AS missing_english_translations
FROM stg_category_translation;
