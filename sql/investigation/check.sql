WITH payment_totals AS (
    SELECT
        order_id,
        SUM(payment_value) AS payment_value
    FROM clean_order_payments
    GROUP BY order_id
)
SELECT
    o.order_status,
    COUNT(*) AS orders_without_items_with_payment,
    ROUND(SUM(p.payment_value), 2) AS recorded_payment_value
FROM clean_orders AS o
INNER JOIN payment_totals AS p
    ON o.order_id = p.order_id
LEFT JOIN clean_order_items AS i
    ON o.order_id = i.order_id
WHERE o.order_status IN ('canceled', 'unavailable')
  AND i.order_id IS NULL
  AND p.payment_value > 0
GROUP BY o.order_status;