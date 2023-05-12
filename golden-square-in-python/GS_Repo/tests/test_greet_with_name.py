from lib.greet import *


def test_greet_with_name():
    result = greet("Muniba")
    # Will return the output seen in terminal
    assert result == f"Hello, Muniba!"