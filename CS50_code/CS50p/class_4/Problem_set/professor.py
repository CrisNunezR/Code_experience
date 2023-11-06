"""
In a file called professor.py, implement a program that:

Prompts the user for a level, n. If the user does not input
1, 2, or 3, the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with digits.

No need to support operations other than addition (+).

Prompts the user to solve each of those problems.
If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem.

If the user has still not answered correctly after three tries,
the program should output the correct answer.
The program should ultimately output the user’s score:
the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts
(and, if need be, re-prompts) the user for a level and returns
1, 2, or 3, and generate_integer returns a randomly generated
non-negative integer with level digits or raises a ValueError
if level is not 1, 2, or 3:

"""


#incorrect answer -> return EEE
#after 3 incorrect answers, return the correct answer

import random

def main():

    level = get_level()
    correct_ans = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        count = 0
        while True:
            try:
                ans = int(input(f"{a} + {b} = "))
            except:
                count +=1
                if count == 3:
                    print(f"{a} + {b} = {a+b}")
                    break
            else:
                if (ans != a + b):
                    print("EEE")
                    count += 1
                    if (count == 3):
                        print(f"{a} + {b} = {a+b}")
                        break
                else:
                    correct_ans += 1
                    break
    print(correct_ans)


def get_level() -> int:
    while True:
        try:
            n = int(input("Level: "))
        except:
            pass
        else:
            if n in [1,2,3]:
                return n

def generate_integer(level) -> int:
    match level:
        case 1:
            return (random.randint(0,9))
        case 2:
            return (random.randint(10,99))
        case 3:
            return (random.randint(100,999))





if __name__ == "__main__":
    main()