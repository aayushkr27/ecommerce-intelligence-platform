CREATE TABLE mart_review_sentiment AS
SELECT
    CASE
        WHEN review_score >= 4 THEN 'Positive (4–5)'
        WHEN review_score = 3 THEN 'Neutral (3)'
        WHEN review_score <= 2 THEN 'Negative (1–2)'
    END AS review_sentiment,

    COUNT(*) AS total_reviews,

    ROUND(AVG(review_score), 2) AS average_review_score

FROM clean_order_reviews

WHERE review_score IS NOT NULL

GROUP BY
    CASE
        WHEN review_score >= 4 THEN 'Positive (4–5)'
        WHEN review_score = 3 THEN 'Neutral (3)'
        WHEN review_score <= 2 THEN 'Negative (1–2)'
    END;

SELECT *
FROM mart_review_sentiment;