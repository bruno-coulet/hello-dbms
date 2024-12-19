
--1. Classement des pays par émissions totale (toutes sources combinées)
SELECT country, 
       (coal_emissions + gas_emissions + oil_emissions + hydro_emissions + renewable_emissions + nuclear_emissions) AS total_emissions
FROM country
ORDER BY total_emissions DESC
LIMIT 20;
