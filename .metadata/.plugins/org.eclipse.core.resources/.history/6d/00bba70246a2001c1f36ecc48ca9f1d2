# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
import math
import random


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y,angle,speed,color,width,height):
        Prey.__init__(self,x,y,width,height,angle,speed)
        self._x       = x
        self._y       = y
        self._speed   = speed
        self._angle   = angle
        self._color   = color
        
    def update(self,model):
        r=random.randint(0,9)
        if r<=2:
            s=self.get_speed()+random.uniform(-0.5,+0.5)
            if 3<=s and s<=7:
                self.set_speed(s)
            a=self.get_angle()+random.uniform(-0.5,+0.5)
            self.set_angle(a)
            self.move()
            self.wall_bounce()
        else:
            self.move()
            self.wall_bounce()
        
    def display(self,canvas):
       canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
