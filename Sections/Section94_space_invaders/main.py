


import os
import math
import time
import random
from turtle import Turtle, Screen,textinput
import turtle

from Player import Player


from Twrite import Twrite
# from Blocks import make_block
# from Bar import Bar
# from Ball import Ball
from highscore_manager import highscore_manager as HM

DIR = os.path.dirname(os.path.realpath(__file__))

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
    x.title("Space Invaders 👽 - press enter to start")

    return x

# def score_to_sleep(score):
#     max_sleep = 0.075
#     min_sleep = 0.00005
#     sleep_diff = max_sleep - min_sleep
#     r = min([score/3300,1.0])
#     return max_sleep - ( sleep_diff * r )


def alien_new_speed(s):
    d = 10000 - s
    d = max([d,0])
    d = min([d,1])

    e = 1-(1-d)*(1-d)

    result = (e*1000 )+5


def get_distance(sp,fp):
    d = sp - fp
    return math.sqrt((d[0]*d[0])+(d[1]*d[1]))

def start_game():
    global game_state
    if game_state == 0:
        game_state = 1

def main():
    global game_state
    # game_state = -1 # for debugging

    screen = get_screen()
    screen.tracer(0)

    twrite = Twrite(color='#ffffff',x=0,y=( (screen.window_height()/2) - 50))
    twrite2 = Twrite(color='#ff0000',x=0,y=( (screen.window_height()/-2) + 20))
    # hswrite = Twrite(color='#666666',y=-100)

    aliens = []
    aliens_x_direction = 1
    alien_speed = 1
    alien_down_shift = 100
    for x in range(-300,300,50):
        for y in range(800 ,200,-50):
        # for y in range(1200  ,0,-50):
        # for y in range(625,0,-50):
                a = Turtle()
                a.up()
                a.shape('square')
                a.goto(int(x),int(y))
                a.color('#A6E22E')
                aliens.append(a)
    
    # bar = Bar()
    # ball = Ball()

    player = Player()


    HSM = HM(dir=DIR)
    player_name = textinput("Name", "what is your name?")

    screen.update()


    screen.listen()
    screen.onkeypress(key='space',fun=player.fire)
    screen.onkeyrelease(key='space',fun=player.xfire)
    # screen.onkeypress(key='Left',fun=bar.left)
    screen.onkeypress(key='Return',fun=start_game)

    score = 0
    sleep = 0.00001
    
    while True:

        while game_state == 0:
            # print('game_state: ',game_state)
            time.sleep(0.1)
            twrite.write('Press Enter to Start')
            screen.update()

        while game_state == 1 :
            # print('game_state: ',game_state)

            turtle.getcanvas().bind('<Motion>',player.mouse_move)
            player.move_projectiles()

            time.sleep(sleep)
            screen.update()

            if aliens[0].pos()[0] > 350:
                aliens_x_direction = -1

                # move down
                for a in aliens:
                    xy = a.pos()
                    a.goto( xy[0] , xy[1] - alien_down_shift)

            if aliens[0].pos()[0] < -950:
                aliens_x_direction = 1

                # move down
                for a in aliens:
                    xy = a.pos()
                    a.goto( xy[0] , xy[1] - alien_down_shift)

            # your score effects the speed of the alens
            alien_speed = alien_new_speed(score)

            for a in aliens:
                xy = a.pos()
                a.goto( xy[0] + ( 2 * aliens_x_direction), xy[1] )
            
            for a in aliens:
                if a.isvisible() == False:
                    continue

                for i,p in enumerate(player.projectiles):
                    if p.isvisible() == False:
                        continue
                    
                    if get_distance(a.pos(),p.pos()) < 20.0:
                        p.hideturtle()
                        p.goto(-3000,3000)
                        a.hideturtle()
                        score += 100

            for a in aliens:
                if a.isvisible() == False:
                    continue

                if a.pos()[1] < -200:
                    HSM.data.append({'name': player_name, 'score':score})
                    HSM.save()
                    game_state = 2 
                    break

            visible_aliens = sum([ 1 for a in aliens if a.isvisible() == True])
            new_color = random.choice(COLORS)
            if visible_aliens == 0:
                alien_down_shift += 50
                for x in range(-300,300,50):
                    for y in range(800 ,200,-50):
                        for a in aliens:
                            if a.isvisible() == False:
                                a.goto(int(x),int(y))
                                a.showturtle()
                                a.color(new_color)
                                break

                
            # twrite.write('score: {0:,.0f} | speed: {1:.5f}'.format(score,alien_speed))
            twrite.write('score: {0:,.0f}'.format(score))
            twrite2.write('ammo: {0}'.format(('*' * player.ammo_count()).ljust(5,'_')))
        
        while game_state == 2 :
            # go to center
            twrite.t.goto(0,0)
            twrite.write('GAME OVER \n score: {0:,.0f} \n\n top 5 \n {1}'.format(score,HSM.get_top(5)))
            screen.update()
            
        
    screen.exitonclick()

if __name__ == '__main__':
    # print([0,1,2,3,4,5][1:])
    main()