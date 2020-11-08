SELECT
    country_code,
    size,
    -- 1. First case
    CASE
        WHEN size > 50000000 THEN 'large' -- 2. Second case
        WHEN size > 1000000 THEN 'medium' -- 3. Else clause + end
        ELSE 'small'
    END -- 4. Alias name (popsize_group)
    AS popsize_group -- 5. From table
FROM
    populations -- 6. Focus on 2015
WHERE
    year = 2015;

SELECT
    country_code,
    size,
    CASE
        WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small'
    END AS popsize_group -- 1. Into table
    INTO pop_plus
FROM
    populations
WHERE
    year = 2015;

-- 2. Select all columns of pop_plus
select
    *
from
    pop_plus

SELECT
    country_code,
    size,
    CASE
        WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small'
    END AS popsize_group INTO pop_plus
FROM
    populations
WHERE
    year = 2015;

-- 5. Select fields
select
    name,
    continent,
    geosize_group,
    popsize_group -- 1. From countries_plus (alias as c)
from
    countries_plus as c -- 2. Join to pop_plus (alias as p)
    INNER JOIN pop_plus as p -- 3. Match on country code
    ON c.code = p.country_code -- 4. Order the table
ORDER BY
    geosize_group;
