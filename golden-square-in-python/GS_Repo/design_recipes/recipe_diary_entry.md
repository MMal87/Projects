1. Describe the Problem
Create an onject called Diary Entry, with methods that:

Take the title and entry as arguments and return a formatted version of the title and entry, with the title being capitalized.

Take no arguments but return the number of words in the diary entry

Take an argument of an integer and return the reading time in minutes for the contents of the ewntry

Take the words per minute and minutes and return how much text could be read in a given number of minutes.

2. Design the Function Signature

class DiaryEntry:
    def __init__(self, title, contents):
    instantiates the class "DiaryEntry" and initializes the title and contents variables.
    Parameters: 
        title: a string containing words
        contents: a string containing words
          
        pass

    def format(self):
        Takes the title and contents and formats them.
        Returns:
        "My Title: These are the contents"
        pass

    def count_words(self):
        Takes no parameters. 
         Returns:
           int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
         Parameters:
           wpm: an integer representing the number of words the user can read 
                per minute
         Returns:
           int: an estimate of the reading time in minutes for the contents at
                the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
         Parameters
           wpm: an integer representing the number of words the user can read
                per minute
           minutes: an integer representing the number of minutes the user has
                    to read
         Returns:
           string: a chunk of the contents that the user could read in the
                   given number of minutes
        
         If called again, `reading_chunk` should return the next chunk,
         skipping what has already been read, until the contents is fully read.
         The next call after that should restart from the beginning.
        pass


3. Create Examples as Tests

Given a title and contents, format the entry like this: "My Title: These are the contents."

def test_formatting_with_title_and_contents():
    Formats the title and contents as "My Title: These are the contents"
    diary_entry = DiaryEntry()
    diary_entry.format("My Title", "Here are my contents") --> "My Title: Here are my contents."

def test_count_words_in_diary():
    returns the number of words in the entry.
    diary_entry = DiaryEntry()
    diary_entry.count_words("My Title", "Here are my contents") --> 6

def test_reading_time()
    Given a reading speed in words per minute, it returns how long it would take to read the entry.
    diary_entry.reading_time(6) --> 1

def test_reading_chunk():
    Given a wpm and a number of minutes, it returns a chunk of text that could be read in that time.
    diary_entry.reading_chunk(6, 1) --> "My Title: Here are my contents."

    

