-- Active: 1719231795972@@127.0.0.1@3306@students

--Créez une requête permettant d’afficher toutes les colonnes de la table students.
DESCRIBE students

--Créez une requête permettant de filtrer la table et d’afficher les élèves âgés de strictement plus de 20 ans.
SELECT *
FROM students
WHERE age > 20

--Créez une requête permettant de faire un classement des élèves selon leur note dans un ordre croissant, puis dans un ordre décroissant.
SELECT *
FROM students
ORDER BY 
    CASE 
        WHEN grade = 'A+' THEN 1
        WHEN grade = 'A' THEN 2
        WHEN grade = 'B+' THEN 3
        WHEN grade = 'B' THEN 4
        WHEN grade = 'C+' THEN 5
        WHEN grade = 'C' THEN 6
END ASC

SELECT *
FROM students
ORDER BY 
    CASE 
        WHEN grade = 'A+' THEN 1
        WHEN grade = 'A' THEN 2
        WHEN grade = 'B+' THEN 3
        WHEN grade = 'B' THEN 4
        WHEN grade = 'C+' THEN 5
        WHEN grade = 'C' THEN 6
END DESC
