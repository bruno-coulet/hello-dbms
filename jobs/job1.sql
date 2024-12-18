-- Active: 1719231795972@@127.0.0.1@3306@world
SELECT Population 
FROM countries 
WHERE Country ="Germany "


SELECT Country, Population 
FROM countries 
WHERE Country IN ("Sweden ", "Norway ", "Denmark ")

SELECT Country, `Area (sq. mi.)` 
FROM countries 
WHERE `Area (sq. mi.)` > 200000 AND `Area (sq. mi.)` < 300000
ORDER BY `Area (sq. mi.)` DESC

