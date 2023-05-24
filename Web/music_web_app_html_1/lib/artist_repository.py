from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from artists_table')
        artists = []
        for row in rows:
            artists.append(Artist(row["id"], row["artist_name"], row["genre"]))   
        return artists
    
    def create(self, artist):
        rows = self._connection.execute('INSERT into artists_table (artist_name, genre) VALUES (%s, %s) RETURNING id', [artist.artist_name, artist.genre])
        
        artist.id = rows[0]['id']
        print("HEY", artist.id)
        return None
    
     # Find a single artist by their id
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists_table WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["artist_name"], row["genre"])

    def find_name(self, artist_name):
        
        rows = self._connection.execute(
            'SELECT * from artists_table WHERE id = %s', [artist_name])
        row = rows[0]
        return Artist(row["id"], row["artist_name"], row["genre"])

    