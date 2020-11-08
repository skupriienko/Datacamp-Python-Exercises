-- Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
from professors
join  universities
ON  professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';
