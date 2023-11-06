"""

Then, in a file called test_plates.py,
implement four or more functions that
collectively test your implementation
of is_valid thoroughly, each of whose
names should begin with test_ so that
 you can execute your tests with:

 pytest test_plates.py
"""

from plates import is_valid

def test_begins_2_letters():
   assert is_valid('33NNNN') == False
   assert is_valid('33') == False
   assert is_valid('NNNNNN') == True

def test_begin_with_0():
   assert is_valid('CS50P2') == False
   assert is_valid('DN320') == True
   assert is_valid('CS05') == False

def test_length_bt_2_and_6():
   assert is_valid('CS50') == True
   assert is_valid('H') == False

def test_length_bt_2_and_6_v2():
   assert is_valid('DN230') == True
   assert is_valid('OUTATIME') == False
   assert is_valid('NNNNNNN') == False

def test_no_puctuation_marks():
   assert is_valid('34DN12!') == False
   assert is_valid('PI3.14') == False
   assert is_valid('?DN230') == False

def test_numbers_at_end():
   assert is_valid('34DN12') == False
   assert is_valid('DN12') == True

#validate 2 first chars are letters

#validates length of plate between 6 and 2, both inclusive
#validates no puntuation marks in plate
#checks that numbers come only at the end and don't begin with '0'



if __name__ == "__main__":
    main()