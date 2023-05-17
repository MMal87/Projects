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
