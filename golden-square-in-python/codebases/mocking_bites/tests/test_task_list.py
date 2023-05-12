from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
"""Given multiple tasks, set all as complete, then call all_complete on them to return true"""
def test_all_complete_returns_true_given_multiple_tasks():
    task_list = TaskList()
    task_1 = Mock()
    task_1.is_complete.return_value = True

    task_2 = Mock()
    task_2.is_complete.return_value = True

    task_3 = Mock()
    task_3.is_complete.return_value = True

    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    assert task_list.all_complete() == True


def test_all_complete_returns_false_given_multiple_tasks():
    task_list = TaskList()
    task_1 = Mock()
    task_1.is_complete.return_value = False

    task_2 = Mock()
    task_2.is_complete.return_value = False

    task_3 = Mock()
    task_3.is_complete.return_value = False

    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    assert task_list.all_complete() == False 

    """given multiple tasks, return a list of all tasks""" 

def test_list_is_returned_given_multiple_tasks():
    task_list = TaskList()
    
    task_1 = Mock()
    task_2 = Mock()
    task_3 = Mock()
    

    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    assert task_list.all() == [task_1, task_2, task_3]

