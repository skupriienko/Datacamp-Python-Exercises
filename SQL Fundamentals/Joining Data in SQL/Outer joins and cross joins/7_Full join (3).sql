-- 7. Select fields (with aliases)
SELECT c1.name AS country,
    region,
    l.name AS language,
    basic_unit,
    frac_unit -- 1. From countries (alias as c1)
FROM countries AS c1 -- 2. Join with languages (alias as l)
    FULL JOIN languages AS l -- 3. Match on code
    USING (code) -- 4. Join with currencies (alias as c2)
    FULL JOIN currencies AS c2 -- 5. Match on code
    USING (code) -- 6. Where region like Melanesia and Micronesia
WHERE region LIKE 'M%esia';
