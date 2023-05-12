from lib.album import Album 

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            album = Album(row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [album_id]) #doing this instead of fstring protects you from someone adding their own sql command here and potentially making your data insecure
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"])

