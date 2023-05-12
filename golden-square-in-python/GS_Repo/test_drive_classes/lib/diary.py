from lib.diary_entry import *
from math import ceil

class Diary:
    def __init__(self):
        self.entries =[]
    

    def add(self, entry):
        self.entries.append(entry)
        

    def all(self):
        return self.entries

    def count_words(self):
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        word_count = self.count_words()
        return ceil(word_count/wpm) 
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        word_count  = wpm * minutes
        most_readable = None
        longest_one = 0
        for entry in self.entries:
            if entry.count_words() <= word_count:
                if entry.count_words() > longest_one:
                    most_readable = entry
                    longest_one = entry.count_words()
        return most_readable

