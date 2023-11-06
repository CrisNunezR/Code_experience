"""
This is simple code that we'll use to exercise
importing and testing from another code-file
"""

def main():
    x = int(input("x: "))
    print("x squared is", square(x))

def square(n):
    return n*n

if __name__ == "__main__":
    main()

