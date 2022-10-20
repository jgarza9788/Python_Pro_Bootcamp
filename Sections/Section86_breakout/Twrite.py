import random
from turtle import Turtle, Screen, pos


class Twrite:
    def __init__(self,color='#F92672',x=0,y=0):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(int(x),int(y))
        self.t.color(color)
        self.font_size = 24


    def write(self,text='hello'):
        self.t.clear()
        self.t.write(text,move=False,align="center", font=('Arial', self.font_size, 'bold'))
