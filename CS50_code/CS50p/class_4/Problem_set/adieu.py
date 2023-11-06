"""
In a file called adieu.py, implement a program that prompts
the user for names, one per line, until the user inputs control-d.

Assume that the user will input at least one name. Then bid adieu
to those names, separating two names with one and, three names with
two commas and one and, and names with commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""


def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
            #names.append(input(""))
        except EOFError:
            break

    print("Adieu, adieu, to ", end = "")

    if len(names) <= 1:
        print(f"{names[0]}")
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]}")
    else:
        for idx in range(len(names)):
            if idx == len(names) - 1 and len(names) > 1:
                print(f"and {names[idx]}")
            else:
                print(f"{names[idx]}, ", end = "")


if __name__ == "__main__":
    main()
