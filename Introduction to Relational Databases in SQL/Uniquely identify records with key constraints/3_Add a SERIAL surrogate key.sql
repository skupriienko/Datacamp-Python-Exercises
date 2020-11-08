-- Add the new column to the table
-- Add the new column to the table
ALTER TABLE professors
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors
ADD CONSTRAINT professors_pkey primary key (id);

-- Have a look at the first 10 rows of professors
select *
from professors
limit 10;
