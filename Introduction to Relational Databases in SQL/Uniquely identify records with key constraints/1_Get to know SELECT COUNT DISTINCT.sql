-- Count the number of rows in universities
SELECT count(*)
FROM universities;

-- Count the number of distinct values in the university_city column
SELECT count(distinct(university_city))
FROM universities;

-- Try out different combinations
select COUNT(distinct(firstname, lastname))
FROM professors;
