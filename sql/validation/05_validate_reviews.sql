
USE olist_analytics;

SELECT
    COUNT(*) AS total_reviews,
    COUNT(DISTINCT review_id) AS distinct_review_ids,
    SUM(review_id IS NULL OR review_id = '') AS missing_review_ids,
    SUM(order_id IS NULL OR order_id = '') AS missing_order_ids,
    SUM(review_score IS NULL OR review_score NOT BETWEEN 1 AND 5)
        AS invalid_review_scores,
    SUM(review_comment_title IS NULL OR review_comment_title = '')
        AS missing_review_titles,
    SUM(review_comment_message IS NULL OR review_comment_message = '')
        AS missing_review_messages
FROM stg_order_reviews;
