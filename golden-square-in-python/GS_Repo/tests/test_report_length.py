from lib.report_length import *

def test_report_length_is_correct():
    result_correct = report_length("horse")
    assert result_correct == "This string was 5 characters long."

def test_report_length_is_short():   
    result_short = report_length("a")
    assert result_short == "This string was 1 characters long."

def test_report_length_is_caps():
    result_caps = report_length("HORSE")
    assert result_caps == "This string was 5 characters long."

def test_report_length_is_spaces():
    result_spaces = report_length(" horse ")
    assert result_spaces == "This string was 7 characters long."

def test_report_length_has_only_spaces():
    result_only_spaces = report_length("   ")
    assert result_only_spaces == "This string was 3 characters long."

def test_report_length_is_incorrect_argument_datatype():
    result_integer = report_length(5)
    assert result_integer == "Incorrect argument given."
    result_float = report_length(5.6)
    assert result_float == "Incorrect argument given."
    result_boolean = report_length(True)
    assert result_boolean == "Incorrect argument given."
    result_list = report_length([])
    assert result_list == "Incorrect argument given."
