-- 2. Select fields
select name,
    country_code,
    urbanarea_pop -- 3. From cities
From cities -- 4. Where city name in the field of capital cities
where name IN -- 1. Subquery
    (
        select capital
        from countries
    )
ORDER BY urbanarea_pop DESC;
