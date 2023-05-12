# 1. Describe the problem


As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
*add todos, mark complete, list complete, list incomplete 
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

* a phone number starts with 0 and is 11 digits long.

# 2. Design the class system

Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. you can use asciiflow.com, excalidraw.com, draw.io or miro.com 

# verbs

record (diary entries)
keeo
reflect
read 
select
keep (todo)
see list
# nouns
diary entry
list of diary entries
experiences
time
reading speed
to do list
phone numbers
list of phone numbers




        ┌──────────────────────────┐
        │                          │
        │  Diary                   │
        │  -Add entry(entry)       │
        │  -show all entries()     │
        │  -Select entry(wpm,      │
        │                minutes)  │
        │  -view todo list()       │
        │  -view phone numbers()   │
        │                          │
        └──────────────────────────┘


        ┌──────────────────────────┐
        │ DiaryEntry               │
        │                          │
        │ -Add(contents)    │
        │                          │
        │ -View entries()          │
        │                          │
        │                          │
        │                          │
        │                          │
        └──────────────────────────┘



        ┌──────────────────────────┐
        │  Todo                    │
        │                          │
        │  -Add(todo)
          - mark complete
         -list complete
           - list incomplete       │
        │                          │
        │                          │
        │                          │
        │                          │
        │                          │
        │                          │
        └──────────────────────────┘




        ┌──────────────────────────┐
        │   PhoneNumbers           │
        │                          │
        │  -listNumbers()          │
        │                          │
        │                          │
        │                          │
        │                          │
        │                          │
        │                          │
        └──────────────────────────┘



    class Diary():
        
       def init(self, entries, todolist, contacts)
            Parameters
            entries list to represent diary entries
            todolist to represent todo list items
            contacts list to represent phone numbers
        def add(self, diary_entry)
            diary_entry- instance of DiaryEntry
            side effects- add an entry to diary list 


        def view_diary()
            side effects- show all diary entries
            pass



class DiaryEntry(self):
        def __init__(self, title, contents)
            title: string representing title
            contents: string representing contents
            side effects- setsa the properties
        
       
class ToDoList()

    def add_task(self, task):
        paramters: task
        side effects- adds task to list
    def incomplete(self):
        returns a list of instances of task representing incomplete tasks
        pass

    def  complete():
        returns a list of instances of task representing complete tasks
        pass

class Task():
    def __init__(self, text):
    text- string representing a task to do
    sets text property

    def marl_complete(self)
        marks task as complete
        returns nothing
        pass

class PhoneNumberRemover():
    def __init__(self, diary):
        diary: an instance of Diary
        set diary property
        pass
    def remove(self):
        returns a list of strings representing a list of phone numbers
        pass

class ReadableEntryFinder():

    def __init__():
        no parameters
    
    def list_contacts():
        display all phone numbers in diary entries


            
# 3. Create Examples as Inetegration tests


when I add multiple diary entries, I should be able to view them using the diary class

diary = Diary()
entry_1 = DiaryEntry("Today I went outside.")
entry_2 = DiaryEntry("Today I stayed at home.")
diary.add(entry_1)
diary.add(entry_2)
diary.view_diary() => [entry_1, entry_2]


when I add multiple entries and call on the view_entries_by_time method
it will return which entries I can read in that time

diary = Diary()
entry_1 = DiaryEntry("Today I went outside.")
entry_2 = DiaryEntry("Today I stayed at home.")
diary.add(entry_1)
diary.add(entry_2)

"""When I add multiple tasks, they are listed in all_incomplete"""
todo_list = task_tracker()
task_1 = Task("Shop")
task_2 = Task("eat")
task_3 = Task("walk")
todo_list.incomplete() == [task_1, task_2, task_3]

"""When I add multiple tasks, they are listed in all_incomplete"""

todo_list = ToDoList()
task_1 = Task("Shop")
task_2 = Task("eat")
task_3 = Task("walk")
task_1.mark_complete()
todo_list.complete() == [task_1]

when I add multiple diary entries and I use PhoneNumberRemover, I will get a list of numberas from all the diary entries

diary = Diary()
entry_1 = DiaryEntry("Title 1", "Today I went outside. My friend's number is: 07653427453")
entry_2 = DiaryEntry("Title 2", "Today I stayed at home.")
entry_3 = DiaryEntry("Title 3", "My friend is: 07375625389")
diary.add(entry_1)
diary.add(entry_2)
diary.view_contacts => ["07653427453", "07375625389"]

When I add multiple diary entries, it ignores invalid numbers
diary = Diary()
entry_1 = DiaryEntry("Title 1", "Today I went outside. My friend's number is: 07653")
entry_2 = DiaryEntry("Title 2", "Today I stayed at home. 075432")
entry_3 = DiaryEntry("Title 3", "My friend is: 07375625389")
diary.add(entry_1)
diary.add(entry_2)
diary.view_contacts => ["07375625389"]

When I add multiple diary entries

# 4. Create examples as unit tests

# Diary unit tests

to begin with, view diary will be empty
diary = Diary()
diary.view_diary == []


to begin with the view_tasks list is empty
diary = Diary()
diary.view_tasks == []

to begin with the contacts list is empty
diary = Diary()
diary.view_contacts == []

# diaryEntry unit tests


When we add an entry, it is reflected in the entry name
diaryentry = DiaryEntry()
diaryentry.add("Here is my diary")
diaryentry.contents => "Here is my diary"


# Todo unit tests



when we add multiple tasks, they are added to a list of tasks and added to incomplete

task = Todo()
task.add_task("eat")
task.add_task("sleep")
task.task => ["eat", "sleep"]

when we mark some tasks complete, they are 






