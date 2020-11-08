-- Select fields
SELECT DISTINCT name,
    total_investment,
    imports -- From table (with alias)
FROM countries AS c -- Join with table (with alias)
    LEFT JOIN economies AS e -- Match on code
    ON (
        c.code = e.code -- and code in Subquery
        AND c.code IN (
            SELECT l.code
            FROM languages AS l
            WHERE official = 'true'
        )
    ) -- Where region and year are correct
WHERE region = 'Central America'
    AND year = 2015 -- Order by field
ORDER BY name;
