"""
In a file called fuel.py, reimplement Fuel Gauge f
rom Problem Set 3, restructuring your code per the below, wherein:

1) convert expects a str in X/Y format as input, wherein each of X and Y
is an integer, and returns that fraction as a percentage rounded to the
nearest int between 0 and 100, inclusive. If X and/or Y is not an integer,
or if X is greater than Y, then convert should raise a ValueError. If Y is 0,
then convert should raise a ZeroDivisionError.

2) gauge expects an int and returns a str that is:
    "E" if that int is less than or equal to 1,
    "F" if that int is greater than or equal to 99,
    and "Z%" otherwise, wherein Z is that same int.

"""

def main():
    frc = input("Fraction: ")

    while frc.find("/") < 0:
        frc = input("Fraction: ")

    while True:
        try:
            rem_fuel = convert(frc)
        except ValueError:
            frc = input("Fraction: ")
        except ZeroDivisionError:
            frc = input("Fraction: ")
        else:
            break


    print(gauge(rem_fuel))


def convert(frc:str) -> int:
    slash_loc = frc.find("/")

    while True:
        try:
            x, y = int(frc[:slash_loc]), int(frc[slash_loc + 1:])
            break
        except ValueError:
            raise

    while True:
        try:
            rem_fuel = x/y
        except ZeroDivisionError:
            raise
            #print('Y value needs to be > 0')
        except ValueError:
            raise
            #print("X and Y need to be integer values")
        else:
            if x > y:
                raise ValueError
            #if x == 100:
            #    raise ValueError
            break

    return round(rem_fuel*100,0)

def gauge(percentage: int) -> str:
    #returns remaning fuel as %
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()