from lib.calculate_reading_time import *
import pytest


def test_two_hundred_word_text():
    text = " ".join(["word" for i in range(0, 200)])
    result = calculate_reading_time(text)
    assert result == 1.0

def test_three_hundred_word_text():
    text = " ".join(["word" for i in range(0,300)])
    result = calculate_reading_time(text)
    assert result == 1.5

def test_empty_string():
    with pytest.raises(Exception) as e:
        calculate_reading_time("")
    error_message = str(e.value)

    assert error_message == "Please enter some text."

    