"""
In a file called test_twttr.py,
implement one or more functions that collectively
test your implementation of shorten thoroughly,
 each of whose names should begin with test_
 so that you can execute your tests with

 pytest test_twttr.py
"""
from twttr import shorten

def test_upper():
    assert shorten("AEIOU") == ""
    assert shorten("HI") == "H"

def test_lower():
    assert shorten("aeiou") == ""
    assert shorten("Hi") == "H"

def test_nonletters():
    assert shorten("@%£%@£") == "@%£%@£"
    assert shorten("@%£e%@a£u") == "@%£%@£"

def test_numbers():
    assert shorten("1234ea") == "1234"
    assert shorten("0000") == "0000"

def test_punctuation():
    assert shorten("hello, there") == "hll, thr"


if __name__ == "__main__":
    main()