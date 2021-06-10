from circle import circle
from line import line
from randomPath import randomPath
import numpy as np

class red(object):
    def __init__(self):
        self.circle = circle()
        self.randomPath = randomPath()
        self.path = self.circle.getPath()

        self.x = self.path[0,:]
        self.y = self.path[1,:]
        self.curx = self.x[0]
        self.cury = self.y[0]
        self.index = 0
        self.color = 1
    
    def update(self):
        self.index += 1
        if(self.index >= self.x.shape[0]):
            self.index = 0
        
        self.curx = self.x[self.index]
        self.cury = self.y[self.index]
    
    def getPos(self):
        return np.array([self.curx, self.cury, self.color])