SELECT distinct languages.name AS language
FROM languages
    INNER JOIN countries ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;
