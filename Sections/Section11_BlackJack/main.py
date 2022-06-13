
import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from clear_screen import clear

from art import logo
from deck import deck


def sum_of_card(h):
    return sum(h['value'])

def hand_value(hand):
    result = 0
    hand.sort(key=sum_of_card)
    # print('sorted hand')
    # print(*hand,sep='\n')
    for card in hand:
        if len(card['value']) == 1:
            result += card['value'][0]
        else:
            if (result + card['value'][0]) > 21:
                result += card['value'][1]
            else:
                result += card['value'][0]
    
    return result


def print_hand(hand):
    for card in hand:
        print(' '*5,card['card'],card['value'])
        # print(' '.join(card['value']))

TF_map = {
    'Yes':True,
    'No':False
}

def print_players_hand(hand):
    print('Your Cards:')
    print_hand(hand)
    print(' '*5,'Total Value',hand_value(hand))
    print()

def main():
    
    print(logo)
    play_another = True

    while play_another:
        d = deck.copy()
        random.shuffle(d)

        players_hand = []
        dealers_hand = [] 

        players_hand.append(d.pop())
        players_hand.append(d.pop())

        dealers_hand.append(d.pop())
        dealers_hand.append(d.pop())

        print_players_hand(players_hand)

        print('Dealer\'s first Cards:')
        print_hand([dealers_hand[0]])
        # print('hand value',hand_value(dealers_hand))
        print()

        another_card = TF_map[pyask.choose_one(choices=['No','Yes'],text='Another card?')]

        while another_card :
            players_hand.append(d.pop())

            print_players_hand(players_hand)

            if hand_value(players_hand) >= 21:
                another_card = False
            else:
                another_card = TF_map[pyask.choose_one(choices=['No','Yes'],text='Another card?')]
            print()

        while hand_value(dealers_hand) < 17:
            dealers_hand.append(d.pop())

        players_score = 21 - hand_value(players_hand)
        dealers_score = 21 - hand_value(dealers_hand)

        if players_score < 0 and dealers_score >= 0:
            print('BUST {0}'.format(random.choice(['❌','😣','👎','😭','😢','💀'])))
        elif players_score == dealers_score:
            print('Draw')
        elif players_score < 0 and dealers_score < 0:
            print('Draw - Double BUST')
        elif dealers_score < 0:
            print('Dealer BUST, You Win {0}'.format(random.choice(['⭐','🤩','👍','😁','😎','😉'])))
        elif players_score < dealers_score:
            print('{0} You Win {0}'.format(random.choice(['⭐','🤩','👍','😁','😎','😉'])))
            print_players_hand(players_hand)
        else:
            print('Sorry, you lost {0}'.format(random.choice(['❌','😣','👎','😭','😢','💀'])))
            print_players_hand(players_hand)
            print('Dealer\'s hand:')
            print_hand(dealers_hand)
        print()

        play_another = TF_map[pyask.choose_one(choices=['No','Yes'],text='Play another round?')]
        clear()
        print('*** BLACK JACK ***')
    
    print('ended BLACK JACK...bye')




if __name__ == '__main__':
    main()
    


    #testing
    ######################

    # d = deck.copy()
    # random.shuffle(d)

    # xhand = []
    # xhand.append(d.pop())
    # xhand.append(d.pop())

    # # xhand.append({'value':[10]})
    # # xhand.append({'value':[2]})
    # # xhand.append({'value':[11,1]})

    # print(len(d))
    # print(len(xhand))
    # print(*xhand,sep='\n')
    # print(hand_value(xhand))

    # main()