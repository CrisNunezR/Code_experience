"""
This code will test the calculator code
"""

from calculator import square

def test_square():
    if square(2) != 4:
        print("error for square(2)")

    assert square(2) == 4

if __name__ == "__main__":
    main()

