-- Select fields
select code,
    year -- From economies
from economies -- Set theory clause
intersect
-- Select fields
select country_code,
    year -- From populations
from populations -- Order by code and year
order by code,
    year;
