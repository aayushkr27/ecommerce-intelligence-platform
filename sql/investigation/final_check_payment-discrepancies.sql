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
)
SELECT
    o.order_status,
    COUNT(*) AS total_orders,
    SUM(
        CASE WHEN i.order_id IS NULL THEN 1 ELSE 0 END
    ) AS orders_without_items,
    ROUND(SUM(COALESCE(i.product_value, 0)), 2) AS product_value,
    ROUND(SUM(COALESCE(i.freight_value, 0)), 2) AS freight_value,
    ROUND(SUM(COALESCE(p.payment_value, 0)), 2) AS payment_value,
    ROUND(
        SUM(
            COALESCE(p.payment_value, 0)
            - COALESCE(i.product_value, 0)
            - COALESCE(i.freight_value, 0)
        ),
        2
    ) AS payment_minus_item_value
FROM clean_orders o
LEFT JOIN item_totals i
    ON o.order_id = i.order_id
LEFT JOIN payment_totals p
    ON o.order_id = p.order_id
GROUP BY o.order_status
ORDER BY ABS(
    SUM(
        COALESCE(p.payment_value, 0)
        - COALESCE(i.product_value, 0)
        - COALESCE(i.freight_value, 0)
    )
) DESC;