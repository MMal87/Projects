import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.albums import Albums
from lib.albums_repository import AlbumsRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji

# """When we visit /albums, we see a list of the albums"""
@app.route('/albums', methods=['GET'])
def get_albums_html():
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)


@app.route('/albums/<id>', methods=['GET'])
def get_single_album_1(id):
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    album = repository.find(id)
    return render_template("albums/single-album.html", album=album)

# @app.route('/albums/<id>', methods=['GET'])
# def get_single_album_2(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumsRepository(connection)
#     album = repository.find(id)
#     return render_template("albums/2.html", albums=album)


# """"Album all and get albums routes"""

@app.route('/albums', methods=['POST'])
def post_albums():
    if has_no_parameters_albums(request.form):
        return "You need to submit a title, release_year and artist id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumsRepository(connection)
    album = Albums(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return '', 200

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumsRepository(connection)
#     return "\n".join(
#         f"{album}" for album in repository.all())

def has_no_parameters_albums(form):
    return ('title' not in form) or ('release_year' not in form) or ('artist_id' not in form)

""""Artist all and get artists routes"""

def has_no_parameters(form):
    return ('artist_name' not in form) or ('genre' not in form)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repository.all() 
    )


@app.route('/artists', methods=['POST'])
def post_artists():
    if has_no_parameters(request.form):
        return "You need to enter an artist AND genre", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['artist_name'], request.form['genre'])
    repository.create(artist)
    return '', 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
