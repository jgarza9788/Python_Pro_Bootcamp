
import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
# print(sys.path)

import pyask


def roll(d):
    return random.randint(1,d)

def roll_d6():
    return roll(6)

def roll_d20():
    return roll(20)

def roll_d12():
    return roll(12)

def roll_d10():
    return roll(10)

def roll_d8():
    return roll(8)

def roll_d4():
    return roll(4)


print("""
        ,     \    /      ,        
       / \    )\__/(     / \       
      /   \  (_\  /_)   /   \      
 ____/_____\__\@  @/___/_____\____ 
|             |\../|              |
|              \VV/               |
|       dragons_and_pythons       |
|_________________________________|
 |    /\ /      \\       \ /\    | 
 |  /   V        ))       V   \  | 
 |/     `       //        '     \| 
 `              V                '
""")

print("Welcome to dragons_and_pythons")

all_decisions = []

choices = ['money','power','women']
item = pyask.choose_one(choices,'Why are you on a quest?')
all_decisions.append(item)

print(f'you are on a quest for {item} !')

print('\n***Lets Start Your Quest***\n')

def quest_for_money():
    #todo finish this part
    pass

def quest_for_power():
    print('In town you hear a rumor about a hammer that no one can lift.')
    print('You journey across the land and find the hammer.')
    input('press enter to roll a D20 for strength check.\n\t15 or more to lift the hammer.')
    strength = roll_d20()
    print('strength: ',strength)

    if strength < 15:
        print('you try to lift the hammer, but your back gives out and you die 💀')
        print_skull()
        return None
    else:
        print('you lift the hammer and the whole crowd cheers!')
        print('...but thor comes down, whips your ass and then you die 💀')
        print_skull()
        return None


def quest_for_women():
    print('while in town you see the girl of your dreams 😍')
    input('press enter to roll a D6 for a charm check.')
    charm = roll_d6()
    print('charm: ',charm)

    if charm > 2:
        print('you both fall in love ♥ ♥ ♥')
        print('... but she\'s a dirty pirate hooker')
        print('your dick falls off and you die 💀')
        print_skull()
        return None
    else:
        print('you get rejected 💔')
        print('you live the rest of your life alone, then you die 💀')
        print_skull()
        return None


def print_skull():
    print("""

  _____
 /     \\
| () () |
 \  ^  /
  |||||
  |||||

        """)

if item == 'money':
    quest_for_money()
elif item == 'power':
    quest_for_power()
elif item == 'women':
    quest_for_women()