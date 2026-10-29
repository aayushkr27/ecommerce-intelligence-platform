
USE olist_analytics;

SELECT
    COUNT(*) AS total_products,
    COUNT(DISTINCT product_id) AS unique_product_ids,
    SUM(product_id IS NULL OR product_id = '') AS missing_product_ids,
    SUM(product_category_name IS NULL
        OR product_category_name = '') AS missing_categories,
    SUM(product_weight_g IS NULL OR product_weight_g <= 0)
        AS invalid_weights,
    SUM(product_length_cm IS NULL OR product_length_cm <= 0)
        AS invalid_lengths,
    SUM(product_height_cm IS NULL OR product_height_cm <= 0)
        AS invalid_heights,
    SUM(product_width_cm IS NULL OR product_width_cm <= 0)
        AS invalid_widths
FROM stg_products;
