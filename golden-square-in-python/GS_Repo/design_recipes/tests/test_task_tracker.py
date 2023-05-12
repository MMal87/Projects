import pytest
from lib.task_tracker import *

# To begin with, no tasks

def test_tracker_no_tasks():
    tracker = TaskTracker()
    assert tracker.incomplete() == []

# Adding a task to the list

def test_one_task_added():
    tracker = TaskTracker()
    tracker.add_task("mow the lawn")
    assert tracker.incomplete() == ["mow the lawn"]

def test_multiple_tasks_added():
    tracker = TaskTracker()
    tracker.add_task("mow the lawn")
    tracker.add_task("feed the pet")
    tracker.add_task("vacuum the room")
    assert tracker.incomplete() == ["mow the lawn", "feed the pet", "vacuum the room"]

def test_task_too_low_complete():
    tracker = TaskTracker()
    tracker.add_task("mow the lawn")
    with pytest.raises(Exception) as e:
        tracker.complete(-1)
    assert str(e.value) == "There is no task"
    assert tracker.incomplete() == ["mow the lawn"]

def test_task_too_low_complete():
    tracker = TaskTracker()
    tracker.add_task("mow the lawn")
    with pytest.raises(Exception) as e:
        tracker.complete(1)
    assert str(e.value) == "There is no task"
    assert tracker.incomplete() == ["mow the lawn"]