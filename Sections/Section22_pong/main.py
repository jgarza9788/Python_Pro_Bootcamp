
# todo clean up some of this code

import math
import time
import random
# from Sections.Section22_pong.pong_classes import collision_x

# from pong_classes import GameState, Paddle, Ball, TWrite
from pong_classes import  Paddle, Twrite, Ball,collision,clamp

from turtle import Screen

game_state = 0 
# 0 = pre-game
# 1 = alive/playing
# 2 = dead

def get_screen():
    x = Screen()
    x.tracer(0)
    x.setup(width=800,height=600)
    x.bgcolor("#1f1f1f")
    x.title("Pong 🏓")

    return x

def get_minmaxY(scr):
    minY = scr.window_height()/-2
    maxY = scr.window_height()/2
    return minY,maxY

def get_minmaxX(scr):
    minX = scr.window_width()/-2
    maxX = scr.window_width()/2
    return minX,maxX


def increase_speed(i):
    i = i/25
    i = clamp(i,0.001,1.0)
    e =  1 - (1 - i) * (1 - i);
    return 0.05 - (0.04 * e)

def start_game():
    global game_state
    if game_state == 0:
        game_state = 1

def main():
    screen = get_screen()
    minY, maxY = get_minmaxY(screen)
    minX, maxX = get_minmaxX(screen)

    tw = Twrite(color='#888888',y=-100)
    tw.font_size = 200
    tw.write('{0} : {1}'.format(0,0))

    itw = Twrite(color='#555555',y=(maxY-30))
    itw.font_size = 12
    itw.write('P1: use \'a\' & \'z\'  | P2: use 🔼 & 🔽')

    mtw = Twrite(color='#ff0000',y=(minY+30))
    mtw.font_size = 12
    mtw.write('press enter to start game')
    

    p1 = Paddle(minY=minY,maxY=maxY)
    p2 = Paddle(x=350,minY=minY,maxY=maxY)
    ball = Ball()

    paddle_bounce_count = 0
    sleep = 0.05

    screen.listen()
    screen.onkeypress(key='Up',fun=p2.up)
    screen.onkeypress(key='Down',fun=p2.down)
    screen.onkeypress(key='a',fun=p1.up)
    screen.onkeypress(key='z',fun=p1.down)
    screen.onkeypress(key='Return',fun=start_game)

    while game_state == 0:
        time.sleep(0.1)
        mtw.write('press enter to start game')
    
    for i in range(5,0,-1):
        mtw.write('game will start in {0} seconds'.format(i))
        time.sleep(1)

    while game_state == 1:
        p1.move()
        p2.move()
        ball.move()

        mtw.write('')

        if ball.hit_right():
            ball.reset()
            p2.score += 1
            tw.write('{0} : {1}'.format(p1.score,p2.score))
            screen.update()
            for i in range(3,0,-1):
                mtw.write('game will start in {0} seconds'.format(i))
                time.sleep(1)

            # ball.change_x_dir()

        if ball.hit_left():
            ball.reset()
            p1.score += 1
            tw.write('{0} : {1}'.format(p1.score,p2.score))
            screen.update()
            for i in range(3,0,-1):
                mtw.write('game will start in {0} seconds'.format(i))
                time.sleep(1)

            # ball.change_x_dir()

        if math.fabs(ball.t.pos()[0]) > (maxX*0.75):
            if collision(p1.get_all_positions(),ball.t.pos()):
                ball.change_x_dir()
                paddle_bounce_count += 1
            elif collision(p2.get_all_positions(),ball.t.pos()):
                ball.change_x_dir()
                paddle_bounce_count += 1

        screen.update()
        sleep = increase_speed(paddle_bounce_count)
        time.sleep(sleep)


        print("sleep: {0}\nball dir: {1}\nball angle: {2}\n".format(sleep,ball.dir,ball.get_angle()),end='\r')


    screen.exitonclick()

if __name__ == '__main__':
    main()