# note requires turtle
# pip install turtle

# https://docs.python.org/3/library/turtle.html


import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


from turtle import Turtle, Screen


def sun(t):
    t.begin_fill()
    t.speed(0)
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break;
    t.end_fill()

def square(t):
    # t.begin_fill()
    t.speed(0)
    while True:
        t.forward(200)
        t.left(90)
        if abs(t.pos()) < 1:
            break;
    # t.end_fill()

def main():
    ttt = Turtle()
    ttt.shape("turtle")
    # just using hex colors
    # timmy_the_turtle.color('red')
    # timmy_the_turtle.color('DodgerBlue')
    # timmy_the_turtle.color('#ff00ff') #hex colors
    ttt.color('#0000ff') #hex colors

    # sun(ttt)
    square(ttt)


    screen = Screen()
    screen.exitonclick()

if __name__ == '__main__':
    main()

