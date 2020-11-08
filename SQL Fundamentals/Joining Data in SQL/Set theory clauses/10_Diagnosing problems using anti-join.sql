-- Select statement
select count(*) -- From countries
From countries -- Where continent is Oceania
where continent = 'Oceania';
-- 5. Select fields (with aliases)
select c1.code,
    name,
    basic_unit AS currency -- 1. From countries (alias as c1)
From countries as c1 -- 2. Join with currencies (alias as c2)
    inner join currencies as c2 -- 3. Match on code
    ON c1.code = c2.code -- 4. Where continent is Oceania
where continent = 'Oceania';
-- 3. Select fields
select code,
    name -- 4. From Countries
From countries -- 5. Where continent is Oceania
where continent = 'Oceania' -- 1. And code not in
    AND code NOT IN -- 2. Subquery
    (
        SELECT code
        FROM currencies
    );
