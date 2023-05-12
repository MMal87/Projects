from lib.track import Track
from lib.music_library import MusicLibrary
import pytest
from unittest.mock import Mock

"""when title and artist are intialized, they return title and artist"""

def test_track_adding_title_and_artist():
    track = Track("Purple Rain", "Prince")
    assert track.title == "Purple Rain"
    assert track.artist == "Prince"

def test_matches_method_track_class():
    track = Track("Kiss", "Prince")
    assert track.matches("is") == True

"""Add nothing to track, return error"""

def test_empty_string_entry():
    with pytest.raises(Exception) as e:
        track = Track("", "")
    error_message = str(e.value)
    assert error_message == "Please enter something"



##MOCK TESTS FROM HERE###

""""add one track using mock, returns a list with 1 track"""

def test_returns_list_with_1_track_given_mock_track():
    music_library = MusicLibrary()
    track_1 = Mock()
    # track_1.add
    music_library.add(track_1)
    assert music_library.tracks == [track_1]


"""Given multiple tracks, it will return a list with the track names"""
def test_returns_list_with_multiple_tracks_given_mock_tracks():
    music_library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.tracks == [track_1, track_2, track_3]


## USING UNIT TESTING MODULE TO DO MOCKS##

"""Given multiple mock tracks, and a keyword with 1 match
#search returns a list with one track"""

def  test_search_with_one_true_result():
    music_library = MusicLibrary()
    track_1 = Mock()
    track_1.matches.return_value = False

    track_2 = Mock()
    track_2.matches.return_value = True

    track_3 = Mock() #does not need any parameters
    track_3.matches.return_value = False
    #here we have hardcoded the True statement into the program so the assert will pass the test
   
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    
    assert music_library.search("ack") == [track_2]

"""Given multiple mock tracks and a keyword with no matches
#search returns an empty list"""
def test_returns_empty_list_with_no_matches():
    music_library = MusicLibrary()
    track_1 = Mock()
    track_1.matches.return_value = False
    track_2 = Mock()
    track_1.matches.return_value = False
    track_3 = Mock()
    track_1.matches.return_value = False

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("ack") == []




"""Given multiple mock tracks and a keyword with multiple matches
#search returns a list with all matches"""
def test_returns_multiple_results_in_list():
    music_library = MusicLibrary()
   
    track_1 = Mock()
    track_1.matches.return_value = True
    
    track_2 = Mock()
    track_2.matches.return_value = False
    
    track_3 = Mock()
    track_3.matches.return_value = True

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("ack") == [track_1, track_3]