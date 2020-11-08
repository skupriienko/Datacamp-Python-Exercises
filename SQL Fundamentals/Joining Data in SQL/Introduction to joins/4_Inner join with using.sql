-- 4. Select fields
select c.name as country, continent, l.name AS language, official
  -- 1. From countries (alias as c)
  from countries as c
  -- 2. Join to languages (as l)
  INNER JOIN languages as l
    -- 3. Match using code
    USING (code)
