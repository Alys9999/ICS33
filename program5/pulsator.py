# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from prey import Prey
from simulton import Simulton


class Pulsator(Black_Hole): 
    count=30
    def __init__(self,x,y,angle,speed,color,width,height):
        self.eaten_size=0
        Black_Hole.__init__(self,x,y,color,width,height)
    
    def update(self,model):
        eaten=Black_Hole.update(self,model)
        if len(eaten) > self.eaten_size:
            self.eaten_size=len(eaten)
            Pulsator.count=30
            Simulton.change_dimension(self,1,1)
        else:
            Pulsator.count-=1
            if Pulsator.count==0:
                Simulton.change_dimension(self,-1,-1)
                Pulsator.count=30
            if Simulton.get_dimension(self)==(0,0):
                model.remove(self)
        return eaten
        
