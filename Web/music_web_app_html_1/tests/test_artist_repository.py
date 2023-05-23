from lib.artist_repository import *
from lib.artist import *

def test_list_all_artists(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    artist_repo = ArtistRepository(db_connection)
    result = artist_repo.all()
    assert result == [
        Artist(1, "Pixies", "Rock"), 
        Artist(2,"ABBA", "Pop"),
        Artist(3,"Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz")]
    


def test_create_method(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    artist_repo = ArtistRepository(db_connection)
    artist = Artist(5, "Test Name", "Test Genre")
    artist_repo.create(artist)
    assert artist_repo.all() == [Artist(1, "Pixies", "Rock"), 
        Artist(2,"ABBA", "Pop"),
        Artist(3,"Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Test Name", "Test Genre")]
    
