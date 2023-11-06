"""
In plates.py, implement a program that prompts the user
for a vanity plate and then output Valid if meets all of
the requirements or Invalid if it does not. Assume that any
letters in the user’s input will be uppercase.

Structure your program per the below, wherein is_valid returns
True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional
functions for is_valid to call (e.g., one function per requirement).

requirements:
    -plate must start with at least two letters
    -plate contains a maximum of 6 and min of 2 characters
    -Numbers cannot be used in the middle of a plate; they must come at the end
    -No periods, spaces, or punctuation marks are allowed
"""



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#executes all validations
def is_valid(plate: str) -> bool:
    if starts_2_letters(plate) and \
    check_len(plate) and \
    chech_punct(plate) and \
    check_nbr(plate):
        return True
    else:
        return False



#validate 2 first chars are letters
def starts_2_letters(s: str) -> bool:
    first_2 = s[:2]
    return first_2.isalpha()

#validates length of plate between 6 and 2, both inclusive
def check_len(s: str) -> bool:
    if 1 < len(s) < 7:
        return True
    else:
        return False

#validates no puntuation marks in plate
def chech_punct(s: str) -> bool:
    for chr in s:
        if chr in ['.', ',', ' ', '/']:
            return False
    return True

#checks that numbers come only at the end and don't begin with '0'
def check_nbr(s: str) -> bool:
    begin_nbr = False

    for chr in s:
        if chr.isnumeric():
            if begin_nbr == False: #this is the 1st numeric char in plate
                begin_nbr = True
                if int(chr) == 0:
                    return False
        elif begin_nbr == True:
                return False #there is a letter after a number

    return True


main()