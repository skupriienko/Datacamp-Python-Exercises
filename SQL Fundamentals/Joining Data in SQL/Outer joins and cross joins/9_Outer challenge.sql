-- Select fields
select c.name AS country,
    region,
    life_expectancy AS life_exp -- From countries (alias as c)
from countries as c -- Join to populations (alias as p)
    LEFT JOIN populations as p -- Match on country code
    ON c.code = p.country_code -- Focus on 2010
WHERE year = 2010 -- Order by life_exp
ORDER BY life_exp -- Limit to 5 records
LIMIT 5
