import pytest
from lib.password_checker import *

#Muniba Malik
# Lets first test if the length is more than or equal to eight.
def test_if_pass_is_correct_length():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("abcdefgh") == True
# Test if password is less than 8 digits
def test_password_less_than_eight_digits_return_invalid():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("abcdefg")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
#Tests for an empty string.
def test_empty_string():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
#Tests for more than one incorrect password.
def test_more_than_one_pass_added():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("123456")
        passwordchecker.check("abcdeh")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
#test for more than one correct password
def test_more_than_one_correct_password_added():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("12345678") and passwordchecker.check("abcdefgh") == True
#Test for one incorrect password and one correct password.
def test_one_pass_correct_and_one_pass_incorrect():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("12345678") == True
    with pytest.raises(Exception) as e:
        passwordchecker.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."











