from lib.albums import Albums
from lib.albums_repository import AlbumsRepository


def test_list_all_albums(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    album_repo = AlbumsRepository(db_connection)
    result = album_repo.all()
    assert result == [Albums(1, 'Doolittle', 1989, 1), Albums(2, 'Surfer Rosa', 1988, 1),  Albums(3, 'Waterloo', 1974, 2)
, Albums(4, 'Super Trouper', 1980, 2), Albums(5, 'Bossanova', 1990, 1), Albums(6, 'Lover', 2019, 3), Albums(7, 'Folklore', 2020, 3), Albums(8, 'I Put a Spell on You', 1965, 4), Albums(9, 'Baltimore', 1978, 4), Albums(10, 'Here Comes the Sun', 1971, 4), Albums(11, 'Fodder on My Wings', 1982, 4), Albums(12, 'Ring Ring', 1973, 2)]





# def test_find_method(db_connection):
#     repository = AlbumsRepository(db_connection)
#     assert repository.find(1)== Albums(1, 'Doolittle', 1989, 1)
    



# def test_create_method(db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     album_repo = AlbumsRepository(db_connection)
#     album = Albums(2, "Test Title", 1000, 1)
#     album_repo.create(album)
#     assert album.id == 13
#     assert album_repo.all() == [Albums(1, 'Doolittle', 1989, 1), Albums(2, 'Surfer Rosa', 1988, 1),  Albums(3, 'Waterloo', 1974, 2)
# , Albums(4, 'Super Trouper', 1980, 2), Albums(5, 'Bossanova', 1990, 1), Albums(6, 'Lover', 2019, 3), Albums(7, 'Folklore', 2020, 3), Albums(8, 'I Put a Spell on You', 1965, 4), Albums(9, 'Baltimore', 1978, 4), Albums(10, 'Here Comes the Sun', 1971, 4), Albums(11, 'Fodder on My Wings', 1982, 4), Albums(12, 'Ring Ring', 1973, 2), Albums(13, "Test Title", 1000, 1)]