from lib.posts import Posts

"""initialize variables"""

def test_variables_are_created():
    posts = Posts(1, "Test Title", "test contents")
    assert posts.id == 1
    assert posts.title == "Test Title"
    assert posts.post_content == "test contents"

def test_comments_are_equal():
    post1 = Posts(1, "Test Title", "test contents")
    post2 = Posts(1, "Test Title", "test contents")
    assert post1 == post2