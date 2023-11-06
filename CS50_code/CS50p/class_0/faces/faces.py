"""
In a file called faces.py, implement a function called convert
that accepts a str as input and returns that same input with any :)
converted to 🙂 (otherwise known as a slightly smiling face) and any
:( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts
the user for input, calls convert on that input, and prints the result.
You’re welcome, but not required, to prompt the user explicitly, as by
passing a str of your own as an argument to input. Be sure to call main
at the bottom of your file.

"""

"""
This code uses Unicode to create emojies
Notice that we can also install the emoji module/library (!pip install emoji)
and then use "import emoji" to print them
"""

def convert(emo: str):
    emo = emo.replace(":)", "\U0001F642")
    emo = emo.replace(":(", "\U0001F641")
    print(emo)

def main():
    convert(input("Please enter a text including emoticons: "))

main()