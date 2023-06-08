from lib.peep_repository import PeepRepository
from lib.peep import Peep


"""
When we call peepRepository#all
We get a list of peep objects reflecting the seed data.
"""

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = PeepRepository(db_connection) 
    peeps = repository.all() 
    assert peeps == [
        Peep(4, 'Late-night coding', 'Working on a new feature...', '22:45:31', 3),
        Peep(3, 'Thoughts for the day', 'Life is a journey, not a destination.', '20:16:31', 1),
        Peep(2, 'Exciting news', 'Just launched my new project!', '15:23:31', 2),
        Peep(1,'Hello world', 'My first peep!', '15:03:31', 1),
        Peep(5, 'Weekend vibes', 'Relaxing and enjoying some downtime.', '12:05:31', 2)
         
        ]
        


# """
# When we call peepRepository#create 
# We get a new record in the database.
# """
def test_create_record(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)

    repository.create(Peep(None, 'Test title', 'Test Content', '23:22:45', 2))

    result = repository.all()
    assert result ==[
        Peep(6, 'Test title', 'Test Content', '23:22:45', 2, 'Jane Smith'),
        Peep(4, 'Late-night coding', 'Working on a new feature...', '22:45:31', 3, 'Michael Johnson' ),
        Peep(3, 'Thoughts for the day', 'Life is a journey, not a destination.', '20:16:31', 1, 'John Doe'),
        Peep(2, 'Exciting news', 'Just launched my new project!', '15:23:31', 2, 'Jane Smith'),
        Peep(1,'Hello world', 'My first peep!', '15:03:31', 1, 'John Doe'),
        Peep(5, 'Weekend vibes', 'Relaxing and enjoying some downtime.', '12:05:31', 2, 'Jane Smith')
             
        ]
    