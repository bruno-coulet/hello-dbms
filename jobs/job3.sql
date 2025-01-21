--afficher toutes les colonnes de la table 
select *
from students 
/* ou */
DESCRIBE students 

--afficher les eleves de moins de 20 ans 
select *
from students
where age < 20

--le classement des meilleurs notes en ordre ascendant 
select *
from students
order by grade asc

--le classement des meilleurs notes en ordre descendant 
select *
from students
order by grade desc 