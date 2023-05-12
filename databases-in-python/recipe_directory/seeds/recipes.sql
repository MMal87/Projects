-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255),
    cooking_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Daal', 90, 1);
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Mexican Bean Stew', 180, 3);
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Carrot Cake', 180, 2);
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Chicken Milanese', 60, 2);
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Leek and Potato Soup', 180, 2);
INSERT INTO recipes(recipe_name, cooking_time, rating) VALUES ('Creme Brulee', 55, 5);

