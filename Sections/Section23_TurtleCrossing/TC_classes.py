import random,math
from turtle import Turtle, Screen, pos


def clamp(n,minN,maxN):
    n = max([n,minN])
    n = min([n,maxN])
    return n


def collision(pos1,pos2,maxd=20):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    d = math.sqrt((x*x) + (y*y))
    if d <= maxd:
        return True
    else: 
        return False


class PlayerTurtle:
    def __init__(self, color='#A6E22E',minY=-300, maxY = 300,minX=-300,maxX=300):
        t = Turtle()
        t.up()
        t.color(color)
        t.goto(0,minY+20)
        t.shape('turtle')
        t.setheading(90)
        self.turtle = t

        self.maxY = maxY
        self.minY = minY
        self.maxX = maxX
        self.minX = minX

    def get_pos(self):
        return self.turtle.pos()

    def won(self):
        if self.turtle.pos()[1] >= self.maxY:
            return True
        else:
            return False

    def reset(self):
        self.turtle.goto(0,self.minY+20)

    def up(self):
        self.turtle.setheading(90)
        self.turtle.forward(20)

    def down(self):
        self.turtle.setheading(-90)
        self.turtle.forward(20)

    def right(self):
        self.turtle.setheading(0)
        self.turtle.forward(20)

    def left(self):
        self.turtle.setheading(180)
        self.turtle.forward(20)
        

class Trains:
    def __init__(self,count=10,speed_range=[5,10],colors=None,minY=-300,maxY=300,minX=-300,maxX=300):

        self.minY = minY
        self.maxY = maxY
        self.minX = minX
        self.maxX = maxX
        self.speed_range = speed_range
        self.count = count*2

        if colors == None:
            colors = ['#ff0000','#00ff00','#0000ff','#ffff00','#00ffff','#ff00ff']

        self.colors = colors
        random.shuffle(self.colors)

        self.trains = []
        for i in range(int(self.count)):
            self.trains.append(
                {
                    't': self.create_train(),
                    'speed': random.uniform(self.speed_range[0],self.speed_range[1])
                }
                )


    def move(self):
        for index,t in enumerate(self.trains):
            if index%2 == 0:
                t['t'].forward(t['speed'])
            else:
                bt = self.trains[index-1]['t']
                t['t'].goto(bt.pos()[0]-20,bt.pos()[1])
                t['t'].color(bt.color()[0])
        
            if t['t'].pos()[0] < (self.minX -50):
                t['t'].goto(
                    random.randint(int(self.maxX/4),self.maxX) + self.maxX,
                    random.randint(int(self.minY*0.8),int(self.maxY*0.8)) 
                )

    def increase_speed(self):
        self.speed_range[0] = 1.1*self.speed_range[0]
        self.speed_range[1] = 1.1*self.speed_range[1]

    def change_count(self):
        self.count = int(1.3*self.count)
        print(self.speed_range)
        
        for t in self.trains:
            t['t'].reset()
            t['t'].up()
            t['t'].goto(-1000,-1000)
            t['t'] = None
        self.trains = []

        for i in range(int(self.count)):
            self.trains.append(
                {
                    't': self.create_train(),
                    'speed': random.uniform(self.speed_range[0],self.speed_range[1])
                }
                )
        
    def create_train(self):
        s = Turtle()
        s.up()
        s.shape('square')
        s.setheading(180)
        s.goto(
            # self.maxX + random.randint(50,100), 
            # random.randint(int(self.minX*0.8),int(self.maxX*0.8)) + self.maxX,
            # random.randint(int(self.minY*0.8),int(self.maxY*0.8)) 
            # )
                random.randint(int(self.minX),int(self.maxX)),
                random.randint(int(self.minY*0.8),int(self.maxY*0.8)) 
            )
        s.color(self.colors[random.randint(0,len(self.colors)-1)])
        return s


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
        self.t.write(
            text,
            move=False,
            align="left", 
            font=('Helvetica', self.font_size, 'bold')
            )
