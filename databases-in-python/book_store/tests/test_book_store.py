from lib.book_store import BookStore

"""Check that variables are set up correctly"""

def test_book_variables():
    book_store = BookStore(1, "Test Title", "Test Author")
    assert book_store.id == 1
    assert book_store.title == "Test Title"
    assert book_store.author_name == "Test Author"

def test_books_format():
    book_store = BookStore(1, "Test Title", "Test Author")
    assert str(book_store) == "1 - Test Title - Test Author"