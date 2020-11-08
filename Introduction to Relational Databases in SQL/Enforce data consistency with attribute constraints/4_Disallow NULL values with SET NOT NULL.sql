-- Disallow NULL values in lastname
ALTER TABLE professors
ALTER COLUMN lastname
SET NOT NULL;
