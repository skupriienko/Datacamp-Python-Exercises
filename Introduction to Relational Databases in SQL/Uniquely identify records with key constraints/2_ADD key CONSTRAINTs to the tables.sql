-- Rename the organization column to id
alter table organizations
rename column organization TO id;

-- Make id a primary key
ALTER TABLE organizations
add constraint organization_pk primary KEY (id);

-- Rename the university_shortname column to id
alter table universities
rename column university_shortname to id;

-- Make id a primary key
alter table universities
add constraint university_pk primary key (id);
