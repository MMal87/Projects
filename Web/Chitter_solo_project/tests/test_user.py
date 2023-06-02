from lib.user import User

def test_user_constructs():
    user = User(1, "Me", "Password", "me@example.com")
    assert user.id == 1
    assert user.name == "Me"
    assert user.password == "Password"
    assert user.email == "me@example.com"

"""cd 
# # We can format artists to strings nicely
# # """
def test_users_format_nicely():
    user = User(1, "Test Name", "Password", "Test email")
    assert str(user) == "user(1, Test Name, Password, Test email)"


"""
We can compare two identical Users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test name", "Password", "Test email")
    user2 = User(1, "Test name", "Password", "Test email")
    assert user1 == user2
