
"""
In a file called plates.py,
reimplement Vanity Plates from Problem Set 2,
restructuring your code per the below, wherein
is_valid still expects a str as input and returns
True if that str meets all requirements and False
if it does not, but main is only called if
the value of __name__ is "__main__":

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


if __name__ == "__main__":
    main()