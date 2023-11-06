"""
implement a program that prompts the user for a str
of text and then outputs that same text but with all
vowels (A, E, I, O, and U) omitted, whether inputted
in uppercase or lowercase.

"""

def rid_vowels(str_: str) -> str:
    str = ""
    for chr in str_:
        if chr not in ['a','e','i','o','u','A','E','I','O','U']:
            str = str + chr
    return str

def main():
    fixed_str = rid_vowels(input("Input: "))
    print(fixed_str)

main()