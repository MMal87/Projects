from lib.diary_tracker import *
from lib.DiaryEntry import *
import pytest
from lib.phone_number_extract import PhoneNumberExtractor


def test_multiple_diary_entries_with_view_diary():
    diary = Diary()
    entry_1 = DiaryEntry("My title", "Today I went outside.")
    entry_2 = DiaryEntry("My title", "Today I stayed at home.")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.view_diary() == [entry_1, entry_2]


# """When I add multiple tasks, they are listed in all_incomplete"""

# todo_list = ToDoList()
# task_1 = Task("Shop")
# task_2 = Task("eat")
# task_3 = Task("walk")
# todo_list.incomplete() == [task_1, task_2, task_3]





# it will return a list of all the mobile phone numbers in the entries"""

diary = Diary()
entry_1 = DiaryEntry("my title 1", "Today I went outside. 07653427453")
entry_2 = DiaryEntry("my title 2", "Today I stayed at home.")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
assert extractor.extract() == ["07653427453"]


# # 4. Create examples as unit tests

# # Diary unit tests

# """to begin with, view diary will be empty"""
# diary = Diary()
# diary.view_diary == []


# """to begin with the view_tasks list is empty"""
# diary = Diary()
# diary.view_tasks == []

# """to begin with the contacts list is empty"""
# diary = Diary()
# diary.view_contacts == []

# # diaryEntry unit tests


# """When we add an entry, it is reflected in the entry name"""
# diaryentry = DiaryEntry()
# diaryentry.add("Here is my diary")
# diaryentry.contents => "Here is my diary"


# # # Todo unit tests

# """when we add a task, it is reflected in the task name"""
# task = ToDoList()
# task.add_task("eat")
# task.task => "eat"

# """when we add multiple tasks, they are added to a list of tasks"""

# task = Todo()
# task.add_task("eat")
# task.add_task("sleep")
# task.task => ["eat", "sleep"]
# """