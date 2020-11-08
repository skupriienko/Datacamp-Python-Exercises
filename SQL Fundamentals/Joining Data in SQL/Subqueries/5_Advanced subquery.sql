-- Select fields
select name,
    continent,
    inflation_rate -- From countries
From countries -- Join to economies
    INNER JOIN economies -- Match on code
    USING (code) -- Where year is 2015
where year = 2015;
-- Select the maximum inflation rate as max_inf
select MAX(inflation_rate) AS max_inf -- Subquery using FROM (alias as subquery)
FROM (
        select name,
            continent,
            inflation_rate
        from countries
            INNER JOIN economies USING (code)
        where year = 2015
    ) AS subquery -- Group by continent
group by continent;


-- Select fields
SELECT name,
    continent,
    inflation_rate -- From countries
FROM countries -- Join to economies
    INNER JOIN economies -- Match on code
    ON countries.code = economies.code -- Where year is 2015
WHERE year = 2015 -- And inflation rate in subquery (alias as subquery)
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
                SELECT name,
                    continent,
                    inflation_rate
                FROM countries
                    INNER JOIN economies ON countries.code = economies.code
                WHERE year = 2015
            ) AS subquery -- Group by continent
        GROUP BY continent
    );
