-- 4. Select fields with aliases
select
    p1.country_code,
    p1.size as size2010,
    p2.size as size2015 -- 1. From populations (alias as p1)
FROM
    populations as p1 -- 2. Join to itself (alias as p2)
    INNER JOIN populations as p2 -- 3. Match on country code
    ON p1.country_code = p2.country_code

-- 5. Select fields with aliases
SELECT
    p1.country_code,
    p1.size AS size2010,
    p2.size AS size2015 -- 1. From populations (alias as p1)
FROM
    populations as p1 -- 2. Join to itself (alias as p2)
    INNER JOIN populations as p2 -- 3. Match on country code
    ON p1.country_code = p2.country_code -- 4. and year (with calculation)
    AND p1.year = p2.year - 5


SELECT
    p1.country_code,
    p1.size AS size2010,
    p2.size AS size2015,
    -- 1. calculate growth_perc
    ((p2.size - p1.size) / p1.size * 100.0) AS growth_perc -- 2. From populations (alias as p1)
FROM
    populations AS p1 -- 3. Join to itself (alias as p2)
    INNER JOIN populations AS p2 -- 4. Match on country code
    ON p1.country_code = p2.country_code -- 5. and year (with calculation)
    AND p1.year = p2.year - 5;
