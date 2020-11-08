/*
 SELECT code
 FROM countries
 WHERE region = 'Middle East';
 */
-- Select field
SELECT DISTINCT name -- From languages
FROM languages -- Order by name
ORDER BY name;

-- Select distinct fields
SELECT DISTINCT name -- From languages
FROM languages -- Where in statement
WHERE code IN -- Subquery
    (
        SELECT code
        FROM countries
        WHERE region = 'Middle East'
    ) -- Order by name
ORDER BY name;
