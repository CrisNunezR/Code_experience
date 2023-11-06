"""
in a file called test_fuel.py, implement two or more
functions that collectively test your implementations
of convert and gauge thoroughly, each of whose names
should begin with test_ so that you can execute your
tests with:

pytest test_fuel.py
"""

"""
:) input of 3/4 yields output of 75%
:) input of 1/3 yields output of 33%
:) input of 2/3 yields output of 67%
:) input of 5-10 results in reprompt
"""
from fuel import gauge
from fuel import convert
import pytest

#testing convert, which receives a string and returns an int
#with the str value bt 1 and 100
def test_convert_0():
    with pytest.raises(ZeroDivisionError) as excinfo:
        convert("2/0")

def test_no_int():
    with pytest.raises(ValueError) as excinfo:
        convert("2.4/5")
    with pytest.raises(ValueError) as excinfo:
        convert("2/5.5")
    with pytest.raises(ValueError) as excinfo:
        convert("tres/cuatro")

def test_x_greater_than_y():
    with pytest.raises(ValueError) as excinfo:
        convert("5/3")

def test_regular_perc():
    assert convert("3/4") == 75
    assert convert("80/100") == 80
    assert convert("2/3") == 67



#testing gauge: receives an integer in range[100] and returns a string "xx%"
def test_0():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_perc():
    f = 65
    assert gauge(f) == str(f)+"%"
    f = 55
    assert gauge(f) == str(f)+"%"
    f = 55
    assert gauge(f) == str(f)+"%"