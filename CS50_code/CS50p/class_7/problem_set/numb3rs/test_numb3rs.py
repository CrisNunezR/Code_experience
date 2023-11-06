"""
implement, in a file called test_numb3rs.py,
two or more functions that collectively test
your implementation of validate thoroughly, each
of whose names should begin with test_ so that
you can execute your tests with:

pytest test_numb3rs.py
"""
from numb3rs import validate

def test_format():
    assert validate(r"1.1.2.3") == True
    assert validate(r"1") == False
    assert validate(r"1.1") == False
    assert validate(r"1.2.3") == False
    assert validate(r"0.0.120") == False
    assert validate(r"0.0.120.1") == True


def test_max():
    assert validate(r"255.255.255.255") == True
    assert validate(r"255.3.6.28") == True
    assert validate(r"1.3.6.28") == True

def test_min():
    assert validate(r"0.0.0.0") == True

def test_words():
    assert validate(r"cat") == False
    assert validate(r"0.0.cat.0") == False

def test_too_big():
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"275.3.6.28") == False
    assert validate(r"255.1999.6.28") == False
    assert validate(r"255.199.2999.28") == False
    assert validate(r"255.199.249.28999") == False

def test_wrong_chars():
    assert validate(r"1.3.@.28") == False
    assert validate(r"255.255.255.!") == False
    assert validate(r"255.255.255.") == False

def test_first_byte():
    assert validate(r"1.1.1.1") == True
    assert validate(r"257.1.1.1") == False
    assert validate(r"1.") == False
    assert validate(r"1.1.") == False
    assert validate(r"1.1.2") == False
    assert validate(r"1.1.2.2") == True

def test_range():
    assert validate(r"555.1.1.1") == False
    assert validate(r"1.555.1.1") == False
    assert validate(r"1.1.555.1") == False
    assert validate(r"1.1.1.555") == False
