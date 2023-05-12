from lib.check_codeword import *
def test_check_codeword_is_horse():
    # remember to have variable passing in function name with argument
    result_horse = check_codeword("horse")
    assert result_horse == "Correct! Come in."
    
def test_codeword_is_close():
    result_close = check_codeword("hive")
    assert result_close == "Close, but nope."
    
def test_wrong_codeword():
    result_wrong = check_codeword("nope")
    assert result_wrong == "WRONG!"