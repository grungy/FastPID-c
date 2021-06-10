from ctypes import *
from circle import circle
from animatedScatter import AnimatedScatter
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation

if __name__ == "__main__":
    circle = circle()
    pid = cdll.LoadLibrary("pid.so")


    path = circle.getPath()

    plot = AnimatedScatter(path)
    plt.show()