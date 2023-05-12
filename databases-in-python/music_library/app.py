from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        music_input = input("What would you like to do? \n 1- List all albums \n 2- List all artists\n")
        if int(music_input) == 1:
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()#returns a list of instances of artist class
            for artist in artists:
                print(artist)#iterate over artists and print to terminal
        elif int(music_input) == 2:
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(album)
        return None

        
if __name__ == '__main__':
    app = Application()
    app.run()




