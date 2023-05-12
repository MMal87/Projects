from lib.gratitudes import *

def test_gratitudes_correct():
    gratitudes = Gratitudes()
    gratitudes.add("family of horses")
    result = gratitudes.format()
    assert result == "Be grateful for: family of horses"

def test_gratitudes_empty_list():
    gratitudes = Gratitudes()
    gratitudes.add("")
    result = gratitudes.format()
    assert result == "Be grateful for: "



# def test_gratitudes_boolean():
#     gratitudes = Gratitudes()
#     gratitudes.add(False)
#     result = gratitudes.format()
#     assert result == "Be grateful for: False"

