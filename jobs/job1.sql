-- Active: 1719231795972@@127.0.0.1@3306@world

--Modifiez la requête ci-dessus afin d’afficher la population de “Germany”.
SELECT Population 
FROM countries 
WHERE Country ="Germany"

--Modifiez la requête ci-dessus afin d’afficher le nom et la population des pays “Sweden”, “Norway” et “Denmark”.
SELECT Country, Population 
FROM countries 
WHERE Country IN ("Sweden", "Norway", "Denmark")


--Créez une requête permettant d’afficher les pays dont la superficie est supérieure à 200 000 mais inférieure à 300 000.
SELECT Country, `Area (sq. mi.)` 
FROM countries 
WHERE `Area (sq. mi.)` > 200000 AND `Area (sq. mi.)` < 300000
ORDER BY `Area (sq. mi.)` DESC

