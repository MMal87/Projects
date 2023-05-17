DROP TABLE IF EXISTS artists_table;
DROP SEQUENCE IF EXISTS artists_table_id_seq;

-- Then, we recreate them
CREATE TABLE artists_table (
    id SERIAL PRIMARY KEY,
    artist_name text,
    genre text
    
);

INSERT INTO artists_table (artist_name, genre) VALUES ('Pixies', 'rock');
INSERT INTO artists_table (artist_name, genre) VALUES ('Abba', 'pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists_table (artist_name, genre) VALUES ('Nina Simone', 'jazz');
