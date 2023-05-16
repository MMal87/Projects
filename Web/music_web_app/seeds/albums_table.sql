DROP TABLE IF EXISTS albums_table;
DROP SEQUENCE IF EXISTS albums_table_id_seq;

-- Then, we recreate them
CREATE TABLE albums_table (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Doolittle', 1988, 1)
