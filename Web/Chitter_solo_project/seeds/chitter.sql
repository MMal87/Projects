DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  password text,
  email text
);

-- Then the table with the foreign key second.
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  created_at text,
  user_id int,
  constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
 
  
);

INSERT INTO users (name, password, email) VALUES
  ('John Doe', 'password123', 'johndoe@me.com'),
  ('Jane Smith', 'securepass', 'janesmith@me.com'),
  ('Michael Johnson', 'pass1234', 'michaeljohnson@me.com');


INSERT INTO peeps (title, content, created_at, user_id) VALUES
 
  ('Hello world', 'My first peep!','15:03:31', 1),
  ('Exciting news', 'Just launched my new project!', '15:23:31', 2),
  ('Thoughts for the day', 'Life is a journey, not a destination.', '20:16:31', 1),
  ('Late-night coding', 'Working on a new feature...', '22:45:31', 3),
  ('Weekend vibes', 'Relaxing and enjoying some downtime.', '12:05:31', 2);