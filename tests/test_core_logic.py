#test_core_logic.py

# This file contains the tests for the core logic of the project. It will be used to test the functionality of the core logic.

from src.core_logic import *

def test_leap_year():
    assert leap_year(2000) == True
    assert leap_year(1900) == False
    assert leap_year(2004) == True
    assert leap_year(2001) == False