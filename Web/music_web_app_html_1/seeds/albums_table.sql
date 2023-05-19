DROP TABLE IF EXISTS albums_table;
DROP SEQUENCE IF EXISTS albums_table_id_seq;

DROP TABLE IF EXISTS artists_table;
DROP SEQUENCE IF EXISTS artists_table_id_seq;

-- Then, we recreate them
CREATE TABLE albums_table (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

-- Then, we recreate them
CREATE TABLE artists_table (
    id SERIAL PRIMARY KEY,
    artist_name text,
    genre text
    
);

INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);





INSERT INTO artists_table (artist_name, genre) VALUES ('Pixies', 'rock');
INSERT INTO artists_table (artist_name, genre) VALUES ('Abba', 'pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Nina Simone', 'jazz');

