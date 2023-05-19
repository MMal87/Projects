# Single Album Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# albums route
GET /albums/1

GET/albums/2


## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /albums/1
#  Expected response (200 OK):
"""
 Doolittle
  Release year: 1989
  Artist: Pixies

# GET /albums/2
Surfer Rosa
  Release year: 1988
  Artist: Pixies
"""


## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /albums
  Expected response (200 OK):
  
"""
def test_get_albums(web_page):
    web_page.goto("http://localhost:5000/albums/1")
    h1_tag = web_page.locator("h1")
    p_tag = web_page.locator("p")
    expect(h1_tag).to_have_text("Doolittle")
    expect(p_tag).to_have_text("Release year: 1989\nArtist: Pixies")

    web_page.goto("http://localhost:5000/albums/2")
    h1_tag = web_page.locator("h1")
    p_tag = web_page.locator("p")
    expect(h1_tag).to_have_text("Surfer Rosa")
    expect(p_tag).to_have_text("Release year: 1988\nArtist: Pixies")


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->