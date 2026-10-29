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
    o.order_id,
    o.order_status,
    ROUND(COALESCE(i.product_value, 0), 2) AS product_value,
    ROUND(COALESCE(i.freight_value, 0), 2) AS freight_value,
    ROUND(COALESCE(p.payment_value, 0), 2) AS payment_value,
    ROUND(
        COALESCE(p.payment_value, 0)
        - COALESCE(i.product_value, 0)
        - COALESCE(i.freight_value, 0),
        2
    ) AS difference
FROM clean_orders AS o
LEFT JOIN item_totals AS i
    ON o.order_id = i.order_id
LEFT JOIN payment_totals AS p
    ON o.order_id = p.order_id
WHERE ABS(
    COALESCE(p.payment_value, 0)
    - COALESCE(i.product_value, 0)
    - COALESCE(i.freight_value, 0)
) > 100
ORDER BY ABS(
    COALESCE(p.payment_value, 0)
    - COALESCE(i.product_value, 0)
    - COALESCE(i.freight_value, 0)
) DESC
LIMIT 20;