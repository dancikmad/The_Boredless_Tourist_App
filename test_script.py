import pytest
from script import add_attraction, find_attractions, get_attractions_for_traveler, attractionssc

# Additional test cases for the script module
def test_add_attraction():
    add_attraction("Paris, France", ["Eiffel Tower", ["landmark", "viewing deck"]])
    assert attractions[0] == [["the Louvre", ["art", "museum"]],
                               ["Arc de Triomphe", ["historical site", "monument"]],
                               ["Eiffel Tower", ["landmark", "viewing deck"]]]
    
def test_find_attractions():
    assert find_attractions("Shanghai, China", ["garden"]) == ["Yu Garden"]
    assert find_attractions("Los Angeles, USA", ["art"]) == ["LACMA"]
    assert find_attractions("Cairo, Egypt", ["historical site", "museum"]) == ["Pyramids of Giza", "Egyptian Museum"]
    
def test_get_attractions_for_traveler():
    traveler = ["John Doe", "São Paulo, Brazil", ["zoo", "historical site"]]
    assert get_attractions_for_traveler(traveler) == "Hi John Doe, we think you'll like these places around São Paulo, Brazil: the São Paulo Zoo, the Pátio do Colégio."
