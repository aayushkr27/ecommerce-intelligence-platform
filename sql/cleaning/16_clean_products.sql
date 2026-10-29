
USE olist_analytics;

CREATE TABLE clean_products AS
SELECT
    product_id,
    NULLIF(TRIM(product_category_name), '') AS product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
FROM stg_products;


SELECT
    COUNT(*) AS total_products,
    COUNT(DISTINCT product_id) AS unique_product_ids,
    SUM(product_category_name IS NULL) AS missing_categories,
    SUM(product_weight_g IS NULL) AS missing_weights,
    SUM(product_length_cm IS NULL) AS missing_lengths,
    SUM(product_height_cm IS NULL) AS missing_heights,
    SUM(product_width_cm IS NULL) AS missing_widths
FROM clean_products;

DESCRIBE clean_products;
