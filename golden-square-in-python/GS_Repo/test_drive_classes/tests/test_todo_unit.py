from lib.todo import *
import pytest

"""Given a task, set it to true in mark_complete"""

def test_task_set_to_true():
    todo = Todo("shop")
    todo.mark_complete()
    assert todo.complete == True

"""Given an emoty string, return None"""

def test_task_empty_string():
    todo = Todo("")
    with pytest.raises(Exception) as e:
        todo.mark_complete()
    error_message = str(e.value)
    assert error_message == "Please enter a task:"


