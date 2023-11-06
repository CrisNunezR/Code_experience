"""
Implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.

If, though, 1% or less remains, output E instead to indicate that
the tank is essentially empty. And if 99% or more remains, output
F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
instead prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.

"""


def main():
    frc = input("Fraction: ")

    while frc.find("/") < 0:
        frc = input("Fraction: ")

    slash_loc = frc.find("/")

    while True:
        try:
            x, y = int(frc[:slash_loc]), int(frc[slash_loc + 1:])
            break
        except ValueError:
            pass

    while True:
        try:
            rem_fuel = x/y
        except ZeroDivisionError:
            pass
            #print('Y value needs to be > 0')
        except ValueError:
            pass
            #print("X and Y need to be integer values")
        else:
            if x <= y:
                break

    #prints out remaning fuel as %
    if rem_fuel <= 0.01:
        print('E')
    elif rem_fuel >= 0.99:
        print('F')
    else:
        print(str(round(rem_fuel*100)) + '%')



"""
alternative more 'elegant' to execute instead of just main()
this basically says 'IF there IS a function main(), execute it...
this avoids an error when there is no function main()
"""
if __name__ == "__main__":
    main()

