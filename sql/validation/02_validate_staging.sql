

USE olist_analytics;

SELECT
    COUNT(*) AS total_orders,
    COUNT(DISTINCT order_id) AS unique_order_ids,
    SUM(order_id IS NULL OR order_id = '') AS missing_order_ids,
    SUM(customer_id IS NULL OR customer_id = '') AS missing_customer_ids,
    SUM(order_purchase_timestamp IS NULL
        OR order_purchase_timestamp = '') AS missing_purchase_timestamps,
    SUM(order_approved_at IS NULL
        OR order_approved_at = '') AS missing_approval_timestamps,
    SUM(order_delivered_carrier_date IS NULL
        OR order_delivered_carrier_date = '') AS missing_carrier_timestamps,
    SUM(order_delivered_customer_date IS NULL
        OR order_delivered_customer_date = '') AS missing_delivery_timestamps
FROM stg_orders;
