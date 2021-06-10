import numpy as np
from matplotlib import pyplot as plt

class line(object):
    def __init__(self):


        # Setting radius
        radius = 5

        # Generating x and y data
        self.x = np.ones((1, 20))
        self.y = np.arange(0, 20)

    def getPath(self):
        return np.vstack((self.x, self.y))


if __name__ == "__main__":
    
    line = line()
    path = line.getPath()

    # Plotting
    plt.plot(path[0,:], path[1,:])
    plt.axis('equal')
    plt.title('Line')
    plt.show()
