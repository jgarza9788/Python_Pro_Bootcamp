# note requires turtle
# pip install turtle

# https://docs.python.org/3/library/turtle.html


import os
import sys
# import random

# DIR = os.path.dirname(os.path.realpath(__file__))
# sys.path.append('\\'.join(DIR.split('\\')[:-2]))
# import pyask


from turtle import Turtle, Screen

t = Turtle()
forward_speed = 10 

def north():
    t.setheading(90)
    t.forward(forward_speed)

def south():
    t.setheading(-90)
    t.forward(forward_speed)

def east():
    t.setheading(0)
    t.forward(forward_speed)

def west():
    t.setheading(180)
    t.forward(forward_speed)

int_color = 0 
colors = [
            "#66D9EF",
            "#A6E22E",
            "#F92672",
            "#FD971F",
            "#AE81FF"
        ]
def next_color():
    global int_color
    int_color += 1
    t.color(colors[int_color % len(colors)])


def main():
    # t = Turtle()
    t.speed(0)
    t.width(5)
    # t.color('red')
    next_color()

    screen = Screen()
    screen.bgcolor("#1f1f1f")

    screen.listen()
    screen.onkeypress(key='Up',fun=north)
    screen.onkeypress(key='Down',fun=south)
    screen.onkeypress(key='Right',fun=east)
    screen.onkeypress(key='Left',fun=west)
    screen.onkeypress(key='c',fun=next_color)
    # screen.onkeypress(key='Right',fun=west)



    screen.exitonclick()

if __name__ == '__main__':
    main()