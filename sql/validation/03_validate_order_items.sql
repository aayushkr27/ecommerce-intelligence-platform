
USE olist_analytics;

SELECT
    COUNT(*) AS total_order_items,
    COUNT(DISTINCT CONCAT(order_id, '-', order_item_id))
        AS unique_order_item_keys,
    SUM(order_id IS NULL OR order_id = '') AS missing_order_ids,
    SUM(product_id IS NULL OR product_id = '') AS missing_product_ids,
    SUM(seller_id IS NULL OR seller_id = '') AS missing_seller_ids,
    SUM(price IS NULL OR price <= 0) AS invalid_prices,
    SUM(freight_value IS NULL OR freight_value < 0)
        AS invalid_freight_values
FROM stg_order_items;
