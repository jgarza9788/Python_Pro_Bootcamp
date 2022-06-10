
import os
import sys
import random

from numpy import True_
from words import words

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
# print(sys.path)

import pyask


TITLE = """
    _                                                   
    | |                                                  
    | |__   __ _ _ __  _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \| '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                             __ / |                      
                            |___ /                   
    """

WORD = ''

DEBUG = False

GUESSED_LETTERS = []

WRONG_GUESS_COUNT = 0


BLANKS = ''

def pick_word():
    return random.choice(words).upper()

def debug_print():
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT
    if DEBUG:
        print()
        print('***debug_Print***')
        print('WORD: ',WORD)
        print('BLANKS: ',BLANKS)
        print('WRONG_GUESS_COUNT: ',WRONG_GUESS_COUNT)
        print('\\debug_Print\\')
        print()

def print_hangman():
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT

    hm = """
    +---+
    |   |
    1   |
   324  |
   56   |
        |
        |
==========
    """

    chars = [' ','O','|','/','\\','/','\\']

    for i in range(WRONG_GUESS_COUNT):
        i += 1
        hm = hm.replace(str(i), chars[i])
    
    for i in range(7):
        hm = hm.replace(str(i), chars[0])

    print(hm)

def update_blanks(letter):
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT

    result = False

    for i,l in enumerate(WORD):
        if l == letter:
            BLANKS = [x for x in BLANKS]
            BLANKS[i] = l
            BLANKS = ''.join(BLANKS)
            result = True
    
    return result

def WON():
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT

    return WORD == BLANKS

def LOST():
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT

    if WRONG_GUESS_COUNT >= 6:
        return True
    else:
        return False


def main():
    global DEBUG,WORD, BLANKS, WRONG_GUESS_COUNT

    print(TITLE)
    WORD = pick_word()
    BLANKS = '_'*len(WORD)

    while WON() == False and LOST() == False:
        debug_print()
        print('\n\n\n')

        print('WORD: ',BLANKS)
        print_hangman()
        letter = pyask.ask_for_letter('Guess a Letter: ',GUESSED_LETTERS).upper()

        GUESSED_LETTERS.append(letter)

        r = update_blanks(letter)
        if r == True:
            print('⭐⭐⭐ AWESOME ⭐⭐⭐')
        else:
            WRONG_GUESS_COUNT += 1
        
    print()
    if LOST():
        print('SORRY, you have ran out of turns 😥')
        print('the word was *',WORD,'*')
    elif WON():
        print('⭐⭐⭐ YOU WON ⭐⭐⭐')
        print('the word was *',WORD,'*')
    

if __name__ == '__main__':

    main()

    # BLANKS = '_xy__'
    # print(BLANKS)
    # BLANKS = [x for x in BLANKS]
    # BLANKS[3] = 'c'
    # print(BLANKS)


    