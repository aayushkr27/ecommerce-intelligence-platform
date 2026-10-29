
USE olist_analytics;

CREATE TABLE clean_order_items AS
SELECT
    order_id,
    order_item_id,
    product_id,
    seller_id,
    STR_TO_DATE(
        NULLIF(shipping_limit_date, ''),
        '%Y-%m-%d %H:%i:%s'
    ) AS shipping_limit_date,
    price,
    freight_value
FROM stg_order_items;


SELECT
    COUNT(*) AS total_order_items,
    COUNT(DISTINCT CONCAT(order_id, '-', order_item_id))
        AS unique_order_item_keys,
    SUM(price IS NULL OR price <= 0) AS invalid_prices,
    SUM(freight_value IS NULL OR freight_value < 0)
        AS invalid_freight_values
FROM clean_order_items;

DESCRIBE clean_order_items;
