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
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums_table (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);






INSERT INTO artists_table (artist_name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists_table (artist_name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Nina Simone', 'Jazz');

