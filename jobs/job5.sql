

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