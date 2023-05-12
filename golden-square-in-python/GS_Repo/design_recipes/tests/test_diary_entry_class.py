import pytest
from lib.diary_entry_class import *
"""Given a title and contents, format the entry like this: "My Title: These are the contents."""
def test_empty_string():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Please enter a title and contents."

""" Formats the title and contents as "My Title: These are the contents"""
def test_format_diary():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.format()
    assert result == "My Title: These are the contents"

"""returns the number of words in the entry."""
def test_count_words():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.count_words()
    assert result == 6

"""Given a reading speed in words per minute, it returns how long it would take to read the entry."""
def test_reading_time():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.reading_time(6)
    assert result == 1

"""Given a wpm and a number of minutes, it returns a chunk of text that could be read in that time."""
def test_reading_time_with_number_not_whole():
    diary = DiaryEntry("My Title", "These")
    result = diary.reading_time(2)
    assert result == 1


"""Given a wpm of 2 and a number of minutes of 1, it returns a chunk of text that could be read."""
def test_reading_chunk():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.reading_chunk(2, 1)
    assert result == "My Title:"

def test_reading_chunk_two_entries():
    diary = DiaryEntry("My Title", "These are the contents")
    assert diary.reading_chunk(3,1) == "My Title: These"
    assert diary.reading_chunk(3,1) == "are the contents"

def test_reading_chunk_looping_round():
    diary = DiaryEntry("My Title", "These are the contents")
    assert diary.reading_chunk(3,1) == "My Title: These"
    assert diary.reading_chunk(3,1) == "are the contents"
    assert diary.reading_chunk(3,1) == "My Title: These"

    

