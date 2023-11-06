# TODO



def main():

    #height = int(input("Height: "))
    s = input("Height: ")

    if get_int(s) != None:
        height = get_int(s)
    else:
        s = input('Please enter only positive integers: ')
        height = get_int(s)

    if height > 8 or height < 1:
        s = input('Please enter values between 1 and 8: ')
        height = get_int(s)
    

    for i in range(height):
        print(" " * (height - i - 1), end = '')
        print("#" * (i+1))


def get_int(s):
    try:
        return int(s)
    except ValueError:
        return None

main()
