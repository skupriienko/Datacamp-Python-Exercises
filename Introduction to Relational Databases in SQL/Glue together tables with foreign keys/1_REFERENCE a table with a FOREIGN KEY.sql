-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

-- Add a foreign key on professors referencing universities
alter TABLE professors
add constraint professors_fkey FOREIGN KEY (university_id) REFERENCES universities (id);
