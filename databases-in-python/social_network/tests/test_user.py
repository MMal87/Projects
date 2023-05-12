from lib.user import User

def test_user_constructs():
    user = User(1, "Me", "me@example.com")
    assert user.id == 1
    assert user.username == "Me"
    assert user.email == "me@example.com"

"""cd 
# # We can format artists to strings nicely
# # """
# def test_users_format_nicely():
#     artist = User(1, "Test Name", "Test email")
#     assert str(artist) == "User(1, Test Name, Test email)"


"""
We can compare two identical Users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test name", "Test email")
    user2 = User(1, "Test name", "Test email")
    assert user1 == user2




