# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
import prey



class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y,color,width,height):
        Simulton.__init__(self,x,y,width,height)
        self._x       = x
        self._y       = y
        self._color   = color
        self.eaten=set()
        
    def update(self,model):
        p= model.find(prey.Prey)
        for b in p:
            if Black_Hole.contains(self,b):
                self.eaten.add(b)
                model.remove(b)
        return self.eaten
            
            
        
    def display(self,canvas):
       di=Simulton.get_dimension(self)
       canvas.create_oval(self._x-(di[0]/2)      , self._y-(di[1]/2),
                                self._x+(di[0]/2), self._y+(di[1]/2),
                                fill=self._color)

    def contains(self,b):
        if (b._x-self._x)**2+(b._y-self._y)**2<=Black_Hole.radius**2:
            return True
        else:
            return False
        
