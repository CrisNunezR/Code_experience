"""
In a file called game.py, implement a program that:

Prompts the user for a level, n.
If the user does not input a positive integer, the program should prompt again.

Randomly generates an integer between 1 and n, inclusive, using the random module.

Prompts the user to guess that integer.
If the guess is not a positive integer, the program should prompt the user again.

If the guess is smaller than that integer,
the program should output Too small! and prompt the user again.
If the guess is larger than that integer,
the program should output Too large! and prompt the user again.
If the guess is the same as that integer,
the program should output Just right! and exit.
"""

import random

def main():

    #controls the input value
    while True:
        try:
            n_ = int(input("Level: "))
        except ValueError:
            #print("Input only positive integers")
            pass #instruction requires doing nothing instead of returning a warning
        else:
            if n_ < 1:
                #print("Input only positive integers")
                pass #instruction requires doing nothing instead of returning a warning
            else:
                break #instruction requires doing nothing instead of returning a warning

    n = random.choice(range(1,n_ + 1))

    #print(n)

    #control the guessed value
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            #print("input only positive integers")
            pass #instruction requires doing nothing instead of returning a warning
        else:
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                break




if __name__ == "__main__":
    main()