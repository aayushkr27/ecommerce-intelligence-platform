
USE olist_analytics;

SELECT
    COUNT(*) AS total_geolocation_rows,
    COUNT(DISTINCT geolocation_zip_code_prefix)
        AS unique_zip_prefixes,
    SUM(geolocation_zip_code_prefix IS NULL
        OR geolocation_zip_code_prefix = '') AS missing_zip_codes,
    SUM(geolocation_lat IS NULL) AS missing_latitudes,
    SUM(geolocation_lng IS NULL) AS missing_longitudes,
    SUM(geolocation_lat NOT BETWEEN -90 AND 90)
        AS invalid_latitudes,
    SUM(geolocation_lng NOT BETWEEN -180 AND 180)
        AS invalid_longitudes
FROM stg_geolocation;
