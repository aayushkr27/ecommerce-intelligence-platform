
USE olist_analytics;

CREATE TABLE clean_order_payments AS
SELECT
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
FROM stg_order_payments;


SELECT
    COUNT(*) AS total_payment_records,
    COUNT(DISTINCT CONCAT(order_id, '-', payment_sequential))
        AS unique_payment_keys,
    SUM(payment_value IS NULL OR payment_value < 0)
        AS invalid_payment_values,
    SUM(payment_value = 0) AS zero_value_payments
FROM clean_order_payments;

DESCRIBE clean_order_payments;
