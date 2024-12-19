-- Active: 1719231795972@@127.0.0.1@3306@world

-- Afficher la population totale du monde.
select SUM(Population)
from countries;

-- afficher la population totale de chacun des continents.
-- ajouter une colonne Continent
ALTER TABLE countries
ADD Continent VARCHAR(255);

-- remplir la colonne continent
UPDATE countries
SET Continent = CASE 
    WHEN Region LIKE 'ASIA%' THEN 'Asia'
    WHEN Region LIKE 'BALTICS' THEN 'Europe'
    WHEN Region LIKE 'C.W. OF IND. STATES' THEN 'Asia'
    WHEN Region LIKE 'EASTERN EUROPE' THEN 'Europe'
    WHEN Region LIKE 'LATIN AMER. & CARIB' THEN 'America'
    WHEN Region LIKE 'NEAR EAST' THEN 'Asia'
    WHEN Region LIKE 'NORTHERN AFRICA' THEN 'Africa'
    WHEN Region LIKE 'NORTHERN AMERICA' THEN 'America'
    WHEN Region LIKE 'OCEANIA' THEN 'Oceania'
    WHEN Region LIKE 'WESTERN EUROPE' THEN 'Europe'
    WHEN Region LIKE 'SUB-SAHARAN AFRICA' THEN 'Africa'
END;

-- compter les population de chaque continent
SELECT Continent, SUM(Population) 
FROM countries
GROUP BY Continent;


-- Afficher le PIB total du continent de chacun des continents.
SELECT Continent, SUM(`GDP ($ per capita)`)
FROM countries
GROUP BY Continent;


-- Afficher le PIB total du continent africain
SELECT Continent, SUM(`GDP ($ per capita)`)
FROM countries
WHERE Continent = 'Africa'
GROUP BY Continent;


-- Afficher le nombre de pays ayant une superficie supérieure ou égale à 1 000 000m2.
SELECT COUNT(Country)
FROM countries
WHERE `Area (sq. mi.)`> 1000000;

show columns from countries;