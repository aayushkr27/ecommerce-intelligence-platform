
USE olist_analytics;

CREATE TABLE clean_order_reviews AS
SELECT
    review_id,
    order_id,
    review_score,
    NULLIF(TRIM(review_comment_title), '') AS review_comment_title,
    NULLIF(TRIM(review_comment_message), '') AS review_comment_message,
    STR_TO_DATE(
        NULLIF(review_creation_date, ''),
        '%Y-%m-%d %H:%i:%s'
    ) AS review_creation_date,
    STR_TO_DATE(
        NULLIF(review_answer_timestamp, ''),
        '%Y-%m-%d %H:%i:%s'
    ) AS review_answer_timestamp
FROM stg_order_reviews;


SELECT
    COUNT(*) AS total_reviews,
    COUNT(DISTINCT review_id) AS distinct_review_ids,
    SUM(review_score IS NULL OR review_score NOT BETWEEN 1 AND 5)
        AS invalid_review_scores,
    SUM(review_comment_title IS NULL) AS missing_review_titles,
    SUM(review_comment_message IS NULL) AS missing_review_messages
FROM clean_order_reviews;

DESCRIBE clean_order_reviews;
