
import math
import time
import random
from tkinter import W
from turtle import Screen


from TC_classes import *

game_state = 0 
# 0 = pre-game
# 1 = alive/playing
# 2 = dead

COLORS = [
            "#66D9EF",
            "#A6E22E",
            "#F92672",
            "#FD971F",
            "#AE81FF"
        ]

def get_screen():
    x = Screen()
    x.setup(width=600,height=600)
    x.bgcolor("#1f1f1f")
    x.title("Turtle Crossing 🐢")

    return x

def get_minmaxY(scr):
    minY = scr.window_height()/-2
    maxY = scr.window_height()/2
    return minY,maxY

def get_minmaxX(scr):
    minX = scr.window_width()/-2
    maxX = scr.window_width()/2
    return minX,maxX

def level_to_sleep(level):
    level = level/100
    level = clamp(level,0.01,1.0)
    e =  1 - (1 - level) * (1 - level);
    return 0.1 - (0.08 * e)

def start_game():
    global game_state
    if game_state == 0:
        game_state = 1

def main():
    global game_state

    screen = get_screen()
    screen.tracer(0)
    sleep = 0.1
    level = 1

    minY,maxY = get_minmaxY(screen)
    minX,maxX = get_minmaxX(screen)

    t = PlayerTurtle(
        minY=minY,
        maxY=maxY,
        minX=minX,
        maxX=maxX
        )


    trains = Trains(colors=COLORS,count=10)

    w = Twrite(color='#66D9EF',x=minX+10,y=maxY-25)
    w.font_size = 12
    w.write('Level: {0} ... Press Enter to Start'.format(level))

    screen.listen()
    screen.onkeypress(key='Up',fun=t.up)
    screen.onkeypress(key='Down',fun=t.down)
    screen.onkeypress(key='Right',fun=t.right)
    screen.onkeypress(key='Left',fun=t.left)
    screen.onkeypress(key='Return',fun=start_game)

    while game_state == 0:
        time.sleep(0.5)
        w.write('Level: {0} ... Press Enter to Start'.format(level))

    while game_state == 1:
        trains.move()
        w.write('Level: {0} '.format(level))
        time.sleep(sleep)
        sleep = level_to_sleep(level=level)
        screen.update()

        if t.won():
            level += 1
            t.reset()
            trains.increase_speed()
            trains.change_count()
        
        colide = False
        for train in trains.trains:
            if collision(train['t'].pos(),t.get_pos()):
                colide = True
                game_state = 2
                break;



    while game_state == 2:
        time.sleep(0.5)
        screen.update()
        w.write('Level: {0} ... Game Over'.format(level))

    screen.exitonclick()

if __name__ == '__main__':
    main()