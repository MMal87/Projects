# 1. Describe the problem


> As a user
so that I can keep track of tasks
I want a program that I can add todo tasks to and see a list of them

>as a user
so that I can focus on tasks to cxomplete
I want to mark tasks as complete and have them disappear from the list 

# 2. Design the class system

Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. you can use asciiflow.com, excalidraw.com, draw.io or miro.com 

# verbs

add todo tasks
see list

mark tasks complete
tasks disappear

# nouns
task
list of tasks
program
    ┌───────────────────────────┐
    │                           │
    │                           │
    │        List of tasks      │
    │ -Add(task)                │
    │ -list_incomplete()        │
    │ -list_complete()          │
    │                           │
    │                           │
    │                           │
    │                           │
    │                           │
    └──────────────┬────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │                              │
    │   Task                       │
    │   - title [property]                           │
    │   -initialize               │
    │                              │
    │  -mark_complete()            │
    │  -complete (property)        │
    │                              │
    │                              │
    │                              │
    │                              │
    └──────────────────────────────┘

class TaskList():
    def add(self,task):
        # Parameters:
        # task- an instancde of the Task class
        #Side effects:
        # Adds the task to an internal list of tasks
        pass

    def list_incomplete(self):
        # Returns:
        # a list of instances of Task that are complete 

    def list_complete(self):
        #Returns:
        # A list of instances of Task that are complete
        pass

    class Task():
    # public properties:
    # title: a string representing a job to do
    # complete a boolean, true if task is complete, false otherwise 
        def __init__(self, title):
            #Parameters:
            #  title: a string representing a job to do
            #Side Effects
            # sets the title property
            # sets the task incomplete at first 
            pass
        
        
        def mark_complete():
            # side-effects: marks task complete
            pass

        
# 3. Create Examples as Inetegration tests


When i add a task
it comes back in the incomplete list 
tracker = TaskTracker()
task = Task("Walk the dog")
task = Task("Feed cat")
tracker.add(task)
tracker.list_incomplete() --> [task_1, task_2]


when i add multiple tasks and mark one complete, 
it does not show up in the incomplete list anymore
tracker = TaskTracker()
task = Task("Walk the dog")
task = Task("Feed cat")
tracker.add(task_1)
tracker.add(task_2)
task_2.mark_complete()
tracker.list_incomplete() --> [task_1]

when i add multiple tasks and mark one complete, 
complete task shows up in complete list
tracker = TaskTracker()
task = Task("Walk the dog")
task = Task("Feed cat")
tracker.add(task_1)
tracker.add(task_2)
task_2.mark_complete()
tracker.list_complete() --> [task_2]


# 4. Create examples as unit tests

initially, the incomplete tasks is empty
# Task tracker unit tests
tracker = Tasktracker()
tracker.list_incomplete() --> []


initially, the complete tasks is empty

tracker = Tasktracker()
tracker.list_complete() --> []    


# Task unit tests

when we construct with a title,
we get the title reflected in the title property

task = Task("walk the dog")
task.title => "walk the dog"

when we construct
the task is initially incomplete

task = Task("Walk the dog")
task.complete => False

when we mark the task as complete
it is complete

task = Task("Walk the dog")
task.complete => True


        


