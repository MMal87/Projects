from lib.artist_validator import ArtistParametersValidator
import pytest

"""With valid name and year 
it is valid"""
def test_is_valid():
    validator = ArtistParametersValidator("Test Artist", "Test Genre")
    assert validator.is_valid() == True


"""with blank or none name 
it is not valid"""
def test_is_not_valid_with_bad_name():
    validator = ArtistParametersValidator("", "Test Genre")
    assert validator.is_valid() == False
    validator_2 = ArtistParametersValidator(None, "")
    assert validator_2.is_valid() == False

def test_is_not_valid_with_bad_genre():
    validator = ArtistParametersValidator("Test Artist", "")
    assert validator.is_valid() == False
    validator_2 = ArtistParametersValidator("Test Artist", None)
    assert validator_2.is_valid() == False
    

"""with invalid parameters
produces ewrrors"""

def test_generate_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Artist name must not be blank",
        "Genre must not be blank"]
    validator_2 = ArtistParametersValidator("name", "")
    assert validator_2.generate_errors() == [
        "Genre must not be blank"]
    validator_3 = ArtistParametersValidator("", "Test Genre")
    assert validator_3.generate_errors() == [
        "Artist name must not be blank"]
    
def test_get_valid_name_if_name_valid():
    validator_1 = ArtistParametersValidator("Test name", "Test Genre")
    assert validator_1.get_valid_name() == "Test name"

    
def test_get_valid_name_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("", "Test Genre")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Cannot get valid name"



def test_get_valid_genre_if_genre_valid():
    validator_1 = ArtistParametersValidator("Title", "Test Genre")
    assert validator_1.get_valid_genre() == "Test Genre"

    
def test_get_valid_genre_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("Title", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"