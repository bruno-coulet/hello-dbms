/*donnée de l'allemagne*/
select *
from world
where name = 'Germany';

/*données de suede , norvege et danemark*/
select *
from world
where name in ('Sweden','Norway','Denmark');

/*pays dont la superficie est entre 200k et 300k*/

select *
from world
where `Area
(sq. mi.)` between 200000 and 300000;