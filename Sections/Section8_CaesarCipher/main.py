
import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class caesar_cipher:

    def __init__(self,shift=None,verbose=False):


        self.verbose = verbose
        if self.verbose:
            print(logo)
        
        if shift == None:
            self.__shift = pyask.ask_question('What is the shift number?:\n',int)
        else:
            self.__shift = shift
        
        self.history = []
        
    def encode(self,message=None):
        if message == None:
            message = pyask.ask_question('what is the message to encode?:\n',str)

        result = ''

        message = str(message).lower()

        for char in message:
            if char not in alphabet:
                result += char
            else:
                index = alphabet.index(char)
                index += self.__shift
                index = index % len(alphabet)
                result += alphabet[index]
            
        self.history.append({'action':'encoded','shift':self.__shift,'input':message,'output':result})

        return result

    def decode(self,message=None):
        if message == None:
            message = pyask.ask_question('what is the message to decode?:\n',str)
        result = ''

        message = str(message).lower()
        
        for char in message:
            if char not in alphabet:
                encoded_message += char
            else:
                index = alphabet.index(char)
                index += (self.__shift *-1)
                index = index % len(alphabet)
                result += alphabet[index]
            
        self.history.append({'action':'decode','shift':self.__shift,'input':message,'output':result})

        return result
    
    def print_history(self):
        for h in self.history:
            print(h)
    
    def change_shift(self,number=None):
        if number == None:
            number = pyask.ask_question('what number would you like to change shift to?:\n',int)

        old_shift = self.__shift
        self.__shift = number
        self.history.append({'action':'change_shift','input':number,'output':'updated'})
        print('{0} ==> {1}'.format(old_shift,self.__shift))



def main():
    cc = ceasar_cipher(shift=None,verbose=True)

    choice = ''
    choices = ['encode','decode','print history','change_shift','end']

    while choice != 'end':
        choice = pyask.choose_one(choices=choices,text='What would you like to do?:')    

        if choice == 'encode':
            print(cc.encode())
        elif choice == 'decode':
            print(cc.decode())
        elif choice == 'print history':
            cc.print_history()
        elif choice == 'change_shift':
            cc.change_shift()
        elif choice == 'quit':
            print('bye!')



if __name__ == "__main__":
    main()