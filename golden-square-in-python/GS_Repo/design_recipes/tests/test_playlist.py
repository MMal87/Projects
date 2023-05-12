import pytest
from lib.playlist import *

# Given one track
# #add_track adds the track to our list
# musictracker = MusicTracker()
# musictracker.add_track("purple rain")
# musictracker = MusicTracker() # => adds "purple rain" to list

def test_music_tracker_one_track():
    musictracker = MusicTracker()
    result = musictracker.add_track("purple rain")
    assert result == None

# Given that multiple tracks are added
# #add_track will add multiple tracks to the list
def test_music_tracker_multiple_tracks():
    musictracker = MusicTracker()
    musictracker.add_track("purple rain")
    musictracker.add_track("wavin' flag")
    musictracker.add_track("when doves cry")
    assert musictracker.view_track() == ["purple rain", "wavin' flag", "when doves cry"]

# Given an empty list
# add_track raises an exception
# musictracker = MusicTracker()
# musictracker.add_track("") # raises an error with the message "No track added"

def test_empty_string():
    musictracker = MusicTracker()
    with pytest.raises(Exception) as e:
        musictracker.add_track("")
    error_message = str(e.value)
    assert error_message == "No track added"

# Given one track and return list
# #add_track adds the track to our list
# musictracker = MusicTracker()
# musictracker.add_track("purple rain")
# musictracker = MusicTracker() # => adds "purple rain" to list
def test_music_tracker_with_list_one_track():
    musictracker = MusicTracker()
    musictracker.add_track("purple rain")
    assert musictracker.view_track() == ["purple rain"]