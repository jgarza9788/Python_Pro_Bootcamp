
import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask

# from clear_screen import clear



from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

TF_map = {
    'Yes': True,
    'No': False
}

def main():
    M = Menu()
    CM = CoffeeMaker()
    MM = MoneyMachine()
    another_order = True

    while another_order:
        order = pyask.choose_one(choices=M.get_items().split('/')[:-1],text='What would you like to drink?: ')
        drink = M.find_drink(order)

        # drink.print_mi()

        if CM.is_resource_sufficient(drink) == False:
            print('sorry, we lack the resources to make your order')
        else:
            print('That would be ${0}.'.format(drink.cost))
            payment_complete = MM.make_payment(drink.cost)
            
        another_order = TF_map[pyask.choose_one(choices=['No','Yes'],text='Another Drink?: ')]
        


if __name__ == '__main__':
    main()

    # print([0,1,2,3,4][1::])

    # M = Menu()
    # print(M.get_items())
    # print(*M.get_items().split('/')[:-1],sep='\n')
    # print(type(M.get_items()))
    # main()