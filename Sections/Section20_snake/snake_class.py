
import random
from turtle import Turtle, Screen, pos


class Snake:

    def __init__(self, color='#A6E22E', size= 3):
        self.turtles = []
        self.pos = []
        self.color = color
        # self.speed = 0 # 0, 1, 2 , 3, 4
        # self.direction = 0
        self.shift = [0,0]
        
        for i in range(size):
            s = Turtle()
            s.up()
            s.shape('square')
            self.pos.append([i*-20,0])
            s.goto(i*-20,0)
            s.color(self.color)
            self.turtles.append(s)
        
        self.right()
    
        
    def get_size(self):
        return len(self.turtles)
    
    def get_head_pos(self):
        return self.turtles[0].pos()

    def move(self):
        p = (self.pos[0][0] + self.shift[0], self.pos[0][1] + self.shift[1])
        self.pos.insert(0,p)

        for i,t in enumerate(self.turtles):
            # t.speed(self.get_speed())
            t.goto(self.pos[i])

        self.pos = self.pos[:self.get_size()]

    def grow(self):
        n = Turtle()
        n.up()
        n.shape('square')
        p = self.turtles[-1].pos()
        self.pos.append([p[0],p[1]])
        n.goto(p[0],p[1])
        n.color(self.color)
        self.turtles.append(n)

    def up(self):
        # self.direction = 90
        if self.shift == [0,-20]:
            return 0

        self.shift = [0,20]

    def down(self):
        # self.direction = -90
        if self.shift == [0,20]:
            return 0
        self.shift = [0,-20]

    def right(self):
        # self.direction = 0
        if self.shift == [-20,0]:
            return 0
        self.shift = [20,0]

    def left(self):
        # self.direction = 180
        if self.shift == [20,0]:
            return 0
        self.shift = [-20,0]

    def is_out_of_window(self,width=600,height=600):
        
        p = self.get_head_pos()

        minX = width/-2
        maxX = width/2
        minY = height/-2
        maxY = height/2

        result = False

        if p[0] < minX:
            result = True
        if p[0] > maxX:
            result = True
        if p[1] < minY:
            result = True
        if p[1] > maxY:
            result = True
        
        return result
    
    def is_overlap(self):

        result = False
        for t in self.turtles[1:]:
            if self.get_head_pos() == t.pos():
                result = True
                break;
        return result

class Food:
    def __init__(self,color='#66D9EF',screen_width=580, screen_height=580):
        self.t = Turtle()
        self.t.up()
        self.t.color(color)
        self.t.shape('circle')

        self.w = ((screen_width/20)/2)
        self.h = ((screen_height/20)/2)

        self.t.goto(random.randint(self.w*-1*20,self.w*20),random.randint(self.h*-1*20,self.h*20))
    
    def get_pos(self):
        return self.t.pos()
    
    def move(self):
        self.t.goto(random.randint(self.w*-1*20,self.w*20),random.randint(self.h*-1*20,self.h*20))

class Twrite:
    def __init__(self,color='#F92672',x=0,y=0):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(int(x),int(y))
        self.t.color(color)


    def write(self,text='hello'):
        self.t.clear()
        self.t.write(text,move=False,align="center", font=('Arial', 24, 'bold'))
