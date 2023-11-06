text = "In the great green room"
words = text.split()

# Round 1
print("Round 1")
#for word in words:
#    print(word)
#print()

# Round 2
print("Round 2")
#for word in words:
#    for c in word:
#        print(c)
#print()

# Round 3
print("Round 3")
#for word in words:
#    if "g" in word:
#        print(word)
#print()

# Round 4
print("Round 4")
#for word in words[2:]:
#    print(word)
print()

# Round 5
print("Round 5")
#for word in words:
#    print("Goodnight Moon")
print()


######################################################################
#adding several dictionaries to a list by asking the user (input())

#defining a list
books = []

# Add three books to your shelf
#for i in range(3):
#    book = dict()   #each 'book; is a dict
#    book["title"] = input("Title: ")
#    book["author"] = input("Author: ")

#    books.append(book)     #adds a new 'book' (dict) to the list 'books'

# Print book titles
#for book in books:
#    print(book["title"])

#print(books)

######################################################################
#adding several dictionaries to a list by using a csv file (csv.reader module)

import csv      #adds the csv library of modules

books = []

#to read from a file we have 2 options
    #option 1: Using 'open' => we neen to close the file after using it
    #books_file = open('books.csv')
    #... #do something
    #close(books_file)

    #option 2: using with/open => file will be closed by python encoder then we finish the 'with indentation'
    #with open('books.csv') as books_file:
    # do something

#let's try using 'with':
with open('books.csv') as books_file:
    text = books_file.read()
    print(text)
    #we get just titles and authores printed out

#we can also try to create dictionaries for each title/author pair
with open('books.csv') as books_file:
    file_reader = csv.DictReader(books_file)
    for book in file_reader:
        books.append(book)

print(books)

