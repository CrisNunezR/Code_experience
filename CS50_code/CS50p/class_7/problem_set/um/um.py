"""
In a file called um.py, implement a function called
count that expects a line of text as input as a str
and returns, as an int, the number of times that “um”
appears in that text, case-insensitively, as a word unto itself,
not as a substring of some other word. For instance, given
text like hello, um, world, the function should return 1.

Given text like yummy, though, the function should return 0.

Structure um.py as follows, wherein you’re welcome to modify
main and/or implement other functions as you see fit, but you
may not import any other libraries. You’re welcome, but not
required, to use re and/or sys.
"""


import re
import sys


def main():
    while True:
        str_ = input("Text: ").strip()

        if len(str_) >= 0:
            try:
                print(count(str_))
            except ValueError:
                sys.exit('ValueError')
            else:
                break
        else:
            raise ValueError

def count(s):
    sequences = [r"^um.?$", r"^um[.,;?! ]", r" um ", r" um[.,;!]+", r"[^\s]um[.,;]+ ", r"[^ ]um\.\.\.", r"um;"]

    unique_matches = set()

    for seq in sequences:
        matches = re.findall(seq, s, re.IGNORECASE)
        #print(matches)
        unique_matches.update(matches)

    return len(unique_matches)



if __name__ == "__main__":
    main()