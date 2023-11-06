#define the functions for speller in python

#we just defined a "word" variable as a set which will contain the previous hash_table
words = set()

def check(words):
    if word.lower() in words:   #checking into lists is much easier!! converting to lower case is also easier
        return True
    else
        return False


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip()    #rstrip (reverse-strip) avoids including the \n at the end of the line in the file
        words.add(word)         #just add new words in dictionary to words set
                                #if I need the whole line, I can simply use: words.add(line)
    close(file)
    return True

def size()
    return len(words)           #python can easily return the length/nbr of elements in a set or dictionary

def unload():
    return true                 #python frees up memory by itself, no need to do it anymore