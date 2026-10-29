CREATE TABLE mart_payment_analysis AS
SELECT
    payment_type,
    COUNT(*) AS payment_records,
    COUNT(DISTINCT order_id) AS unique_orders,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    ROUND(AVG(payment_value), 2) AS avg_payment_record_value
FROM clean_order_payments
GROUP BY payment_type;

SELECT *
FROM mart_payment_analysis
ORDER BY total_payment_value DESC;