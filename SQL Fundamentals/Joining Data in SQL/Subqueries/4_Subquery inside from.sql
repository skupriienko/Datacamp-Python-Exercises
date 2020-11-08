-- Select fields (with aliases)
select code,
    count(name) as lang_num -- From languages
From languages -- Group by code
group by code;

SELECT local_name,
    subquery.lang_num
FROM countries,
    (
        SELECT code,
            COUNT(*) AS lang_num
        FROM languages
        GROUP BY code
    ) AS subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;
