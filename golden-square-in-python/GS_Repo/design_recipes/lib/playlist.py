class MusicTracker():
    def __init__(self):
        self.playlist = []

    def add_track(self, track):
        if track == "":
            raise Exception("No track added")
        return self.playlist.append(track)
    
    def view_track(self):
        return self.playlist
