"""
training code for I/O functions

"""
#Open allows us to write to ('w') and read ('r') information from a file
#information in detail can be found in docs.python.org/3/library/functions.html#open

def non_pythonic():
    #using 'w' will always 'recreate' the file, which means erasing previous information
    #file = open("names.txt", "w")

    #we can also use 'a' (append) to add new information without erasing previous info
    file = open("names.txt", "a")

    while True:
        try:
            name = input("Enter a name: ")
        except EOFError:
            print("\n")
            break
        else:
            file.write(f"{name}\n")
    file.close()

"""
a more Pythonic way to handle files to write on them
is to use "with" instead of open-close

using "with" renders needless the use of close!

"""
def more_pythonic():

    with open("names.txt", "a") as file:
        while True:
            try:
                name = input("Enter a name: ")
            except EOFError:
                print("\n")
                break
            else:
                file.write(f"{name}\n")



#now we'll read the info from the text file
# notice that we need to 'remove' the \n characters
# also, when we open file, we automatically get a list
# with every line in the file as a new list (that's why we can do "for line in file")
def read_from_file():
    with open("names.txt", 'r') as file:
        for line in sorted(file):
            print("hello, ", line.rstrip())

"""
Notice that since file is already a list of lists (with every line in the text as a new list)
we dont need to do this:

    with open("names.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

#we can simply, as in the code, do this:
    with open("names.txt", 'r') as file:
        for line in file:
            print("hello, ", line.rstrip())
"""

if __name__ == "__main__":
    read_from_file()