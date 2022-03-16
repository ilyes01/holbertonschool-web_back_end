--sql script that lists alll bands with glam rock 
--ranked by their longevity
SELECT band_name, (IFNULL(split, 2020) - fomred) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
