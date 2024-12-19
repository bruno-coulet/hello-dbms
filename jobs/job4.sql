-- Active: 1719231795972@@127.0.0.1@3306@world


-- 1. Créez une requête permettant d’afficher les prix nobels de 1986.
SELECT winner, subject
FROM nobels
WHERE yr = 1986


-- 2. Créez une requête permettant d’afficher les prix nobels de littérature de 1967.
SELECT winner
FROM nobels
WHERE yr = 1967 AND subject = 'Literature'

--  3. Créez une requête permettant d’afficher l’année et le sujet du prix nobel d’Albert Einstein.
SELECT yr, subject
FROM nobels
WHERE winner = 'Albert Einstein'

-- 4. Créez une requête permettant d’afficher les détails (année, sujet,lauréat) des lauréats du prix de Littérature de 1980 à 1989 inclus.
SELECT *
FROM nobels
WHERE yr > 1979 AND yr < 1990


-- 5. Créez une requête permettant d’afficher les détails des lauréats du prix de Chimie.
    -- Avec une fonction de fenêtre
SELECT *, 
       COUNT(*) OVER (PARTITION BY subject) AS laureates_count
FROM nobels
WHERE subject = 'Chemistry';


    -- Avec une sous requête	
SELECT *, 
       (SELECT COUNT(*) 
        FROM nobels 
        WHERE subject = 'Chemistry') AS laureates_count
FROM nobels
WHERE subject = 'Chemistry';
