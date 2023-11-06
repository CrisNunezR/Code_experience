"""
In a file called pizza.py, implement a program that expects
exactly one command-line argument, the name (or path) of a
CSV file in Pinocchio’s format, and outputs a table formatted
as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.

notice the need to: pip import tabulate

Format the table using the library’s grid format. If the user does not
specify exactly one command-line argument, or if the specified file’s
name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit.

"""

import sys
import csv
from tabulate import tabulate

def main():

    #checks number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    #checks if csv file
    if ends_in_csv(file_path) == False:
        sys.exit("Not a CSV file")

    #checks if file exists
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        sys.exit("File does not exist")

    #prints table-formatted output]
    table_output(file_path)

#checks last 4 chars == '.csv'
def ends_in_csv(file: str) -> bool:
    last_4 = file[-4:]
    return last_4 == '.csv'

#reads csv file and prints table
def table_output(file: str):
    #print(tabulate(table, headers, tablefmt="grid"))
    with open(file, 'r') as file:
        table = csv.reader(file)

        #print(tabulate(table))
        print(tabulate(table, headers="firstrow", tablefmt="grid"))



if __name__ == "__main__":
    main()