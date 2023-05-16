from lib.albums import Albums

class AlbumsRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            album = Albums(row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
