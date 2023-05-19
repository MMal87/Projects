from playwright.sync_api import Page, expect

# Tests for your routes go here
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tag = page.locator("h2")
    p_tag = page.locator("p")
    expect(h2_tag).to_have_text(["Title: Doolittle", "Title: Surfer Rosa"])
    expect(p_tag).to_have_text(["Released: 1989", "Released: 1988"])

def test_get_single_albums_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Doolittle")
    expect(p_tag).to_have_text("Release year: 1989\nArtist: Pixies")

# def test_get_single_albums_2(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/albums/2")
#     h1_tag = page.locator("h1")
#     p_tag = page.locator("p")
#     expect(h1_tag).to_have_text("Surfer Rosa")
#     expect(p_tag).to_have_text("Release year: 1988\nArtist: Pixies")