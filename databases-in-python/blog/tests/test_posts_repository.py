from lib.posts_repository import PostRepository
from lib.comments import Comments
from lib.posts import Posts


"""When we call #find_all it will return the requested items"""

def test_find_with_posts(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    result = repository.find_with_comments(1)
    assert result == Posts(1, 'How to use Git', 'Here are my contents.', [Comments(2, 'Jane Smith', 'I completely agree.', 1)])

