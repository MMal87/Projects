from lib.secret_diary import SecretDiary
import pytest

from unittest.mock import Mock


def test_lock_function():
    diary = Mock()
    diary.contents = "Here are my contents"
    diary.read.side_effect = Exception("Go away!")
    with pytest.raises(Exception) as e:
        diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_unlock_function():
    diary = Mock()
    
    diary.read.return_value = "Here are my contents"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert diary.read() == "Here are my contents"


    
    


