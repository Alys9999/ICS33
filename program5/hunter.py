# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from simulton import Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self,x,y,angle,speed,color,width,height):
        Pulsator.__init__(self,x,y,angle,speed,color,width,height)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)
        
        
        
    def update(self,model):
        self.move()
        self.wall_bounce()
        eaten=Pulsator.update(self,model)
        p= model.find(Prey)
        min_dis=201
        for b in p:
            b_dot=Simulton.get_location(b)
            b_dis=Simulton.distance(self,b_dot)
            if b_dis<min_dis:
                mb=b
                min_dis=b_dis
        if min_dis<=200:
            x_diff=mb._x-self._x
            y_diff=mb._y-self._y
            self._angle=atan2(y_diff,x_diff)
        return eaten
