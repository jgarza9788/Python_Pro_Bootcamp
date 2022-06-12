
import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from clear_screen import clear

from art import logo, vs
from game_data import data


def choice_to_string(item):
    # print(item)
    return '{name}, {description}, {country}'.format(
        name=item['name'],
        description=item['description'],
        country=item['country']
    )

1
def main():

    print(logo)
    win_count = 0 
    d = data.copy()
    random.shuffle(d)
    A = d.pop()
    B = d.pop()
    
    while len(d) > 0:
        print(vs)

        players_pick = pyask.choose_one(
            choices=[choice_to_string(A),choice_to_string(B)]
            ,text='Who has more instragram followers?: ')
        
        if 0 and A['follower_count'] > B['follower_count']:
            print('Good Job')
            B = None
        elif 1 and A['follower_count'] < B['follower_count']:
            print('Good Job')
            A = B
            B = None
        else: 
            print('Sorry, better luck next time')
            break;

        try:
            B = d.pop()
        except:
            print('wow, you went through all the instagram accounts!')
            break;

        input('press enter for next round')
        clear()


if __name__ == '__main__':
    main()

    # d = data.copy()
    # random.shuffle(d)
    # A = d.pop()
    # print(choice_to_string(A))
    # print(type(choice_to_string(A)))