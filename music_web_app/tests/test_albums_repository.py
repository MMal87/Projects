from lib.albums import Albums
from lib.albums_repository import AlbumRepository
def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    result = album_repo.all()
    assert result == [Albums('Doolittle', 1989, 1)]
