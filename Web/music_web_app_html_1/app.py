import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.albums import Albums
from lib.albums_repository import AlbumsRepository
from lib.album_parameters_validator import AlbumParametersValidator

# Create a new Flask app
app = Flask(__name__)


""""App to link album names to pages with album details"""
@app.route('/albums', methods=['GET'])
def get_albums_html():
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

"""When entering an album id, return the album linked """
@app.route('/albums/<id>', methods=['GET'])
def get_single_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    album = repository.find(id)
    return render_template("albums/single-album.html", album=album)

# @app.route('/albums', methods=['POST'])
# def post_albums():
#     if has_no_parameters_albums(request.form):
#         return "You need to submit a title, release_year and artist id", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumsRepository(connection)
#     album = Albums(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
#     repository.create(album)
#     return '', 200


""""Album all and get albums routes"""

@app.route('/albums/new', methods=["GET"])
def show_form():
    return render_template("albums/new.html")

@app.route('/albums', methods=["POST"])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    # title = request.form['title']
    # release_year = int(request.form['release_year'])
    validator = AlbumParametersValidator(request.form['title'], request.form['release_year'])
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
    
    album = Albums(None, validator.get_valid_title, validator.get_valid_release_year, 1)
    #create a new album
    # album = Albums(None, title, release_year, 1)
    #cgeck validity and if not, show form again with errors
    # if not album.is_valid():
    #         return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

    repository.create(album)
    return redirect(f"/albums/{album.id}")


def has_no_parameters_albums(form):
    return ('title' not in form) or ('release_year' not in form) or ('artist_id' not in form)





""""Artist all and get artists routes"""

def has_no_parameters(form):
    return ('artist_name' not in form) or ('genre' not in form)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/index.html", artists=artists)


@app.route('/artists/<id>', methods=['GET'])
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.find(id)
    return render_template("artists/single-artist.html", artists=artists)


"""When adding an artist, it appears in the list of artists"""
@app.route('/artists/new', methods=["GET"])
def show_artist_form():
    return render_template("artists/new.html")

@app.route('/artists', methods=["POST"])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_name = request.form['artist_name']
    genre = request.form['genre']
    artist = Artist(None, artist_name, genre)
    repository.create(artist)
    return redirect(f"/artists/{artist.id}")   






# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
