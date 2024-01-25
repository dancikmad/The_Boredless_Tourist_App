import pytest
from script import get_destination_index

# Testing the functions in script module
def test_get_destination_index():
    assert get_destination_index("Los Angeles, Usa") == 2
    