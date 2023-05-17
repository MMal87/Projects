from lib.artist_repository import *
from lib.artist import *

def list_all_artists(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    artist_repo = ArtistRepository(db_connection)
    result = artist_repo.all()
    assert result == "Pixies, Abba, Taylor Swift, Nina Simone"

def test_create_method(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    artist_repo = ArtistRepository(db_connection)
    artist = Artist(5, "Test Name", "Test Genre")
    artist_repo.create(artist)

    assert artist_repo.all() == ["Pixies", "Abba", "Taylor Swift", "Nina Simone", "Test Name"]