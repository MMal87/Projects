
class MusicLibrary:
    def __init__(self):
        self.tracks = []
        
    def add(self, track):
        return self.tracks.append(track)

    def search(self, keyword):
        match_list = []
        for item in self.tracks:
            if item.matches(keyword) == True:
                match_list.append(item)
        return match_list

