
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
    print('There is a dragon\'s cave that no one dare ventures to.')
    print('everyone knows dragons keep a hoard of gold, but few have the guts to slay the dragon for it.')
    print('You visit your local store to pick up some items.')
    print('but when it comes to a weapon you could only carry one, due to the long journey.')
    weapons = ['sword','axe','spear']
    weapon = pyask.choose_one(weapons,'what do you pick?')
    all_decisions.append(weapon)

    print(f'\"oh this is a lucky {weapon}\" the shopkeeper tells you')

    print('after days of traveling you get close to the cave.')
    rest_choices = ['yes','no']
    rest = pyask.choose_one(rest_choices,'do you need a rest?')
    all_decisions.append(rest)

    if rest == 'no':
        print('there is no time to rest, you decide to enter the cave now')
    elif rest == 'yes':
        print('you make camp down wind from the cave, and prepare for the tomorrow when you slay the dragon')

    print('as you enter the cave you can smell the soot and ash from the dragon\'s breath')
    print(f'you take out your {weapon}, because you know you\'ll come face to face with the dragon soon')
    print('THERE, you spot some eyes glowing in the dark.')
    print('the dragon lunges at you')
    print('with only moments to spare you were able to block the attack')

    #todo finish out these later ...boring work :/
    if weapon == 'axe' and rest == 'yes':
        print('')
        print('')
        print('')

    if weapon == 'axe' and rest == 'no':
        print('')
        print('')
        print('')
    if weapon == 'spear' and rest == 'yes':
        print('')
        print('')
        print('')

    if weapon == 'spear' and rest == 'no':
        print('')
        print('')
        print('')

    if weapon == 'sword' and rest == 'yes':
        print('')
        print('')
        print('')

    if weapon == 'sword' and rest == 'no':
        print('')
        print('')
        print('')


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