from lib.music_library import MusicLibrary
from lib.track import Track

"""given multiple titles and artist names, they will be initialized by the add method"""

def test_library_add_method():
    music_library = MusicLibrary()
    track_1 = Track("Purple Rain", "Prince")
    track_2 = Track("Kiss", "Prince")
    track_3 = Track("When Doves Cry", "Prince")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.tracks == [track_1, track_2, track_3]


def test_library_add_method():
    music_library = MusicLibrary()
    track_1 = Track("Purple Rain", "Prince")
    track_2 = Track("Kiss", "Prince")
    track_3 = Track("When Doves Cry", "Prince")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("is") == [track_2]

def test_multiple_tracks_in_search():
    music_library = MusicLibrary()
    track_1 = Track("Purple Rain", "Prince")
    track_2 = Track("Kiss", "Prince")
    track_3 = Track("When Doves Cry", "Prince")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("in") == [track_1, track_2, track_3]

def test_multiple_tracks_not_in_search():
    music_library = MusicLibrary()
    track_1 = Track("Purple Rain", "Prince")
    track_2 = Track("Kiss", "Prince")
    track_3 = Track("When Doves Cry", "Prince")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("zx") == []

## 


