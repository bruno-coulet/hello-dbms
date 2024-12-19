
--Créez une requete permettant d'afficher la population totale mondiale 
SELECT SUM(population) AS 'Population mondiale'
FROM countries

--Créez une requête permettant d'afficher la population totale de chaque continent
SELECT Region, SUM(population) AS 'Population totale'
FROM countries
GROUP BY Region 

--Créez une requête permettant d’afficher le PIB total du continent de chacun des continents.
SELECT Region, SUM(`GDP ($ per capita)` * population) AS 'PIB total'
FROM countries
GROUP BY Region

--Créez une requête permettant d’afficher le PIB total du continent africain.
SELECT SUM(`GDP ($ per capita)` * population) AS 'PIB total'
FROM countries
WHERE Region LIKE '%Africa';

--Créez une requête permettant d’afficher le nombre de pays ayant une superficie supérieure ou égale à 1 000 000m2.
SELECT COUNT(Country) AS 'Nombre de pays'
FROM countries
WHERE `Area (sq. mi.)` >= 1000000

--Créez une requête permettant d’afficher la population totale des pays suivants : Estonia, Latvia, Lithuania.
SELECT SUM(population) AS 'Population totale'
FROM countries
WHERE Country IN ('Estonia', 'Latvia', 'Lithuania')

--Créez une requête permettant d’afficher le nombre de pays de chaque continent.
SELECT Region, COUNT(Country) AS 'Nombre de pays'
FROM countries
GROUP BY Region
ORDER BY COUNT(Country) DESC

--Créez une requête permettant d’afficher les continents ayant une population totale d’au moins 100 millions d’individus.
SELECT Region, SUM(population) AS 'Population totale'
FROM countries
GROUP BY Region
HAVING SUM(population) >= 100000000
ORDER BY SUM(population) DESC