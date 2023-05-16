# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums', data={'title': 'Doolittle', 'release_year': '1988', 'artist_id': 1})
    assert response.status_code == 200
    assert response.status_code('utf-8') == ""