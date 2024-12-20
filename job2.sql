use world;

/*pays commençant par B */
select Country
from world
where country LIKE 'B%';

/*pays commençant pas Al*/
select Country
from world
where country LIKE 'Al%';

/*pays finissant pas Y */
select Country
from world
where country LIKE '%y';

/*pays finissant pas land*/
select Country
from world
where country LIKE '%land';

/*pays contenant la lettre w */
select Country
from world
where country LIKE '%w%';

/*pays contenant la lettre oo ou ee*/
select Country
from world
where country LIKE '%oo%' or country LIKE '%ee%';

/*pays contenant 3 fois la lettre a */
select Country
from world
where country LIKE '%a%a%a%';

/*pays ayant comme deuxieme lettre le r */
select *
from world
where country LIKE '_r%';