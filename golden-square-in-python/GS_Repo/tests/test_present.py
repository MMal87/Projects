import pytest
from lib.present import *


#test if 
def test_wrap_already_wrapped():
    present = Present()
    present.wrap("candle")
    with pytest.raises(Exception) as e:
        present.wrap("candle")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_wrap_has_none():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."    

def test_wrap_has_none():
    present = Present()
    present.wrap("candle")
    assert present.unwrap() == "candle"

def test_wrap_different_parameter():
    present = Present()
    present.wrap(22)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    assert present.unwrap() == 22
    
