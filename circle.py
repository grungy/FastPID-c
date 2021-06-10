import numpy as np
from matplotlib import pyplot as plt

class circle(object):
    def __init__(self):

        # Creating equally spaced 100 data in range 0 to 2*pi
        theta = np.linspace(0, 2 * np.pi, 100)

        # Setting radius
        radius = 5

        # Generating x and y data
        self.x = radius * np.cos(theta)
        self.y = radius * np.sin(theta)

    def getPath(self):
        return np.vstack((self.x, self.y))


if __name__ == "__main__":
    
    circle = circle()
    path = circle.getPath()

    # Plotting
    plt.plot(path[0,:], path[1,:])
    plt.axis('equal')
    plt.title('Circle')
    plt.show()
