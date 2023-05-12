import pytest
from lib.grammar_stats import *

def test_grammar_when_true():
    grammar = GrammarStats()
    assert grammar.check("A string of text!") == True

def test_grammar_check_when_false_with_no_capital():
    grammar = GrammarStats()
    assert grammar.check("a string of text!") == False

def test_grammar_check_when_false_with_no_specialchars():
    grammar = GrammarStats()
    assert grammar.check("A string of words") == False

"""Could test the counter variables here to see if they workas expected, but this wouldnt be fully necessary"""

def test_percentage_good_correct():
    grammar = GrammarStats()
    grammar.check("A string of text!")
    assert grammar.percentage_good() == 100
def test_percentage_good_two_entries_correct():
    grammar = GrammarStats()
    grammar.check("A string of text!")
    grammar.check("A string of text!")
    assert grammar.percentage_good() == 100

def test_percentage_good_one_entry_incorrect():
    grammar = GrammarStats()
    grammar.check("A string of text")
    assert grammar.percentage_good() == 0

def test_percentage_good_two_entries_incorrect():
    grammar = GrammarStats()
    grammar.check("A string of text")
    grammar.check("A string of text")
    assert grammar.percentage_good() == 0

def test_percentage_good_one_correct_one_incorrect():
    grammar = GrammarStats()
    grammar.check("A string of text!")
    grammar.check("A string of text")
    grammar.check("A string of text")
    assert grammar.percentage_good() == 33

    

