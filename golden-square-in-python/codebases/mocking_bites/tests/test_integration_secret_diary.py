from lib.secret_diary import SecretDiary
from lib.diary import Diary 
import pytest

"""Given a diary entry, set to unlock, 
#read will return a string of the diary entry """

def test_single_entry_locked():
    diary = Diary("This is entry 1.")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_single_entry_unlocked():
    diary = Diary("This is entry 1.")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is entry 1."



    




