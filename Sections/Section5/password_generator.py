
import os
from symtable import Symbol
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
# print(sys.path)

import pyask

print('Welcome to the PyPassword Generator!')


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z']

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', 
    ')', '*', '+', ',', '-', '.', '/', ':', 
    ';', '<', '=', '>', '?', '@', '[', '\\', 
    ']', '^', '_', '`', '{', '|', '}', '~'
    ]

numbers= [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

letter_count = pyask.ask_question('How may letters would you like in your password?',int)
symbols_count = pyask.ask_question('How may symbols would you like in your password?',int)
numbers_count = pyask.ask_question('How may numbers would you like in your password?',int)

pw_list = []
pw_list += random.choices(population=letters,k=letter_count)
pw_list += random.choices(population=symbols,k=symbols_count)
pw_list += random.choices(population=numbers,k=numbers_count)

random.shuffle(pw_list)
password = ''.join(pw_list)

print(password)

