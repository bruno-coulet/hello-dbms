--1. Classement des pays par émissions totale (toutes sources combinées)
SELECT country,
    (
        coal_emissions + gas_emissions + oil_emissions + hydro_emissions + renewable_emissions + nuclear_emissions
    ) AS total_emissions
FROM country
ORDER BY total_emissions DESC
LIMIT 20;
--2. Pays avec la plus grande dépence au charbon 
SELECT country,
    coal_emissions
FROM country
WHERE coal_emissions > 50
ORDER BY coal_emissions DESC;
--3. Pays avec la plus grande dépence au gaz
SELECT country,
    gas_emissions
FROM country
WHERE gas_emissions > 50
ORDER BY gas_emissions DESC;
--4. Pays avec la plus grande dépence au pétrole
SELECT country,
    oil_emissions
FROM country
WHERE oil_emissions > 50
ORDER BY oil_emissions DESC;
--5. Contribution des énergies renouvelables par pays
SELECT country,
    renewable_emissions
FROM country
ORDER BY renewable_emissions DESC;
--6. Contribution des énergies nucléaires par pays
SELECT country,
    nuclear_emissions
FROM country
ORDER BY nuclear_emissions DESC;
--7. Contribution des énergies hydroélectriques par pays
SELECT country,
    hydro_emissions
FROM country
ORDER BY hydro_emissions DESC;
--8. Proportion des émissions totales par source d'énergie
SELECT SUM(coal_emissions) AS total_coal,
    SUM(gas_emissions) AS total_gas,
    SUM(oil_emissions) AS total_oil,
    SUM(hydro_emissions) AS total_hydro,
    SUM(renewable_emissions) AS total_renewables,
    SUM(nuclear_emissions) AS total_nuclear
FROM country;
--9. Pays ayant un mix énergétique équilibré 
SELECT country,
    coal_emissions,
    gas_emissions,
    oil_emissions,
    hydro_emissions,
    renewable_emissions,
    nuclear_emissions
FROM country
WHERE coal_emissions > 10
    AND gas_emissions > 10
    AND oil_emissions > 10
    AND renewable_emissions > 10;