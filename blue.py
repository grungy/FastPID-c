from circle import circle
from ctypes import *
import numpy as np

# pidlib = cdll.LoadLibrary("pid.so")

class blue(object):
    def __init__(self):
        self.curx = 0
        self.cury = 0
        self.curPos = np.zeros(2)
        self.index = 0
        self.color = 0
        
        self.pid = cdll.LoadLibrary("pid.so")
        self.pid.init_pid(1, 1, 1)
    
    def update(self, redPos):
        distance = np.linalg.norm(self.curPos - redPos)
        print("Distance: %f" % c_int16(int(distance)).value)
        self.pid.pid_update(c_int16(int(distance)).value)
        output = int(self.pid.get())
        print("Output: %f" % output)
        self.curPos = self.curPos + output * (self.curPos - redPos)
        print("Blue curPos: ", self.curPos)
    
    def getPos(self):
        return np.array([self.curPos[0], self.curPos[1], self.color])

if __name__ == "__main__":
    obj = blue()
    print(obj.curPos)

    redPos = np.array([1, 1])
    obj.update(redPos)
    print(obj.curPos)