import os
import math
import time
import pandas as pd
from turtle import Turtle, Screen,textinput
import turtle


DIR = os.path.dirname(os.path.realpath(__file__))
BACKGROUND = os.path.join(DIR,"blank_states_img.gif")
uss = pd.read_csv(os.path.join(DIR,"50_states.csv"))
uss = uss.to_dict(orient='records')

scorelist = {i['state']:'🟥' for i in uss}
# print(scorelist)
# print(scorelist['California'])
# quit()
print(uss[:10])

class Twrite:
    def __init__(self,color='#000000',x=0,y=0):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(int(x),int(y))
        self.t.color(color)
        self.font_size = 12

    def write(self,text='hello'):
        # self.t.clear()
        self.t.write(text,move=False,align="center", font=('Arial', self.font_size, 'bold'))


def get_screen():
    x = Screen()
    x.setup(width=725,height=491)
    x.title("U.S. States ⭐⭐⭐⭐⭐🦅⭐⭐⭐⭐⭐")
    # x.tracer(0)
    print(BACKGROUND)
    x.addshape(BACKGROUND)
    turtle.shape(BACKGROUND)
    return x

# def get_mouse_click_coor(x,y):
#     print(x,y)



def main():

    screen = get_screen()
    # turtle.onscreenclick(get_mouse_click_coor)

    while True:
        answer = textinput('Guess The State','What\'s Another States Name?:\n\'QUIT\' to quit')
        try:
            answer = answer.strip().upper()
            for i in uss:
                if i['state'].upper() == answer:
                    nt = Twrite(x=i['x'],y=i['y'])
                    nt.write(i['state'])
                    scorelist[i['state']] = '✅'
            
            if answer == 'QUIT' or answer == 'EXIT':
                sf = os.path.join(DIR,'score.csv')
                # print(scorelist.keys())
                with open(sf,'w',encoding='utf-8') as f:
                    for k in list(scorelist.keys()):
                        print(k)
                        print(scorelist[k])
                        f.write( scorelist[k] + '\t' + k + '\n')
                print('saved: ',sf)
                turtle.bye()
        except Exception as e:
            print(str(e))
            time.sleep(1)
            pass    

        

    turtle.mainloop()


if __name__ == '__main__':
    main()