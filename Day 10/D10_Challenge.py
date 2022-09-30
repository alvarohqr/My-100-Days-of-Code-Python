import os
os.system('cls' if os.name == 'nt' else 'clear')
from art import logo

'''Calculator program
    1) Enter a number
    2) Enter a operator
    3) Enter a second number
    4) Calculate the result
    5) Type 'y' to continue calculating with the result or type
        'n' to start a new calculation:
'''
print(logo)

def operations(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b
    elif op == '^':
        return a ** b
    else:
        return 'Pick a valid operator!\n'
 

def Calculator():
    keep_going = True

    while keep_going:
        n1 = float(input("What's the first number?: "))
        print('+\n-\n*\n/\n%\n^')
        op = input('Pick an operation: ')
        n2 = float(input("What's the next number?: "))
        result = operations(n1,n2,op)
        
        print(f"{n1} {op} {n2} = {result}")
        
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        
        if cont == 'n':
            keep_going = False
            os.system('cls')
            Calculator()       
        elif cont == 'y':
            n1 = result
            '''
            op = input('Pick an operation: ')
            n2 = float(input("What's the next number?: "))
            result = Calculator(n1, n2, op)
            print(f"{n1} {op} {n2} = {result}")
            cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
            '''
        
Calculator()