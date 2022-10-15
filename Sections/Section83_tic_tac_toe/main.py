# tic tac toe

import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

import nerdfonts as nf
from termcolor import colored


class tictactoe:
    def __init__(self):

        self.empty_color = 'cyan'
        self.x_color = 'red'
        self.o_color = 'green'

        self.board = list(range(0,9))

        self.chars = [ 
            colored ( nf.icons['fae_thin_close'], color=self.x_color ),
            colored ( nf.icons['fa_circle_o'], color=self.o_color ),
            ]
        self.turn_int = 0 
        self.over = False
    
    def show_board(self):
        # print(self.board[0:3])
        cb = [ colored(str(i),self.empty_color) for i in self.board]
        for i in range(3,12,3):
            # print(i)
            print(*cb[i-3:i])

    def show_board_debug(self):
        for index, i in enumerate(self.board):
            print(index,i)
    
    def update_board(self,player_char,pick):

        try:
            if type(self.board[pick]) == int:
                self.board[pick] = player_char
                return True
            else: 
                return False
        except:
            return False

    def did_win(self,player_char):
        result = False

        b = self.board.copy()

        if b[0] == player_char and \
            b[1] == player_char and \
            b[2] == player_char:
            result = True
        if b[3] == player_char and \
            b[4] == player_char and \
            b[5] == player_char:
            result = True
        if b[6] == player_char and \
            b[7] == player_char and \
            b[8] == player_char:
            result = True
        if b[0] == player_char and \
            b[3] == player_char and \
            b[6] == player_char:
            result = True
        if b[1] == player_char and \
            b[4] == player_char and \
            b[7] == player_char:
            result = True
        if b[2] == player_char and \
            b[5] == player_char and \
            b[8] == player_char:
            result = True
        if b[0] == player_char and \
            b[4] == player_char and \
            b[8] == player_char:
            result = True
        if b[2] == player_char and \
            b[4] == player_char and \
            b[6] == player_char:
            result = True
        return result


    def spaces_left(self):   

        num_count  = 0
        for x in self.board:
            if type(x) == int:
                num_count += 1
        return num_count


    def turn(self):
        turn_successful = False
        while turn_successful == False:


            p = self.chars[self.turn_int % 2]
            print(p, '\'s Turn ... ')
            print('please, pick a number')
            self.show_board()
            # self.show_board_debug()

            pick = pyask.ask_question('',int)

            turn_successful = self.update_board(p,pick)
            
            print()
            if turn_successful:
                won = self.did_win(p)
                self.turn_int += 1

                if won == True:
                    self.over = True
                    return p

                if self.spaces_left() == 0:
                    self.over = True
                    return None

            else:
                print('#'*10)
                print('*** can\'t move there | try again ***')


    def play(self):
        x = None
        while self.over == False:
            x = self.turn()
        
        print()
        self.show_board()
        print( '*'*5 ,str(x), 'WON!', '*'*5)





def main():

    print("""OXOX TIC TAC TOE OXOX \n\n""")

    new_game = 'Yes'

    while new_game == 'Yes':

        ttt = tictactoe()
        ttt.play()
        # ttt.show_board()
        # print(ttt.board)

        new_game = pyask.choose_one(['No','Yes'], 'New Game?')
        print(new_game)

if  __name__ == '__main__':
    main()

