from lib.task_tracker import TaskTracker
from lib.task import Task

"""When tasks are marked complete, they will be removed from incomplete list"""

def test_mark_task_complete_remove_from_incomplete():
    todo_list = TaskTracker()
    task_1 = Task("Shop")
    task_2 = Task("eat")
    task_3 = Task("walk")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.incomplete() == [task_1, task_2, task_3]
    
