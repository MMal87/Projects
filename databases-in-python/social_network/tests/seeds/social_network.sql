-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INTEGER,
    user_id INTEGER
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('John Doe', 'john.doe@example.com');
INSERT INTO users (username, email) VALUES ('Jane Doe', 'jane.doe@example.com');


INSERT INTO posts (title, content, views, user_id) VALUES ('My first post', 'This is my post', 10, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('My second post', 'This is my second post', 30, 2);
