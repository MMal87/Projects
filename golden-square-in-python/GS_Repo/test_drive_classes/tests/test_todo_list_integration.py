from lib.todo_list import *
from lib.todo import *



"""Given a task, it will be added to a list"""
def test_adding_task_to_list():
    todo = TodoList() #instantiating an instance of the class
    task = Todo("shop")#adding an item
    task2 = Todo("go for a walk")
    todo.add(task)#calling the .add method to the class to add it to the list
    todo.add(task2)
    assert todo.todolist == [task, task2]
    

"""given a task, it will be marked incomplete"""
def test_mark_incomplete():
    todo =TodoList()
    task = Todo("shop")
    task2 = Todo("go for a walk")
    todo.add(task)
    todo.add(task2)
    todo.incomplete()
    assert todo.todolist == [task, task2]
    

"""Given two tasks, one marked complete, it will return a list with the task marked complete"""
def test_two_tasks_one_mark_complete():
    todo =TodoList()
    task = Todo("shop")#adding items using the Todo class
    task2 = Todo("go for a walk")
    task.mark_complete()#marking the items complete using a method from the Todo class, no the todolist class.
    todo.add(task)
    todo.add(task2)
    assert todo.complete() == [task]#returning the list containing the items marked complete

"""Given two tasks, both will be in a list of complete tasks"""
def test_two_tasks_both_marked_complete():
    todo =TodoList()
    task = Todo("shop")
    task2 = Todo("go for a walk")
    task.mark_complete()
    task2.mark_complete()
    todo.add(task)
    todo.add(task2)
    assert todo.complete() == [task, task2]  
    
"""Given a task, it will mark all todos complete """
def test_mark_all_complete():
    todo =TodoList()
    task = Todo("shop")
    task2 = Todo("go for a walk")
    task.mark_complete()
    task2.mark_complete()
    todo.add(task)
    todo.add(task2)
    assert todo.complete() == [task, task2] 

    """Use give_up to mark all tasks complete"""
 
def test_give_up():
    todo =TodoList()
    task = Todo("shop")
    todo.add(task)
    todo.give_up()
    assert todo.complete() == [task]

"""Given tasks that are already marked complete,"""
def test_give_up_with_already_marked_complete():
    todo = TodoList()
    task = Todo("shop")
    task2 = Todo("go for a walk")
    task.mark_complete()
    task2.mark_complete()
    todo.add(task)
    todo.add(task2)
    todo.give_up()
    assert todo.complete() == [task, task2]

def test_give_up_without_adding():
    todo = TodoList()
    todo.give_up()
    assert todo.complete() == []
    

