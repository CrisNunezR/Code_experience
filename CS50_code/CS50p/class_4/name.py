#using sys.argv to retreive elements from the prompt

import sys

#print("hello, my name is", sys.argv[1])

#notice that the content of argv is:
    #argv[0] = name of the file being executed
    #argv[1] = what ever variables are entered after the file name

#To control the cases where the use forgets to include a required variable in the prompt we can:

#1: use try-except
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Use a name in the prompt after the file name")

#2: use an if statement that controls the length of the argv array
if len(sys.argv) < 2:
    print("Use a name in the prompt after the file name")
else:
    print("hello, my name is", sys.argv[1])

#3: use if with a sys.exit instead of putting the relevant code on the 'else' clause
if len(sys.argv) < 2:
    sys.exit("Use a name in the prompt after the file name")

print("hello, my name is", sys.argv[1])
#Notice that this code is ‘cleaner’ since it does not ‘hide’ the actual relevant code behind an ‘else’


