"""
in a file called test_bank.py,
implement three or more functions that
collectively test your implementation of
value thoroughly, each of whose names should
begin with test_ so that you can execute your tests with:

pytest test_bank.py
"""

from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_20():
    assert value("hi") == 20
    assert value("Hi, there") == 20
    assert value("How you diong?") == 20

def test_100():
    assert value("good day!") == 100
    assert value("what's up?") == 100


if __name__ == "__main__":
    main()