import pytest
from script import get_destination_index, get_traveler_location, test_traveler

# Testing the functions in script module
def test_get_destination_index():
    assert get_destination_index("Los Angeles, Usa") == 2
    assert get_destination_index("Paris, France") == 0
    
def test_get_traveler_location():
    assert get_traveler_location(test_traveler) == 1