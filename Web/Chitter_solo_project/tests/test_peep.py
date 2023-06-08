from lib.peep import Peep

def test_peep_constructs():
    peep = Peep(1, "Test Title", "Test content", "15:15:15", 1)
    assert peep.id == 1
    assert peep.title == "Test Title"
    assert peep.content == "Test content"
    assert peep.created_at == "15:15:15"
    assert peep.user_id == 1

    

"""cd 
# # We can format artists to strings nicely
# # """
def test_peeps_format_nicely():
    peep = Peep(1, "Test Title", "Test content", "15:15:15", 1)
    assert str(peep) == "Peep(1, Test Title, Test content, 15:15:15, 1)"


"""
We can compare two identical peeps
And have them be equal
"""
def test_peeps_are_equal():
    peep1 = Peep(1, "Test Title", "Test content", "15:15:15", 1)
    peep2 = Peep(1, "Test Title", "Test content", "15:15:15", 1)
    assert peep1 == peep2


