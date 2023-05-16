

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


"""When I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter text
Then: I should get a 200 response with "Alice,Joe,Julia,Kieran,Zoe"  """

def test_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran' })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

"""When I make a POST request to /sort-names
And: I send "joe,alice,zoe,julia,kieran" as the body parameter text
Then: I should get a 200 response with "alice,joe,julia,kieran,zoe"  """

def test_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'joe,alice,zoe,julia,kieran' })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "alice,joe,julia,kieran,zoe" 