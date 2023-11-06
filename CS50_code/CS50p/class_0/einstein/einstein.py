"""
implement a program in Python that prompts the user
for mass as an integer (in kilograms) and then outputs
the equivalent number of Joules as an integer. Assume
that the user will input an integer.
"""

def main():
    #m = int(input("Please enter an integer that represents the number of kg to convert: "))
    m = int(input("m: "))

    #this prints the energy in joules (by multiplying the mass in kgs
    # by the speed of light in meters per second)
    print("E: ", m*300000000**2)
    #print(m*300000000**2)

main()
