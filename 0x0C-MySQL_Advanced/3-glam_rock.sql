--comments
--comments
SELECT band_name,
    (YEAR(split) - YEAR(formed)) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
