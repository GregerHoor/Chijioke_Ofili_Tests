CREATE TABLE IF NOT EXISTS shirt_color (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    frequency INTEGER
);

ALTER TABLE shirt_color
ADD CONSTRAINT unique_shirt_name UNIQUE (name);