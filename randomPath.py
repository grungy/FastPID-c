from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

class spline_2d():
    '''make a 2D spline where the independent variable is the path length'''
    def __init__(self, x, y):
        self.s = self.__calc_s(x, y)  # path length at each point
        self.sx = CubicSpline(self.s, x)  # a function of path distance
        self.sy = CubicSpline(self.s, y)  # a function of path distance

    def __calc_s(self, x, y):
        dx = np.diff(x)
        dy = np.diff(y)

        self.ds = np.append([0], np.hypot(dx, dy))
        return np.cumsum(self.ds)  # total path length up until each point in the array
    
    def calc_position(self, s):
        """
        calc position
        """
        x = self.sx(s)
        y = self.sy(s)

        return x, y

class randomPath():
    def __init__(self):
        self.x = np.random.randint(-8, 8, size=7)
        self.y = np.random.randint(-8, 8, size=7)
        self.x = np.append(self.x, self.x[0])  # make it closed loop
        self.y = np.append(self.y, self.y[0])  # make it closed loop
        self.ds = 1  # meters

        self.sp = spline_2d(self.x, self.y)
        self.s = np.arange(0, self.sp.s[-1], self.ds)  # construct vector with path data for use as independent variable
            # resample the splines
        self.rx, self.ry = self.sp.calc_position(self.s)
    
    def get(self):
        return np.vstack((self.rx, self.ry))
    
    def plotPath(self):
        plt.subplots(1)
        plt.plot(self.x, self.y, "xb", label="input")
        plt.plot(self.rx, self.ry, "-r", label="spline")
        plt.grid(True)
        plt.axis("equal")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.legend()
        plt.show()

if __name__ == "__main__":

    path = randomPath()
    path.plotPath()


    plt.show()