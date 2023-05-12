from lib.to_do import *

def test_is_there_todo_function():
    result = to_do("")
    assert result == False
def test_if_todo_at_start():
    result = to_do("#TODO, cook, shop")
    assert result == True

def test_if_todo_not_present():
    result = to_do("cycle, cook, shop")
    assert result == False
