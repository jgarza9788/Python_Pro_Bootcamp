from turtle import Turtle


class Player:
    def __init__(self,width=1,shoot_on=50,x=0,y=-250,minX=-375,maxX=375):
        self.t = Turtle()
        self.t.up()
        self.t.shape('arrow')
        self.t.color('#ffffff')
        self.t.setheading(90)
        self.t.goto(x,y)

        self.projectiles = []
        self.projectile_speed = 5
        self.firing = False
        self.i = 0

        self.minX = minX
        self.maxX = maxX 

        

        for i in range(5):
            p = Turtle()
            p.up()
            p.shape('classic')
            p.setheading(90)
            p.goto(self.t.pos())
            p.color('#ff0000')
            p.width(width=5)
            # p.down()
            p.hideturtle()
            self.projectiles.append(p)

    def ammo_count(self):
        return sum([ 1 for p in self.projectiles if p.isvisible() == False])

    def get_all_positions(self):
        result = []
        for t in self.turtles:
            result.append([t.pos()[0],t.pos()[1]])
        return result

    def move_projectiles(self):
        self.i += 1
        for p in self.projectiles:
            # lets also recycle the turtle
            if p.pos()[1] >= 300:
                p.hideturtle()
                p.up()
                p.clear()
            else:
                p.forward(self.projectile_speed)
                if (self.i % 5) == 0:
                    self.i = 0
                    p.clear()
    
    def fire(self):
        # self.projectiles.append(self.get_projectile())
        if self.firing == False:
            self.firing = True
            print('fire!')

            for p in self.projectiles:
                if p.isvisible() == False:
                    p.goto(self.t.pos())
                    p.showturtle()
                    p.down()
                    break;


    def xfire(self):
        self.firing = False
        print('x')

    def mouse_move(self,event):
        # print(event.x, event.y)
        self.t.goto( (event.x - 300) , self.t.pos()[1] )
