"""
In a file called interpreter.py, implement a program that prompts the user for an
arithmetic expression and then calculates and outputs the result as a floating-point
value formatted to one decimal place. Assume that the user’s input will be formatted
as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
"""

#notice that this code supports only 4 math operations "+, -, *, or /"
def locate_oper(str_: str) -> int:

    if str_.find("+") != -1:
        return str_.find("+")
    elif str_.find('-') != -1:
        return str_.find("-")
    elif str_.find('*') != -1:
        return str_.find("*")
    elif str_.find('/') != -1:
        return str_.find('/')
    else:
        return(-1)



def main():

    expr = input("Expression: ").replace(" ","")

    op_loc = locate_oper(expr)

    op = expr[op_loc:op_loc + 1]

    #print(expr)

    a = float(expr[:op_loc])
    b = float(expr[op_loc + 1: ])

    #print('a: ', a, 'b:',b)
    match op:
        case '+':
            print(round(a + b,1))
        case '-':
            print(round(a-b,1))
        case '*':
            print(round(a*b, 1))
        case '/':
            print(round(a/b,1))

main()