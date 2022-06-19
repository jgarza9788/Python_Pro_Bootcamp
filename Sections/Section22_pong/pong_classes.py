import random
import math
from turtle import Turtle, Screen, pos


# class GameState:
#     '''
#     a finite game state engine... but it would cause me to rewrite a log of code to work with it.
#     A for effort
#     '''

#     def __init__(self):
#         # self.int_hist = [0]
#         self.num = 0

#         self.states = {
#             'setup': {'start':[],'during':[]},
#             'playing': {'start':[],'during':[]},
#             'endgame': {'start':[],'during':[]},
#             'restart': {'start':[],'during':[]},
#         }

#         self.statelist = list(self.states.keys())

#     def print(self):
#         print( self.statelist[self.num] )
    
#     def get_state_name(self,num=None):
#         if num == None:
#             num = self.num
#         return self.statelist[num]

#     def exe(self,functs):
#         for f in functs:
#             f['funct'](f['args'])

#     def exe_current_state(self):
#         self.exe(self.states[self.get_state_name()]['during'])

#     def change(self,new_state):
#         if type(new_state) == str:
#             new_state = self.statelist.index(new_state)
        
#         if self.num == 0 and new_state == 1:
#             self.num = new_state
#         if self.num == 1 and new_state == 2:
#             self.num = new_state
#         if self.num == 2 and new_state == 3:
#             self.num = new_state
#         if self.num == 3 and new_state == 1:
#             self.num = new_state

#         self.exe(self.states[self.get_state_name()]['start'])


def clamp(n,minN,maxN):
    n = max([n,minN])
    n = min([n,maxN])
    return n


def collision_x(pos1,pos2,maxd=20):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    d = math.sqrt((x*x) + (y*y))
    if d <= maxd:
        return True
    else: 
        return False

def collision(poslist, pos):
    result = False
    for p in poslist:
        if collision_x(p,pos):
            result = True
            break;
    return result

class Paddle:
    def __init__(self,width=1,height=5,x=-350,y=0,minY=-300,maxY=300):
        self.turtles = []
        self.pos = [x,y]
        self.shift = [0,20]

        self.minY = minY
        self.maxY = maxY - ((height*20)/2)

        self.score = 0

        for i in range(height):
            s = Turtle()
            s.up()
            s.shape('square')
            # self.pos.append([i*-20,0])
            s.goto(self.calc_pos(i))
            s.color('#ffffff')
            self.turtles.append(s)

    def get_all_positions(self):
        result = []
        for t in self.turtles:
            result.append([t.pos()[0],t.pos()[1]])
        return result

    def calc_pos(self,i):
        return self.pos[0] + (i*self.shift[0]),self.pos[1] + (i*self.shift[1])
    
    def move(self):
        for index,i in enumerate(self.turtles):
            x,y  = self.calc_pos(index)
            i.goto(x,y)


    def up(self):
        y = self.pos[1]
        y += 20
        y = clamp(y,self.minY,self.maxY)
        self.pos[1] = y
    
    def down(self):
        y = self.pos[1]
        y -= 20
        y = clamp(y,self.minY,self.maxY)
        self.pos[1] = y


class Ball:
    def __init__(self,minY=-300,maxY=300,minX=-400,maxX=400):
        import math

        self.minY = minY
        self.maxY = maxY
        self.minX = minX
        self.maxX = maxX

        self.t = Turtle()
        self.t.up()
        # self.t.width(5)
        self.t.shape('circle')
        self.t.color('#ffffff')
        self.t.goto(0,0)    

        self.dir = [10,10]
        self.in_speed = 1.01

    def random_dir(self):
        x = random.randint(-10,10)
        y = random.randint(-10,10)
        self.dir = [x,y]

    def reset(self):
        # self.dir = []
        self.random_dir()

        while self.get_speed() <= 7.0:
            self.random_dir()

        self.t.goto(0,0)

    def try_bounce(self):
        if self.hit_top() or self.hit_bottom():
            self.bounce()

    def bounce(self):
        d = self.dir
        self.dir = [d[0],d[1]*-1]

    def change_x_dir(self):
        # self.increase_speed()
        d = self.dir
        self.dir = [d[0]*-1,d[1]]

    def hit_bottom(self):
        y = self.t.pos()[1]
        if y <= self.minY+20:
            return True
        else:
            return False

    def hit_top(self):
        y = self.t.pos()[1]
        if y >= self.maxY-20:
            return True
        else:
            return False

    def hit_right(self):
        x = self.t.pos()[0]
        if x >= self.maxX:
            return True
        else:
            return False

    def hit_left(self):
        x = self.t.pos()[0]
        if x <= self.minX:
            return True
        else:
            return False

    def move(self):
        self.try_bounce()
        pos = self.t.pos()
        x, y = pos[0] + self.dir[0], pos[1] + self.dir[1]
        self.t.goto(x,y)

    def get_angle(self):
        # return math.tan(self.dir[1]/self.dir[0])
        rad =  math.atan2(self.dir[1],self.dir[0]); 
        # return rad * (180 / math.PI)
        return rad
    
    def rad_to_degree(self,rad):
        return rad * (180/math.PI)
    
    def get_speed(self):
        return math.sqrt((math.pow(self.dir[1],2))+(math.pow(self.dir[0],2)))

    def get_XY(self):
        y = math.sin(self.get_angle())
        x = math.cos(self.get_angle())
        s = self.get_speed()
        y *= s
        x *= s
        return [x,y]
    
    # def increase_speed(self):
    #     s = self.get_speed()
    #     y = math.sin(self.get_angle())
    #     x = math.cos(self.get_angle())
    #     s = self.get_speed() * self.in_speed
    #     y *= s
    #     x *= s
    #     self.dir = [x,y]

    
    # def increase_speed(self):
    #     angle = math.tan(self.dir[1]/self.dir[0])
    #     hyp = math.sqrt((math.pow(self.dir[1],2))+(math.pow(self.dir[0],2)))
    #     hyp *= 1.01

    #     x = math.cos()




class Twrite:
    def __init__(self,color='#ffffff',x=0,y=0,font_size=24):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(int(x),int(y))
        self.t.color(color)
        self.font_size = font_size


    def write(self,text='hello'):
        self.t.clear()
        self.t.write(text,move=False,align="center", font=('Helvetica', self.font_size, 'bold'))


if __name__ == '__main__':
    b = Ball()
    b.dir = [1,-1]
    print(b.get_angle())

    pass


# testing the gamestate engine
    # def start_playing(args):
    #     print('start_playing')

    # def start_playing_and_print(args):
    #     # print('start_playing')
    #     print(args)

    # gs = GameState()
    # gs.print()
    # gs.states['playing']['start'].append({'funct':start_playing,'args':[]})
    # gs.states['playing']['start'].append({'funct':start_playing_and_print,'args':['Z','Y','Z']})

    # gs.change(1)
