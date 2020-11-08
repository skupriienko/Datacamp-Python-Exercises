-- Select fields
select name -- From countries
from countries -- Set theory clause
INTERSECT
-- Select fields
select name -- From cities
from cities;
