
USE olist_analytics;

SELECT
    'orders -> customers' AS relationship_name,
    COUNT(*) AS unmatched_rows
FROM stg_orders o
LEFT JOIN stg_customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL

UNION ALL

SELECT
    'order_items -> orders',
    COUNT(*)
FROM stg_order_items i
LEFT JOIN stg_orders o
    ON i.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT
    'order_items -> products',
    COUNT(*)
FROM stg_order_items i
LEFT JOIN stg_products p
    ON i.product_id = p.product_id
WHERE p.product_id IS NULL

UNION ALL

SELECT
    'order_items -> sellers',
    COUNT(*)
FROM stg_order_items i
LEFT JOIN stg_sellers s
    ON i.seller_id = s.seller_id
WHERE s.seller_id IS NULL

UNION ALL

SELECT
    'payments -> orders',
    COUNT(*)
FROM stg_order_payments p
LEFT JOIN stg_orders o
    ON p.order_id = o.order_id
WHERE o.order_id IS NULL

UNION ALL

SELECT
    'reviews -> orders',
    COUNT(*)
FROM stg_order_reviews r
LEFT JOIN stg_orders o
    ON r.order_id = o.order_id
WHERE o.order_id IS NULL;
