"""
implement, in a file called test_jar.py, four or more functions
that collectively test your implementation of Jar thoroughly, each
of whose names should begin with test_ so that you can execute your tests with:

pytest test_jar.py

Note that it’s not as easy to test instance methods as it is to test functions alone,
since instance methods sometimes manipulate the same “state” (i.e., instance variables).
To test one method (e.g., withdraw), then, you might need to call another method first
(e.g., deposit). But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, as
with Python’s own mock object library, so that you can call just the one method but
 modify the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!
"""

import pytest
from jar import Jar

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12

def test_deposit():
    jar1 = Jar()

    jar1.deposit(3)
    assert jar1.size == 3

    jar1.deposit(9)
    assert jar1.size == 12

    with pytest.raises(ValueError):
        jar1.deposit(1)

def test_withdraw():
    jar1 = Jar()

    jar1.deposit(3)
    jar1.withdraw(1)
    assert jar1.size == 2




def test_str():
    jar1 = Jar()
    assert str(jar1) == ""

    jar1.deposit(3)
    assert str(jar1) == "🍪🍪🍪"

    jar1.deposit(8)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"




