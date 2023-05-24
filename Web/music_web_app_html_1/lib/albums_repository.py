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
        rows = self._connection.execute('INSERT INTO albums_table (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [album.title, album.release_year, album.artist_id])
        
        album.id = rows[0]['id']
        
        return None
        
    
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * FROM albums_table WHERE id = %s', [album_id])        
        row = rows[0]
       
        return Albums(row['id'], row['title'], row['release_year'], row['artist_id'])
    
    
  
    