-- Select fields from 2010 table
select * -- From 2010 table
from economies2010 -- Set theory clause
UNION
-- Select fields from 2015 table
select * -- From 2015 table
from economies2015 -- Order by code and year
ORDER BY code,
    year;
