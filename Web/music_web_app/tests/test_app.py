




def test_get_list(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1988, 1)"


def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post('/albums', data={'title': 'Bossanova', 'release_year': '1990', 'artist_id': '1'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Album(1, Doolittle, 1988, 1)\n" "Album(2, Bossanova, 1990, 1)"


def test_no_input(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a title, release_year and artist id"
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Album(1, Doolittle, 1988, 1)"

