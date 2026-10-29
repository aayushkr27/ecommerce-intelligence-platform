WITH item_totals AS (
    SELECT
        order_id,
        SUM(price) AS product_value,
        SUM(freight_value) AS freight_value
    FROM clean_order_items
    GROUP BY order_id
),
payment_totals AS (
    SELECT
        order_id,
        SUM(payment_value) AS payment_value
    FROM clean_order_payments
    GROUP BY order_id
),
order_comparison AS (
    SELECT
        o.order_id,
        o.order_status,
        COALESCE(i.product_value, 0) AS product_value,
        COALESCE(i.freight_value, 0) AS freight_value,
        COALESCE(p.payment_value, 0) AS payment_value,
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END AS no_items,
        CASE WHEN p.order_id IS NULL THEN 1 ELSE 0 END AS no_payment
    FROM clean_orders o
    LEFT JOIN item_totals i ON o.order_id = i.order_id
    LEFT JOIN payment_totals p ON o.order_id = p.order_id
)
SELECT
    COUNT(*) AS total_orders,
    SUM(no_items) AS orders_without_items,
    SUM(no_payment) AS orders_without_payments,
    SUM(CASE
        WHEN no_items = 0 AND no_payment = 0
        THEN 1 ELSE 0
    END) AS orders_with_items_and_payments,
    ROUND(SUM(product_value + freight_value), 2) AS item_value_including_freight,
    ROUND(SUM(payment_value), 2) AS recorded_payment_value,
    ROUND(SUM(payment_value - product_value - freight_value), 2)
        AS payment_minus_item_value
FROM order_comparison;