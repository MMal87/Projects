from lib.albums import Albums

class AlbumsRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums_table')
        albums = []
        for row in rows:
            album = Albums(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums

    def create(self, album):
        self._connection.execute('INSERT INTO albums_table (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT albums_table.title, albums_table.release_year, artists_table.artist_name FROM albums_table JOIN artists_table ON albums_table.artist_id = artists_table.id WHERE albums_table.id = %s', [album_id])
        row = rows[0] 
        return Albums(None, row['title'], row['release_year'], row['artist_name'])
  
    