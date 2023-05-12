from lib.counter import *
def test_counter_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_correct_result():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_add_multiples():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."