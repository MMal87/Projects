from lib.albums import Albums
from lib.albums_repository import AlbumsRepository


def test_list_all_albums(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    album_repo = AlbumsRepository(db_connection)
    result = album_repo.all()
    assert result == [Albums(1, 'Doolittle', 1988, 1)]

def test_create_method(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    album_repo = AlbumsRepository(db_connection)
    album = Albums(2, "Test Title", 1000, 1)
    album_repo.create(album)
    assert album_repo.all() == [Albums(1, 'Doolittle', 1988, 1), Albums(2, "Test Title", 1000, 1)]
