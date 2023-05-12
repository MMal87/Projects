class DiaryEntry:
    title = ""
    contents = ""

    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def count_words(self):
        content = self.contents.split()
        return len(content)

    def reading_time(self, wpm):
        text_length = len(self.contents.split())
        return text_length/wpm
        

    def reading_chunk(self, wpm, minutes):
        amount_of_words = wpm * minutes
        text = self.contents.split()
        if self.read_so_far >= len(text):
           self.read_so_far = 0
       
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + amount_of_words
        chunk = " ".join(text[chunk_start: chunk_end])
      

        self.read_so_far += amount_of_words
        return chunk





