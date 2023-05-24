from playwright.sync_api import Page, expect

# """Tests for your routes go here"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text(['Doolittle', 'Surfer Rosa', 'Waterloo', 'Super Trouper', 'Bossanova', 'Lover', 'Folklore', 'I Put a Spell on You', 'Baltimore', 'Here Comes the Sun', 'Fodder on My Wings', 'Ring Ring'])

def test_get_single_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    h2_tag = page.locator("h2")
    expect(h1_tag).to_have_text("Doolittle")
    expect(h2_tag).to_have_text("Release year: 1989")



def test_get_albums_links(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    link = page.get_by_role("link", name="Doolittle")
    expect(link).to_have_attribute("href", "/albums/1")

def test_post_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")


""""Select a single artist"""
def test_get_single_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    h2_tag = page.locator("h2")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Artists")
    expect(h2_tag).to_have_text("Pixies")
    expect(p_tag).to_have_text("Genre: Rock")

def test_get_artist_links(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tag =page.locator("h1")
    expect(h1_tag).to_have_text("Artists")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])


# """Creat new album and add to list of albums"""
def test_add_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.fill("input[name='title']", "New Album")
    page.fill("input[name='release_year']", "Release year: 1000")
    page.click("text=Create Album")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("New Album")
    # h2_tag = page.locator("h2")
    # expect(h2_tag).to_have_text("Release year: 1000")



# # """If we create a new book without a title or author
# # We see an error message
# # """
def test_validate_album(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("Your submission contains errors: " "Title must not be blank, " "Release year must be a number")


""""Test add artist method"""

def test_add_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add new artist")
    page.fill("input[name='artist_name']", "New Artist")
    page.fill("input[name='genre']", "Test Genre")
    page.click("text=Create Artist")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("New Artist")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Genre: Test Genre")

# def test_validate_artist(db_connection, page, test_web_address):
#     page.set_default_timeout(1000)
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/artists")
#     page.click("text=Add new artist")
#     page.click("text=Create Artist")
#     errors = page.locator(".t-errors")
#     expect(errors).to_have_text("Your submission contains errors: " "Artist name must not be blank, " "Genre must not be blank")











