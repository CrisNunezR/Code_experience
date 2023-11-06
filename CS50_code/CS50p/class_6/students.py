"""
we use this code to train working with csv files

"""


#notice that I don't need 'r' since it's the default value for open

"""
with open("students.csv","r") as file:
    for line in file:
        name, apt = line.rstrip().split(",")
        print(f"{name} lives in {apt}")
"""

#rstrip() removes white spaces from a string
#split separates a string using a given value (in this case, a comma ',')
    #thus, we are passing 2 values to row, generating a list


"""
let's use the csv module of python to solve for a value like:
    caro, "dpto 502, providencia"
where the apartment string has a comma (,) which is the char I'm using to tell
the elements apart
"""


import csv

print("Using a regular list:")
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for name, apt in reader:
        print(f"{name} lives in {apt}")

print("\n")
#Using DictReader to import the data right into a Dictionary if the data has headers!!

import csv

students = []
print("Using dictionaries:")
with open("students_header.csv","r") as file:
    reader = csv.reader(file)
    for name, apt in reader:
        students.append({'name': name, 'address':apt})

for neighbor in sorted(students, key=lambda neighbor: neighbor['name']):
    print(f"{neighbor['name']} lives in {neighbor['address']}")

#writing a file using a dictionary (DictWriter):

import csv

name = input("What's your name? ")
address = input("what's your address? ")

with open("neighbours.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "address"])
    writer.writerow({'address':address, 'name': name})


