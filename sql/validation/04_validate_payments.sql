
USE olist_analytics;

SELECT
    COUNT(*) AS total_payment_records,
    COUNT(DISTINCT CONCAT(order_id, '-', payment_sequential))
        AS unique_payment_keys,
    SUM(order_id IS NULL OR order_id = '') AS missing_order_ids,
    SUM(payment_value IS NULL OR payment_value < 0)
        AS invalid_payment_values,
    SUM(payment_value = 0) AS zero_value_payments,
    SUM(payment_type IS NULL OR payment_type = '')
        AS missing_payment_types,
    SUM(payment_sequential IS NULL OR payment_sequential < 1)
        AS invalid_payment_sequences
FROM stg_order_payments;
