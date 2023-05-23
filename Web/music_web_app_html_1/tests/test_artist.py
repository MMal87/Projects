from lib.artist import Artist

def test_artist_variables():
    artist = Artist(1, 'Test name', "Test genre")
    assert artist.id == 1
    assert artist.artist_name == 'Test name'
    assert artist.genre == "Test genre"


def test_artists_are_equal():
    artist1 = Artist(1, 'Test name', "Test genre")
    artist2 = Artist(1, 'Test name', "Test genre")
    assert artist1 == artist2

def test_artists_format_nicely():
    album = Artist(1, "Test Artist", "Test Genre")
    assert str(album) == "Artist(1, Test Artist, Test Genre)"