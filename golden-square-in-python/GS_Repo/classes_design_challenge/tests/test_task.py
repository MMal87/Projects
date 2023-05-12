from lib.task import Task
"""Task constract with title"""

def test_task_constructs():
    task = Task("Go for a walk")
    task.title == "Go for a walk"

""""New tasks will be incomplete"""

def test_task_incomplet():
    task = Task("Go for a walk")
    assert task.complete == False

"""When task marked complete, it is reflected in complete"""
def test_mark_task_complete():
    task = Task("Go for a walk")
    assert task.complete == True