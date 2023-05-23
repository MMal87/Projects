from playwright.sync_api import Page, expect

# """Tests for your routes go here"""
# def test_get_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     h2_tag = page.locator("h2")
#     expect(h2_tag).to_have_text(['Doolittle', 'Surfer Rosa', 'Waterloo', 'Super Trouper', 'Bossanova', 'Lover', 'Folklore', 'I Put a Spell on You', 'Baltimore', 'Here Comes the Sun', 'Fodder on My Wings', 'Ring Ring'])

# def test_get_single_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/albums/1")
#     h1_tag = page.locator("h1")
#     p_tag = page.locator("p")
#     expect(h1_tag).to_have_text("Doolittle")
#     expect(p_tag).to_have_text("Release year: 1989\nArtist: Pixies")



# def test_get_single_albums_4(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/albums/4")
#     h1_tag = page.locator("h1")
#     p_tag = page.locator("p")
#     expect(h1_tag).to_have_text("Super Trouper")
#     expect(p_tag).to_have_text("Release year: 1980\nArtist: Abba")

# def test_get_albums_links(page, test_web_address):
#     page.goto(f"http://{test_web_address}/albums")
#     link = page.get_by_role("link", name="Doolittle")
#     expect(link).to_have_attribute("href", "/albums/1")


# """"Select a single artist"""
# def test_get_single_artist(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/artists/1")
#     h1_tag = page.locator("h1")
#     h2_tag = page.locator("h2")
#     p_tag = page.locator("p")
#     expect(h1_tag).to_have_text("Artists")
#     expect(h2_tag).to_have_text("Pixies")
#     expect(p_tag).to_have_text("Genre: Rock")




# def test_get_artist_links(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/artists")
#     h1_tag =page.locator("h1")
#     expect(h1_tag).to_have_text("Artists")
#     h2_tag = page.locator("h2")
#     expect(h2_tag).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])
#     link = page.get_by_role("link_album", name="Pixies")
#     expect(link).to_have_attribute("href", "/artists/1")



"""Creat new artist and add to list of artists"""
def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='release_year']", "1000")
    page.fill("input[name='artist_id']", "Pixies")
    page.click("text=Create Album")
    page.goto(f"http://{test_web_address}/albums/13")
    title_element = page.locator("h1")#this is referring to the single-album html
    expect(title_element).to_have_text("Test Album")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text("Release year: 1000\nArtist: Pixies")












