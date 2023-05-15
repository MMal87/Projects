DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    author_name VARCHAR(255),
    content VARCHAR(255),
    post_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content) VALUES ('How to use Git', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('Fun classes', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('Using a REPL', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('My weekend in Edinburgh', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('The best chocolate cake EVER', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('A foodie week in Spain', 'Here are my contents.');
INSERT INTO posts (title, content) VALUES ('SQL basics', 'Here are my contents.');


INSERT INTO comments (author_name, content, post_id) VALUES ('Daniel Harris', 'I have a question.', 6);
INSERT INTO comments (author_name, content, post_id) VALUES ('Jane Smith', 'I completely agree.', 1);
INSERT INTO comments (author_name, content, post_id) VALUES ('Emily Davis', 'Can you elaborate on that point?', 3);
INSERT INTO comments (author_name, content, post_id) VALUES ('Laura Anderson', 'I have a different opinion.', 4);
INSERT INTO comments (author_name, content, post_id) VALUES ('Michael Wilson', 'Interesting perspective.', 2);
INSERT INTO comments (author_name, content, post_id) VALUES ('David Roberts', 'Thought-provoking article.', 5);