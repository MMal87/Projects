from lib.book_store_repository import BookRepository
from lib.book_store import BookStore

"""When calling BookRepository #all method, we will get a list of all the book objects"""

def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    book_repo = BookRepository(db_connection)
    books = book_repo.all()

    assert books == [
        BookStore(1, "Nineteen Eighty-Four","George Orwell"),
        BookStore(2, "Mrs Dalloway", "Virginia Woolf"),
        BookStore(3, "Emma", "Jane Austen"),
        BookStore(4, "Dracula", "Bram Stoker"),
        BookStore(5, "The Age of Innocence", "Edith Wharton")
        ]