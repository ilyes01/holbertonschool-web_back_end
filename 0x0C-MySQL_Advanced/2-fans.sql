--SQL script that ranks country origins of bands 
--order by the number of "non unique" fans 
SELECT origin, SUM(fans) AS nb-fans
FROM metal bands
GROUB BY oringin
ORDER BY nb_fans DESC;

