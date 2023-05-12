import pytest
from lib.improve_grammar import *



def test_improve_grammar_returns_true():
    result = improve_grammar("Hello World!")
    assert result == True

def test_improve_grammar_returns_False():
    result = improve_grammar("hello world")
    assert result == False

def test_with_capital_without_punctuation():
    result = improve_grammar("Hello, world")
    assert result == False

def test_with_empty_string():
    with pytest.raises(Exception) as e:
        improve_grammar("")
    error_message = str(e.value)
    assert error_message == "Please enter some text."

def test_with_capital_with_punctuation_elsewhere():
    result = improve_grammar("Hello! world")
    assert result == False
