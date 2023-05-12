class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        if self.title == "" or self.artist == "":
            raise Exception("Please enter something")

    def matches(self, keyword):
        if keyword in self.title or keyword in self.artist:
            return True
        return False
