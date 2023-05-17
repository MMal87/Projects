_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# artist 
GET /artists
expected response: 200 status code 
and list of artists
Pixies
Abba
Taylor Swift 
Nina Simone   

# albums  route
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)
```
# artist 
GET /artists
expected response: 200 status code 
and list of artists
Pixies, Abba, Taylor Swift, Nina Simone, Wild Nothing 



## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._
test all 
returns 200 status code 

def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, Abba, Taylor Swift, Nina Simone'

def test_post_artist(web_client):
    post_response = web_client.post('/artists', data={
      'artist_name': 'Wild Nothing', 'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    get_response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, Abba, Taylor Swift, Nina Simone'

def test_no_artist_input(web_client):
    response = web_client.post('/artists')
    assert post_response.status_code == 400
    assert response.data.decode('utf-8') == "You need to enter an artist AND genre"
    get_response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, Abba, Taylor Swift, Nina Simone'

  




_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


"""

# POST /albums
#  Parameters:
#   title: Doolittle
    release_year: 1988
    artist_id: 1
#  Expected response (200 OK):
"""

"""
# POST /albums
#  Parameters:
#   title: Bossanova
    release_year: 1990
    artist_id: 1
#  Expected response (200 OK):
"""
"""

# GET /albums
# expected response
#Album(1, Doolittle, 1)
#Album(2, Bossanova, 1)

POST /albums
400 Bad Request "You need to submit a title, release year and artist id"


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title': 'Doolittle', 'release_year': '1988', 'artist_id': 1})
    assert response.status_code == 200
    assert response.status_code('utf-8') == 'Doolittle, 1998, 1'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
