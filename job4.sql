/*Créez une requête permettant d’afficher les prix nobels de 1986.*/
select *
from nobel
where yr = 1986

/*Créez une requête permettant d’afficher les prix nobels de littérature
de 1967.*/

select *
from nobel
where yr = 1967
    and subject = 'literature'

/*Créez une requête permettant d’afficher l’année et le sujet du prix
nobel d’Albert Einstein.*/

select subject , yr
from nobel
where winner = "Albert Einstein"

/*Créez une requête permettant d’afficher les détails (année, sujet,
lauréat) des lauréats du prix de Littérature de 1980 à 1989 inclus.*/
select *
from nobel
where yr between 1980 and 1989
    and subject = "literature"

/*Créez une requête permettant d’afficher les détails des lauréats du
prix de Mathématiques. Combien y en a-t-il ?*/
select *
from nobel
where subject = 'mathematic'