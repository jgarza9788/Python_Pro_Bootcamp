# note requires turtle
# pip install turtle

# https://docs.python.org/3/library/turtle.html


import os
import sys
import random
import turtle

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


from turtle import Turtle, Screen,numinput,textinput

# t = Turtle()
# forward_speed = 10 

# def north():
#     t.setheading(90)
#     t.forward(forward_speed)

# def south():
#     t.setheading(-90)
#     t.forward(forward_speed)

# def east():
#     t.setheading(0)
#     t.forward(forward_speed)

# def west():
#     t.setheading(180)
#     t.forward(forward_speed)

# int_color = 0 

# def next_color():
#     global int_color
#     int_color += 1
#     t.color(colors[int_color % len(colors)])


def turtle_factory(number,colors):
    result = []

    for i in range(number):
        t = Turtle()
        t.shape("turtle")
        t.up()
        t.color(colors[i % len(colors)])
        t.goto(-450,((50*number)/2) - (50*i))
        t.down()
        t.width(5)
        result.append(t)
    
    return result


def main():

    screen = Screen()
    screen.setup(width=1000,height=1000)
    screen.bgcolor("#1f1f1f")

    colors = [
            "#66D9EF",
            "#A6E22E",
            "#F92672",
            "#FD971F",
            "#AE81FF"
        ]
    # colors = [
    #     "#ff0000",
    #     "#00ff00",
    #     "#0000ff",
    #     "#ffff00",
    #     "#ff00ff"
    # ]

    turtle_count = 5

    tl = ''
    for i in range(turtle_count):
        tl += str(i) + ','

    bet = numinput('pick a turtle',tl,minval=0,maxval=4)

    t = turtle_factory(turtle_count,colors)

    finished = False
    while finished == False:
        t_num = random.randint(0,turtle_count-1)
        x = t[t_num]
        x.forward(random.randint(1,10))

        if x.pos()[0] >= 450:
            # x.goto(0,0)
            x.circle(50)
            x.circle(75)
            x.circle(35)

            if bet == t_num:
                textinput("WIN", "your turtle won!")
            else:
                textinput("Sorry", "your turtle lost")

            finished = True
            print(x.color())

    screen.exitonclick()

if __name__ == '__main__':
    main()