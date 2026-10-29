
USE olist_analytics;

CREATE TABLE clean_orders AS
SELECT
    order_id,
    customer_id,
    order_status,
    STR_TO_DATE(order_purchase_timestamp, '%Y-%m-%d %H:%i:%s')
        AS order_purchase_timestamp,
    STR_TO_DATE(NULLIF(order_approved_at, ''),
        '%Y-%m-%d %H:%i:%s') AS order_approved_at,
    STR_TO_DATE(NULLIF(order_delivered_carrier_date, ''),
        '%Y-%m-%d %H:%i:%s') AS order_delivered_carrier_date,
    STR_TO_DATE(NULLIF(order_delivered_customer_date, ''),
        '%Y-%m-%d %H:%i:%s') AS order_delivered_customer_date,
    STR_TO_DATE(order_estimated_delivery_date, '%Y-%m-%d %H:%i:%s')
        AS order_estimated_delivery_date
FROM stg_orders;


SELECT
    COUNT(*) AS total_orders,
    COUNT(DISTINCT order_id) AS unique_order_ids
FROM clean_orders;

DESCRIBE clean_orders;

