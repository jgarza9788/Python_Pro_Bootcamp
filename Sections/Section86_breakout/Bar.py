from turtle import Turtle

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

class Bar:
    def __init__(self,width=1,height=5,x=0,y=-250,minX=-375,maxX=375):
        self.turtles = []
        self.pos = [x,y]
        self.shift = [20,0]

        self.minX = minX
        self.maxX = maxX 

        # self.sync_x = False

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

    def mouse_move(self,event):
        print(event.x, event.y)

        for index,i in enumerate(self.turtles):
            i.goto( (event.x - 400) + (index * self.shift[0]), self.pos[1] )



    def left(self):
        x = self.pos[0]
        x -= 10
        x = clamp(x,self.minX,self.maxX)
        self.pos[0] = x
    
    def right(self):
        x = self.pos[0]
        x += 10
        x = clamp(x,self.minX,self.maxX)
        self.pos[0] = x