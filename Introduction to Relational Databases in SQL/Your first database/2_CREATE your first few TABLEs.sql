-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT *
FROM professors

-- Create a table for the universities entity type
create table universities (
university_shortname text,
university text,
university_city text);


-- Print the contents of this table
SELECT *
FROM universities

-- Add the university_shortname column
alter table professors
add column university_shortname text;

-- Print the contents of this table
SELECT *
FROM professors
