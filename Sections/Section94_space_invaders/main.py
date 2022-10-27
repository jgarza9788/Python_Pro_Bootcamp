


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
# from highscore_manager import highscore_manager as HM

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
    x.setup(width=600,height=1250)
    x.bgcolor("#1f1f1f")
    x.title("Space Invaders 👽 - press enter to start")

    return x

# def score_to_sleep(score):
#     max_sleep = 0.075
#     min_sleep = 0.00005
#     sleep_diff = max_sleep - min_sleep
#     r = min([score/3300,1.0])
#     return max_sleep - ( sleep_diff * r )
    

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

    twrite = Twrite(color='#666666',x=0,y=((screen.window_height()/4)*-1))
    # hswrite = Twrite(color='#666666',y=-100)

    # blocks = []
    # for x in range(-375,375,25):
    #     for y in range(275,0,-25):
    #         blocks.append(make_block(color=random.choice(COLORS),x=x, y=y))
    
    # bar = Bar()
    # ball = Ball()

    player = Player()


    # HSM = HM(dir=DIR)
    player_name = textinput("Name", "what is your name?")

    screen.update()


    screen.listen()
    screen.onkeypress(key='space',fun=player.fire)
    screen.onkeyrelease(key='space',fun=player.xfire)
    # screen.onkeypress(key='Left',fun=bar.left)
    screen.onkeypress(key='Return',fun=start_game)

    score = 0
    ot = 0
    t = 0 
    sleep = 0.01
    
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

            # if ball.hit_right() or ball.hit_left():
            #     ball.bounce_RL()
            
            # if ball.hit_top():
            #     ball.bounce_T()
            
            
            # if ball.hit_bottom():
            #     game_state = 2
            #     # game over 
            
            # for b in blocks:
            #     if get_distance(b.pos(),ball.t.pos()) < 20.0 and b.isvisible():
            #         b.hideturtle()
            #         score += 100
            #         ball.add_speed(multiply_speed= 1.1)


            #         x = abs( b.pos()[0] - ball.t.pos()[0] )
            #         y = abs( b.pos()[1] - ball.t.pos()[1] )

            #         if x > y :
            #             ball.bounce_RL()
            #         else:
            #             ball.bounce_T()
                    
            #         break;
            
            # min_ball_distance = 100
            # for b in bar.turtles:
            #     ball_distance = get_distance(b.pos(),ball.t.pos())
            #     if ball_distance < 20.0 and ball.hit_bar_flag == False:
            #         score += 100
            #         ball.hit_bar_flag = True
            #         ball.bounce_T()
                
                # min_ball_distance = min( [ ball_distance, min_ball_distance])
            
            # if min_ball_distance >= 40.0 and ball.hit_bar_flag == True:
            #     ball.hit_bar_flag = False
                
            # # twrite.write('score: {0:,.0f} | speed: {1:.5f}'.format(score,ball.get_speed()))
            twrite.write('score: {0:,.0f} '.format(score))
        
        while game_state == 2 :
            # twrite.write('GAME OVER \n score: {0:,.0f} '.format(score))
            screen.update()
            
        
    screen.exitonclick()

if __name__ == '__main__':
    # print([0,1,2,3,4,5][1:])
    main()