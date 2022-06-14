# note requires turtle
# pip install turtle

# https://docs.python.org/3/library/turtle.html


import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


from turtle import Turtle, Screen
import threading

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

def dashed_square(t):
    # t.begin_fill()
    t.speed(0)
    t.width(5)
    while True:

        pen_on = True
        for i in range(10):
            pen_on = (pen_on != True)
            
            if pen_on:
                t.down()
            else:
                t.up()
            t.forward(20)

        t.left(90)
        if abs(t.pos()) < 1:
            break;
    # t.end_fill()

def get_default_color_list():
    return [
            "#66D9EF",
            "#A6E22E",
            "#F92672",
            "#FD971F",
            "#AE81FF"
        ]

def n_gone(t,colors=None):

    if colors == None:
        colors = get_default_color_list()
    
    t.width(5)
    for i in range(3,11):
        # t.color(random.choice(colors))
        t.color(colors[i % len(colors)])

        for j in range(0,i):
            t.forward(75)
            t.right(360/i)

def random_walk(t,steps=1000, colors = None):
    if colors == None:
        colors = get_default_color_list()
    
    t.width(5)
    for i in range(steps):
        t.color(colors[i % len(colors)])
        t.left(45 * random.randint(1,8))
        t.forward(25)

    
def random_walk_multiturtle(count=10):
    for i in range(count):
        # random_walk(Turtle())
        tx = Turtle()
        tx.speed(0)
        tx.shape("turtle")

        x = threading.Thread(target=random_walk, args=(tx,50))
        x.start()

def spirograph(t,gap_size = 10,colors = None):
    if colors == None:
        colors = get_default_color_list()

    # turn = (3.14*2)/circle_count
    for i in range(int(360/gap_size)):
        t.color(colors[i % len(colors)])
        t.left(gap_size * i)
        t.circle(100)


def main():
    ttt = Turtle()
    ttt.speed(0)
    ttt.width(5)
    screen = Screen()
    screen.bgcolor("#1f1f1f")

    ttt.shape("turtle")
    # just using hex colors
    # timmy_the_turtle.color('red')
    # timmy_the_turtle.color('DodgerBlue')
    # timmy_the_turtle.color('#ff00ff') #hex colors
    # ttt.color('#0000ff') #hex colors

    # sun(ttt)
    # square(ttt)
    # dashed_square(ttt)

    # n_gone(ttt,colors=None)
    # random_walk(ttt)

    # random_walk_multiturtle(10)

    spirograph(ttt,10)

    screen.exitonclick()

if __name__ == '__main__':
    # x = True
    # for i in range(10):
    #     x = (x != True)
    #     print(x)

    main()

