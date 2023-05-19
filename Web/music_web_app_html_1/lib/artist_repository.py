class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        names = self._connection.execute('SELECT * from artists_table')
        artist_names = []
        for name in names:
            artist_names.append(name["artist_name"])   
        return artist_names
    
    def create(self, artist):
        self._connection.execute('INSERT into artists_table (artist_name, genre) VALUES (%s, %s)', [artist.artist_name, artist.genre])
        return None



    

    # for dictionary in dict_list:
    # for key, value in dictionary.items():
    #     print(value)  # print the value of the 'artist_name' key