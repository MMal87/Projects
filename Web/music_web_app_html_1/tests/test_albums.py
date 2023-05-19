from lib.albums import Albums

def test_album_variables():
    album = Albums(1, 'Test title', 1000, 1)
    assert album.id == 1
    assert album.title == 'Test title'
    assert album.release_year == 1000
    assert album.artist_id == 1

def test_albums_are_equal():
    album1 = Albums(1, "Test title", 1000, 1)
    album2 = Albums(1, "Test title", 1000, 1)
    assert album1 == album2

def test_artists_format_nicely():
    album = Albums(1, "Test Title", 1000, 1)
    assert str(album) == "Album(1, Test Title, 1000, 1)"