
USE olist_analytics;

CREATE TABLE clean_geolocation AS
SELECT
    geolocation_zip_code_prefix,
    AVG(geolocation_lat) AS latitude,
    AVG(geolocation_lng) AS longitude
FROM stg_geolocation
WHERE geolocation_lat BETWEEN -90 AND 90
  AND geolocation_lng BETWEEN -180 AND 180
GROUP BY geolocation_zip_code_prefix;


SELECT
    COUNT(*) AS total_zip_prefixes,
    COUNT(DISTINCT geolocation_zip_code_prefix)
        AS unique_zip_prefixes,
    SUM(latitude IS NULL OR longitude IS NULL)
        AS missing_coordinates
FROM clean_geolocation;
