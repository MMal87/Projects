from lib.user_repository import UserRepository
from lib.user import User

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository
    users = repository.all() 
    assert users == [
        User(1, 'John Doe', 'password123', 'johndoe@me.com'),
        User(2, 'Jane Smith', 'securepass', 'janesmith@me.com'),
        User(3, 'Michael Johnson', 'pass1234', 'michaeljohnson@me.com'),   
    ]


"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'Jim Doe', 'password1234', 'jimdoe@me.com'))

    result = repository.all()
    assert result ==[
        User(1, 'John Doe', 'password123', 'johndoe@me.com'),
        User(2, 'Jane Smith', 'securepass', 'janesmith@me.com'),
        User(3, 'Michael Johnson', 'pass1234', 'michaeljohnson@me.com'),
        User(4, 'Jim Doe', 'password1234', 'jimdoe@me.com')
    ]