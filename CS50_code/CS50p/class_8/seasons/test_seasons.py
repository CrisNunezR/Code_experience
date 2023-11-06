"""
implement, in a file called test_seasons.py,
one or more functions that test your implementation
of any functions besides main in seasons.py thoroughly,
each of whose names should begin with test_ so that you can
execute your tests with:

pytest test_seasons.py
"""

from datetime import date
from seasons import get_date, calculate_minutes, number_to_words
import pytest


#get_date receives a str date and extracts year, month and day as strings
def test_get_date():
    test_date = "1998-08-21"
    assert get_date(test_date) == ('1998', '08', '21')
    test_date = "2020-12-02"
    assert get_date(test_date) == ('2020', '12', '02')
    with pytest.raises(ValueError):
        get_date(r"January second, 2022")
    with pytest.raises(ValueError):
        get_date(r"January 1, 2022")
    with pytest.raises(ValueError):
        get_date(r"2022/12/30")
    with pytest.raises(ValueError):
        get_date(r"2022-30-12")

def test_calculate_minutes():
    year, month, day = '1999', '01', '01'
    today_midnight = date(int('2000'), int('01'), int('01'))
    assert calculate_minutes(year, month, day, today_midnight) == 525600

    year, month, day = '1999', '12', '31'
    today_midnight = date(int('2000'), int('01'), int('01'))
    assert calculate_minutes(year, month, day, today_midnight) == 1440


def test_int_to_word():
    assert number_to_words(10) == "Ten"
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert number_to_words(526) == "Five hundred twenty-six"
