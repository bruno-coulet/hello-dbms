show databases;
use world;
show tables;

describe world;




/*donnée de l'allemagne*/
select *
from world
where Country = 'Germany';

/*données de suede , norvege et danemark*/
select *
from world
where Country in ('Sweden','Norway','Denmark');

/*pays dont la superficie est entre 200k et 300k*/
select Country, `Area (sq. mi.)`
from world
where `Area (sq. mi.)` between 200000 and 300000;