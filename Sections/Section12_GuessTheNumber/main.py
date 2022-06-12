
import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


def get_guesses():
    difficulty = pyask.choose_one(['easy','hard'],'Choose a Difficulty:')
    result = 0
    if difficulty == 'easy':
        result = 10
    else:
        result = 5
    return result

def print_hint(N,gn):
    if N > gn:
        print('Too Low')
    elif N < gn:
        print('Too High')

def main():
    print('Welcome to the Number Guessing Game!')
    N = random.randint(1,100)
    print('I\'m Thinking of a number between 1 and 100')
    guesses = get_guesses()
    print('you have {0} guesses'.format(guesses))

    for g in range(1,guesses+1):
        print('{0} out of {1}'.format(g,guesses))
        gn = pyask.ask_question('Make a guess: ',int)
        print_hint(N,gn)
        if N == gn:
            print('***CORRECT***')
            break;
        
        if g == guesses:
            print('Sorry ...better luck next time')
        

if __name__ == '__main__':
    main()
    # print(list(range(1,6)))