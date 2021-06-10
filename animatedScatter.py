import matplotlib.pyplot as plt
import matplotlib.animation as animation
from circle import circle
from red import red
from blue import blue
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, path):
        self.dt = 45
        self.red = red()
        self.blue = blue()
        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots()
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=self.dt, 
                                          init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        # self.ax.plot(, , "xb", label="input")
        self.ax.plot(self.red.path[0, :], self.red.path[1, :], "-r", label="spline")

        data = np.vstack((self.red.getPos(), self.blue.getPos()))
    
        self.scat = self.ax.scatter(data[:, 0], data[:, 1], c=data[:, 2], vmin=0, vmax=1,
                                    cmap="jet", edgecolor="k")
        self.ax.axis([-10, 10, -10, 10])
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        # data = next(self.stream)
        self.red.update()
        self.blue.update(self.red.getPos()[:2])
        data = np.vstack((self.red.getPos(), self.blue.getPos()))

        # Set sizes...
        self.scat.set_sizes(np.array([100, 100]))
        # Set x and y data...
        self.scat.set_offsets(data[:, :2])
        # Set colors..
        self.scat.set_array(data[:, 2])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

if __name__ == "__main__":
    circle = circle()
    path = circle.getPath()
    plot = AnimatedScatter(path)
    plt.show()