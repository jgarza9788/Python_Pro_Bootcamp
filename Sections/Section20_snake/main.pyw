
import math
import time
import random
from turtle import Turtle, Screen
import turtle

from snake_class import Snake,Food,Twrite

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
    x.title("Snake 🐍")

    return x

def score_to_sleep(score):
    score = score/100000
    e =  1 - (1 - score) * (1 - score);
    return 0.1 - (0.075 * e)


def get_distance(sp,fp):
    d = sp - fp
    return math.sqrt((d[0]*d[0])+(d[1]*d[1]))

def start_game():
    global game_state
    if game_state == 0:
        game_state = 1



def main():
    global game_state

    screen = get_screen()
    screen.tracer(0)
    # snake = Snake(color=random.choice(COLORS))
    snake = Snake()
    print(snake.get_size())
    screen.update()

    food = Food( screen_width = screen.window_width() - 40, screen_height=screen.window_height() - 40)

    twrite = Twrite(y=((screen.window_height()/2) - 40))

    screen.listen()
    screen.onkeypress(key='Up',fun=snake.up)
    screen.onkeypress(key='Down',fun=snake.down)
    screen.onkeypress(key='Right',fun=snake.right)
    screen.onkeypress(key='Left',fun=snake.left)
    screen.onkeypress(key='Return',fun=start_game)


    score = 0
    ot = 0
    t = 0 
    sleep = 0.25

    while game_state == 0:
        time.sleep(0.1)
        twrite.write('Press Enter to Start')

    while game_state == 1 :
        snake.move()
        time.sleep(sleep)
        screen.update()

        t += sleep
        score += (t - ot) * 100
        ot = t

        sleep = score_to_sleep(score=score)


        if snake.is_out_of_window(width = screen.window_width(), height=screen.window_height() ) :
            game_state = 2

        if snake.is_overlap():
            game_state = 2

        # print(snake.get_head_pos())
        
        if get_distance(snake.get_head_pos(),food.get_pos()) < 20.0:
            score += 1000
            snake.grow()
            print('score: {0} \n sleep: {1}'.format(score,sleep),end='\r')
            food.move()
        
        twrite.write('score: {0:,.0f}'.format(score))
        


    screen.exitonclick()

if __name__ == '__main__':
    # print([0,1,2,3,4,5][1:])
    main()