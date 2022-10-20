import random
from turtle import Turtle, Screen, pos

def make_block(color='#66D9EF',x=0,y=0):
    b = Turtle()
    b.up()
    b.shape('square')
    b.goto(int(x),int(y))
    b.color(color)
    return b

