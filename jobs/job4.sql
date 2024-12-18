-- Active: 1719231795972@@127.0.0.1@3306@nobels

SELECT winner, subject
FROM nobels
WHERE yr = 1986

SELECT winner
FROM nobels
WHERE yr = 1967 AND subject = 'Literature'

SELECT yr, subject
FROM nobels
WHERE winner = 'Albert Einstein'


SELECT *
FROM nobels
WHERE yr > 1979 AND yr < 1990

SELECT *
FROM nobels
WHERE subject = "Chemistry"

COUNT row
FROM nobels
WHERE subject = "Chemistry"