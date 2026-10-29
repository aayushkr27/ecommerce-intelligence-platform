SELECT
    COUNT(*) AS eligible_delivered_orders,

    SUM(
        CASE WHEN delivery_status = 'On time or early'
        THEN 1 ELSE 0 END
    ) AS on_time_orders,

    ROUND(
        100.0 * AVG(
            CASE WHEN delivery_status = 'On time or early'
            THEN 1.0 ELSE 0.0 END
        ),
        2
    ) AS on_time_delivery_percentage,

    ROUND(AVG(days_to_delivery), 2) AS avg_days_to_delivery

FROM mart_delivery_performance;