-- Active: 1719231795972@@127.0.0.1@3306@world

--Créez une requête permettant de trouver les noms de pays commençant par la lettre B.
SELECT Country 
FROM countries
WHERE Country LIKE "B%"

--Créez une requête permettant de trouver les noms de payscommençant par “Al”.
SELECT Country 
FROM countries
WHERE Country LIKE "AL%"

--Créez une requête permettant de trouver les noms de pays finissant par la lettre y.
SELECT Country 
FROM countries
WHERE Country LIKE "%y "

--Créez une requête permettant de trouver les noms de pays finissant par “land”.
SELECT Country 
FROM countries
WHERE Country LIKE "%land "

--Créez une requête permettant de trouver les noms de pays contenant la lettre “w”.
SELECT Country 
FROM countries
WHERE Country LIKE "%w%"

--Créez une requête permettant de trouver les noms de pays contenant “oo” ou “ee”.
SELECT Country 
FROM countries
WHERE Country REGEXP 'oo|ee'

--Créez une requête permettant de trouver les noms de pays contenant au moins trois fois la lettre a.
SELECT Country
FROM countries
WHERE Country REGEXP '(.*a.*){3}'

--Créez une requête permettant de trouver les noms de pays ayant la lettre r comme seconde lettre.
SELECT Country
FROM countries
WHERE Country REGEXP '(^.r)'
