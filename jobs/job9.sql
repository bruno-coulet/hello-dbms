/*Les pays qui ont un taux de mortalité plus élevé que leur taux de natalité*/
select *
from world
where birthrate < deathrate


/*Requete pour voir si il y a plus de naissance ou de mort dans le monde*/
select sum(Birthrate) , sum(deathrate)
from world;


/*Les payys avec le plus d'habitants par M²*/
select *
from world
order by `Pop.Density-persq.mi.` desc;


/*Les pays avec le plus gros pib par habitant et par continent */
WITH
    ranked_countries
AS
(
        SELECT
    region,
    country,
    `GDP
-$percapita`,
        ROW_NUMBER
() OVER
(PARTITION BY region ORDER BY `GDP-$percapita` DESC) AS rank_num
    FROM world
)
SELECT region, country, `GDP
-$percapita`
FROM ranked_countries
WHERE rank_num = 1;

/*La chine etant le pays le plus peuplé , voici le pourcentage d'habitant des pays par rapport a la chine */
SELECT
    country ,
    population ,
    ROUND(population * 100 / 
    (select population
    from world
    where country = "China") , 2 ) AS calcul_de_pourcentage
from world;

/*pays qui ont le plus de mortalité infantile */

select *
from world
order by `
Infantmortality-per1000births` desc;