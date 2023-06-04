'''
Created on 7 Sep, 2021

@author: Rituraj
'''
class particle:
    
    def create(self,x,ox,y,oy):
        self.x=x
        self.ox=ox
        self.y=y
        self.oy=oy
        
    def get_velX(self):
        return self.x-self.ox
    def get_velY(self):
        return self.y-self.oy
