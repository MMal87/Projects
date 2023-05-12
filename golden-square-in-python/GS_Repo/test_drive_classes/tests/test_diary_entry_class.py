from lib.diary_entry import *

"""intialize the title and contents variables and return title and contents"""

def test_initializing_vars():
    diary_entry = DiaryEntry("Title", "These are my contents.")
    assert diary_entry.title == "Title"
    assert diary_entry.contents == "These are my contents."

"""Given a title and contents,
I can calculate the word count of the contents as"""
def test_count_words():
    diary_entry = DiaryEntry("Title", "These are my contents.")
    assert diary_entry.count_words() == 4

"""Given a title and contents, plus 4 wpm,
I can calculate the reading time of 1"""
def test_reading_time():
    diary_entry = DiaryEntry("Title", "These are my contents.")
    assert diary_entry.reading_time(4) == 1

"""Given wpm and minutes, 
I can return a chunk of text that can be read in that time."""
def test_reading_chunk():
    diary_entry = DiaryEntry("Title", "These are my contents.")
    assert diary_entry.reading_chunk(4, 1) == "These are my contents."

"""Given wpm and minutes, 
I can return a chunk of text that can be read in that time ."""
def test_reading_chunk_with_multiple_entries():
    diary_entry = DiaryEntry("Title", "These are my contents.")
    diary_entry.reading_chunk(2,1)
    assert diary_entry.reading_chunk(2, 1) == "my contents."
    

"""Given a wpm and minutes that are not long enough to read the shortest text,
return None """


