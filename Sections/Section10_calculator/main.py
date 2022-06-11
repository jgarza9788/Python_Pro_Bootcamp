import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from art import logo

op_options = ['+','-','*','/','quit']

def add(A,B):
    return A + B

def subtract(A,B):
    return A - B

def multiply(A,B):
    return A * B

def divide(A,B):
    return A / B

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def main():
    print(logo)
    N = pyask.ask_question('What\'s the first number?: ',float)

    while True:
        op = pyask.choose_one(op_options,'Pick an operations:')

        if op == 'quit':
            print('👋 bye ')
            break;

        NN = pyask.ask_question('What\'s the second number?: ',float)

        print('{0} {1} {2} = '.format(N,op,NN))

        N = operations[op](N,NN)
        
        print('answer >> ',N)



if __name__ == "__main__":
    main()