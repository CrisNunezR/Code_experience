"""
implement a program in Python that prompts
the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods).
"""

def main():
    _ = input("Please enter a text: ")
    print(_.replace(" ", "..."))

main()