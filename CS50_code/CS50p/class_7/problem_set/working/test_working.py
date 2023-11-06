"""

Either before or after you implement convert in working.py,
additionally implement, in a file called test_working.py,
three or more functions that collectively test your implementation
of convert thoroughly, each of whose names should begin with test_ so
that you can execute your tests with:

pytest test_working.py

"""

from working import convert
import pytest

def test_basic_format():
    assert convert(r"9 AM to 5 PM") == "09:00 to 17:00"
    assert convert(r"9 PM to 5 AM") == "21:00 to 05:00"
    assert convert(r"11 PM to 8 AM") == "23:00 to 08:00"

def test_min_format():
    assert convert(r"9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert(r"9:15 PM to 5 AM") == "21:15 to 05:00"

def test_night_shift():
    assert convert(r"10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert(r"5:25 PM to 8:50 AM") == "17:25 to 08:50"

def test_valueerror():
    with pytest.raises(ValueError):
        convert(r"13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert(r"9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert(r"09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert(r"9:60 AM to 5:60 PM")


