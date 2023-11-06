"""
in a file called lines.py, implement a program that expects
exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments
and blank lines. If the user does not specify exactly one command-line
argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead
exit via sys.exit.

Assume that any line that starts with #, optionally preceded
by whitespace, is a comment. (A docstring should not be considered
a comment.) Assume that any line that only contains whitespace is blank.
"""
import sys


def main():

    #checks number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    #checks if python file
    if ends_in_py(file_path) == False:
        sys.exit("Not a Python file")

    #checks if file exists
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        sys.exit("File does not exist")

    #returns the number of lines
    print(count_text_lines(file_path))


#checks last 3 chars == '.py'
def ends_in_py(file: str) -> bool:
    last_3 = file[-3:]
    return last_3 == '.py'

#count lines
def count_text_lines(file: str) -> int:
    counter = 0
    with open(file, 'r') as file:
        for line in file:
            if not line.lstrip().startswith("#") and line.lstrip() != "":
                counter += 1

    return counter

if __name__ == "__main__":
    main()