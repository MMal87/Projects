from lib.user_repository import UserRepository
from lib.user import User

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() 

    # Assert on the results
    assert users == [
        User(1, "John Doe", "john.doe@example.com"),
        User(2, "Jane Doe", "jane.doe@example.com")
        
    ]


"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Jimmy Doe", "jimmy.doe@example.com"))

    result = repository.all()
    assert result == [
        User(1, "John Doe", "john.doe@example.com"),
        User(2, "Jane Doe", "jane.doe@example.com"),
        User(3, "Jimmy Doe", "jimmy.doe@example.com")
    
    
    ]

    

