"""
In a file called bank.py, reimplement Home Federal Savings Bank
from Problem Set 1, restructuring your code per the below,
wherein [function] value expects a str as input and returns 0
if that str starts with “hello”, 20 if that str
starts with an “h” (but not “hello”), or 100 otherwise,
treating the str case-insensitively.

You can assume that the string passed to the value
function will not contain any leading spaces.
Only main should call print.
"""

def value(greeting):

    grt = greeting.replace(" ", "").lower()
    if grt[:5] == "hello":
        return 0
    elif grt[:1] == "h":
        return 20
    else:
        return 100

def main():
    grt = input("Greeting: ")
    print(f"${value(grt)}")


if __name__ == "__main__":
    main()