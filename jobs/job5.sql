

--Créez une requête permettant d’afficher les pays dont la population est supérieure à celle de "Russia".
SELECT Country
FROM countries
WHERE population > (
    SELECT population
    FROM countries
    WHERE Country = 'Russia'
)

--Créez une requête permettant d’afficher les pays d'Europe dont le PIB par habitant est supérieur à celui d’ "Italy".
SELECT Country, `GDP ($ per capita)`
From countries
WHERE Region LIKE '%EUROPE%' AND `GDP ($ per capita)` > (
    SELECT `GDP ($ per capita)`
    FROM countries
    WHERE Country = 'Italy'
)
ORDER BY `GDP ($ per capita)` DESC

--Créez une requête permettant d’afficher les pays dont la population est supérieure à celle du Royaume-Uni mais inférieure à celle de l'Allemagne.
SELECT Country, population
FROM countries
WHERE population > (
    SELECT population
    FROM countries
    WHERE Country = 'United Kingdom'
)
AND population < (
    SELECT population
    FROM countries
    WHERE Country = 'Germany'
)
ORDER BY population DESC

--Crééz une requête permettant d'afficher ke nom et la population de chaques pays d'Europe, en pourcentage de la population de l'Allemagne.
SELECT Country, population, (population / (
    SELECT population
    FROM countries
    WHERE Country = 'Germany'
)) * 100 AS 'Population (%)'
FROM countries
WHERE Region LIKE '%EUROPE%'
ORDER BY population DESC

--Créer une requête permettant de trouver le plus grand pays de chaque continent, en indiquant son continent, son nom et sa superficie.
SELECT Region, Country, `Area (sq. mi.)`
FROM countries c1
WHERE `Area (sq. mi.)` = (
    SELECT MAX(`Area (sq. mi.)`)
    FROM countries c2
    WHERE c1.Region = c2.Region
)


--Crééz une requête permettant de trouver les continents où tous les pays ont une population inférieure ou égale à 25 000 000.
SELECT Region
FROM countries
GROUP BY Region
HAVING COUNT(CASE WHEN population > 25000000 THEN 1 END) = 0;
