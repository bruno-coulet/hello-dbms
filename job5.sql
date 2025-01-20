/* Créez une requête permettant d’afficher les pays dont la population
est supérieure à celle de "Russia"*/
select country
from world
where population > (select population
from world
where country = 'russia');


/* Créez une requête permettant d’afficher les pays d'Europe dont le PIB
par habitant est supérieur à celui d’ "Italy"*/
select *
from world
where `GDP
($percapita)` >
(select `GDP
($percapita)` from world where country = 'italy');

/* Créez une requête permettant d’afficher les pays dont la population
est supérieure à celle du Royaume-Uni mais inférieure à celle de
l'Allemagne*/
select *
from world
where population between ( select population
from world
where country = 'UnitedKingdom') and ( select population
from world
where country = 'Germany');
/* L'Allemagne (80 millions d'habitants) est le pays le plus peuplé
d'Europe L'Autriche (8,5 millions d'habitants) compte 11% de la
population allemande Créez une requête permettant d’afficher le nom
et la population de chaque pays d'Europe, en pourcentage de la
population de l'Allemagne*/

SELECT
    country ,
    population ,
    ROUND(population * 100 / (select population
    from world
    where country = "Germany") , 2 ) AS calcul_de_pourcentage
from world
where Region like "%EUROPE%";

/* Créez une requête permettant de trouver le plus grand pays de
chaque continent, en indiquant son continent, son nom et sa
superficie*/

WITH
    ranked_countries
    AS
    (
        SELECT
            region,
            country,
            `Area
    
    (sq.mi.)`,
        ROW_NUMBER
() OVER
(PARTITION BY region ORDER BY `Area
(sq.mi.)` DESC) AS rank_num
    FROM world
)
SELECT region, country, `Area
(sq.mi.)`
FROM ranked_countries
WHERE rank_num = 1;

/* Créez une requête permettant de trouver les continents où tous les
pays ont une population inférieure ou égale à 25 000 000*/

SELECT region
FROM world
GROUP BY region
HAVING MAX(population) < 25000000;