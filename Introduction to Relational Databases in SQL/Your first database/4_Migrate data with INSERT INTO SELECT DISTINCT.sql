-- Insert unique affiliations into the new table
insert into affiliations
select distinct firstname, lastname, function, organization
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT *
FROM affiliations;
