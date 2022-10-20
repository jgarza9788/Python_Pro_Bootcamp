import random
import math
from turtle import Turtle, Screen, pos


class Ball:
    def __init__(self,minY=-300,maxY=300,minX=-400,maxX=400):
        import math

        self.minY = minY
        self.maxY = maxY
        self.minX = minX
        self.maxX = maxX

        self.hit_bar_flag = False

        self.t = Turtle()
        self.t.up()
        # self.t.width(5)
        self.t.shape('circle')
        self.t.color('#ffffff')
        self.t.goto(0,0)    

        self.dir = [random.randint(1,10),5]
        self.in_speed = 10
        self.max_speed = 25

        self.set_dir()


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
        self.bounce_T()

    def bounce_T(self):
        d = self.dir
        self.dir = [d[0],d[1]*-1]

    def bounce_RL(self):
        d = self.dir
        self.dir = [d[0]*-1,d[1]]

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
        # self.try_bounce()
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

    def add_speed(self, more_speed = 0, multiply_speed = 1):
        xy = self.get_XY(more_speed,multiply_speed)
        self.dir = xy

    def set_dir(self):
        y = math.sin(self.get_angle())
        x = math.cos(self.get_angle())
        s = self.in_speed
        y *= s
        x *= s
        self.dir =  [x,y]

    def get_XY(self, more_speed=0, multiply_speed = 1):
        y = math.sin(self.get_angle())
        x = math.cos(self.get_angle())
        s = ( self.get_speed() + more_speed ) * multiply_speed
        s = min([s,self.max_speed])
        y *= s
        x *= s
        return [x,y]