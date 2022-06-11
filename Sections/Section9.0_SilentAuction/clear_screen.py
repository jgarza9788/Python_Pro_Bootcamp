


# import only system from os
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



if __name__ == "__main__":
    #test 
    print('hello '* 100 )
    clear()
    print('hello, is it me your look for?')