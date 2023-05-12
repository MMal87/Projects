from lib.diary import *
from lib.diary_entry import *


""" Given I add two diary entries, 
I can see them represented in the list"""
def test_multiple_entries_and_list_them():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    entry_2 = DiaryEntry("Title2:", "These are my contents.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


"""Given I add two entries, 
I can calculate the word count as 10"""
def test_count_words_of_contents():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    entry_2 = DiaryEntry("Title2:", "These are my contents as well.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 10


"""Given that I add two entries and an int for wpm,
I can calculate the reading time"""
def test_reading_time_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    entry_2 = DiaryEntry("Title2:", "These are my contents.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(3) == 3

"""Given one entry, wpm and minutes,
I can choose an entry that is best for a specific reading time"""

def test_best_entry_for_reading_time_one_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(7, 1) == entry_1

"""Given two diary entries with lengths of 4 words and 7 words,
if i enter a reading time of 4, it will return the first entry"""

def test_best_entry_for_reading_time_two_entries_lowest_wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    entry_2 = DiaryEntry("Title2:", "These are my contents as an example.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(4, 1) == entry_1


"""Given a reading time that is not long enough for the amount of words, return None"""
def test_findbestentry_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry("Title2:", "These are my contents as an example.")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 1) == None

"""Given two diary entries with lengths of 4 words and 7 words,
if i enter a reading time of 7, it will return the second entry"""

def test_best_entry_for_reading_time_two_entries_highest_wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Title:", "These are my contents.")
    entry_2 = DiaryEntry("Title2:", "These are my contents as an example.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2


"""SHould add some exceotions for having no entries added"""




