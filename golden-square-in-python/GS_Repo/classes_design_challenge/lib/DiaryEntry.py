import math

class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Please enter a title and contents.")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        count = self.format().split()
        return len(count)
    
    def reading_time(self, wpm):
        length = len(self.contents.split())
        return math.ceil(length/wpm)


    def reading_chunk(self, wpm, minutes):
        amount_of_words = wpm * minutes
        text = self.format().split()
        if self.read_so_far >= len(text):
            self.read_so_far = 0
        chunk_start = self.read_so_far 
        chunk_end = self.read_so_far + amount_of_words
        chunk = text[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk)