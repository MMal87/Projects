CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text
  password text
);

-- Then the table with the foreign key second.
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (name, password) VALUES
  ('John Doe', 'password123'),
  ('Jane Smith', 'securepass'),
  ('Michael Johnson', 'pass1234');


INSERT INTO peeps (title, content, user_id) VALUES
  ('Hello world', 'My first peep!', 1),
  ('Exciting news', 'Just launched my new project!', 2),
  ('Thoughts for the day', 'Life is a journey, not a destination.', 1),
  ('Late-night coding', 'Working on a new feature...', 3),
  ('Weekend vibes', 'Relaxing and enjoying some downtime.', 2);