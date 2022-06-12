import os
import sys
import random

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


from turtle import Turtle, Screen
import threading

def get_colors(image='hpainting.jpg'):
    image = os.path.join(DIR,image)
    import colorgram
    result = []
    for i in colorgram.extract(image, 20):
        cl = list(i.rgb)
        avgc = sum(cl)/3
        # print(cl)
        print(cl,i.rgb,avgc)

        if avgc < 225.0:
            result.append(i)
    return result

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def get_default_color_list():
    return [
            "#66D9EF",
            "#A6E22E",
            "#F92672",
            "#FD971F",
            "#AE81FF"
        ]

def main():
    ttt = Turtle()
    ttt.speed(0)
    ttt.width(5)
    # ttt.shape("turtle")
    # ttt.color('#ffffff')
    screen = Screen()
    # screen.bgcolor("#1f1f1f")
    # screen.bgcolor("#000000")

    ttt.up()

    # -+   ++
    #   
    # --   +-

    colors = get_colors()
    # colors = get_default_color_list()

    for i in range(-300,300,30):
        for j in range(-300,300,30):
            ttt.up()
            ttt.goto(i,j)
            ttt.down()

            nc = random.choice(colors).rgb
            ttt.color('#' + rgb_to_hex(nc))

            # ttt.color(random.choice(colors))

            ttt.begin_fill()
            ttt.circle(5)
            ttt.end_fill()


    screen.exitonclick()

if __name__ == '__main__':
    main()

    
