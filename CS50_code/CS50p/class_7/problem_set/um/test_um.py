"""
Either before or after you implement count in um.py,
additionally implement, in a file called test_um.py,
three or more functions that collectively test your
implementation of count thoroughly, each of whose
names should begin with test_ so that you can execute your tests with:

pytest test_um.py

"""

from um import count
import pytest

def test_just_um():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('um.') == 1
    assert count('Um.') == 1
    assert count('Um...') == 1

def test_um_in_word():
    assert count('yum') == 0
    assert count('yummy') == 0
    assert count('hum') == 0

def test_three_points():
    assert count('Um...') == 1
    assert count('And there is, um..., something else') == 1
    assert count('Um, thanks, um...') == 2

def test_in_phrase():
    assert count('Um, hello, um, world...') == 2
    assert count('hello, um, world...') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2
