CREATE TABLE mart_customer_retention AS
WITH customer_order_counts AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM clean_customers AS c
    INNER JOIN clean_orders AS o
        ON c.customer_id = o.customer_id
    WHERE c.customer_unique_id IS NOT NULL
    GROUP BY c.customer_unique_id
)
SELECT
    customer_unique_id,
    total_orders,
    CASE
        WHEN total_orders = 1 THEN '1 order'
        WHEN total_orders = 2 THEN '2 orders'
        ELSE '3+ orders'
    END AS customer_order_group
FROM customer_order_counts;

SELECT
    customer_order_group,
    COUNT(*) AS number_of_customers,
    ROUND(
        100.0 * COUNT(*) / (SELECT COUNT(*) FROM mart_customer_retention),
        2
    ) AS percentage_of_customers
FROM mart_customer_retention
GROUP BY customer_order_group
ORDER BY
    CASE customer_order_group
        WHEN '1 order' THEN 1
        WHEN '2 orders' THEN 2
        ELSE 3
    END;