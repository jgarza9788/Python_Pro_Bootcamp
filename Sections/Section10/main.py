import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from art import logo

operations = ['+','-','*','/']


def main():
    N = pyask.ask_question('What\'s the first number?: ',float)

    while True:
        op = pyask.choose_one(operations,'Pick an operations:')
        NN = pyask.ask_question('What\'s the second number?: ',float)

        print('{0} {1} {2}'.format(N,op,NN))

        if op == '+':
            N = N + NN
        elif op == '-':
            N = N - NN
        elif op == '*':
            N = N * NN
        elif op == '/':
            N = N / NN
        
        print(N)



if __name__ == "__main__":
    main()