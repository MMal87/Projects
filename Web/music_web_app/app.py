import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request
from lib.artist_repository import ArtistRepository

from lib.artist import Artist
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     return ":)"

# @app.route('/artists', methods=['POST'])
# def post_artists():
#     if has_no_parameters(request.form):
#         return "You need to submit a title, release_year and artist id", 400
#     connection = get_flask_database_connection(app)
#     repository = artistsRepository(connection)
#     artist = artists(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
#     repository.create(artist)
#     return '', 200

# @app.route('/artists', methods=['GET'])
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = artistsRepository(connection)
#     return "\n".join(
#         f"{artist}" for artist in repository.all() 
#     )

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




# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
