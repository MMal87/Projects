
from lib.album import *

"""When adding variables title, release_year and artist_id, they are intialized."""

def test_album_variables():
    album = Album('Test title', 'Test release_year', 'Test artist_id')
    assert album.title == 'Test title'
    assert album.release_year == 'Test release_year'
    assert album.artist_id == 'Test artist_id'

"""We can format albums to strings nicely"""

def test_artists_format_nicely():
    album = Album(1, "Test Title", "Test release_year")
    assert str(album) == "Album(1, Test Title, Test release_year)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Artist", "Test Genre")
    album2 = Album(1, "Test Artist", "Test Genre")
    assert album1 == album2

