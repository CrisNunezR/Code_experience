"""
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:

the name of an existing CSV file to read as input, whose
columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns
should be, in order, first, last, and house.

Converts that input to that output, splitting each name
into a first name and last name. Assume that each student
will have both a first name and last name.
If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via sys.exit
with an error message.

"""

import sys
import csv


def main():

    #checks number of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    orig_path = sys.argv[1]
    outfile_path = sys.argv[2]

    #checks if csv file
    if not ends_in_csv(orig_path):
        sys.exit("Not a CSV file")

    #checks if file exists
    try:
        _ = open(orig_path, 'r')
    except FileNotFoundError:
        sys.exit(f"Could not read {orig_path}")

    #creates a list with names split
    students_fixed = [['first', 'last', 'house']]
    students = read_students(orig_path)
    for student in students:
        last, first = student['name'].split(',')
        students_fixed.append([first, last ,student['house']])

    #writes down a new csv file with split names
    write_csv(outfile_path, students_fixed)

    return 0


#checks last 4 chars == '.csv'
def ends_in_csv(file: str) -> bool:
    last_4 = file[-4:]
    return last_4 == '.csv'

#reads file into a list of dicts and returns it
def read_students(file: str) -> list:
    students = []
    with open(file, mode = 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})
    return students

#write csv file with data from a list
def write_csv(file: str, students: list):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile)

        for student in students:
            writer.writerow([student[0].strip(), student[1].strip(), student[2].strip()])


if __name__ == "__main__":
    main()