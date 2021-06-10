from ctypes import *
import matplotlib.pyplot as plt
import numpy as np  



if __name__ == "__main__":

    pidlib = cdll.LoadLibrary("libFastPID.so")

    print(pidlib.five(None))

    Kp=0.1 
    Ki=0.5 
    Kd=0 
    Hz=10
    output_bits = 1
    output_signed = False
    feedback = 100
    setpoint = 0

    pidlib.configure(float(Kp), Ki, Kd, Hz, output_bits, output_signed)