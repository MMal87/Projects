from lib.comments import Comments

"""initialize variables"""

def test_variables_are_created():
    comments = Comments(1, "Test Author", "Test Content", "Test post_id")
    assert comments.id == 1
    assert comments.author_name == "Test Author"
    assert comments.content == "Test Content"
    assert comments.post_id == "Test post_id"

def test_comments_are_equal():
    comment1 = Comments(1, "Test Author", "Test Content", "Test post_id")
    comment2 = Comments(1, "Test Author", "Test Content", "Test post_id")
    assert comment1 == comment2

