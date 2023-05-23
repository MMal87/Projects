class Artist():
    def __init__(self, id, artist_name, genre):
        self.id = id
        self.artist_name = artist_name
        self.genre = genre
    def __eq__(self, other):#allows us to compare if one instance of artist is equal to another, by comparing all properties shown above
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Artist({self.id}, {self.artist_name}, {self.genre})"

