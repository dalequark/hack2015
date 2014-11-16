import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import serial

ser = serial.Serial("/dev/tty.usbmodem1411", 57600)

fig = plt.figure()
ax = fig.add_subplot(111)
# some X and Y data
x = np.arange(10000)
y = np.random.randn(10000)
li, = ax.plot(x, y)
fig.canvas.draw()
plt.show(block=False)
ser.nonblocking()

while True:
    try:
        line = ser.readline()
        line = line.split()
        if(len(line) < 2):  continue
        if(line[0].isdigit()):
            data1 =  (float(line[0]) * 5 / 1023 )
            data2 =  (float(line[1]) * 5 / 1023 )
        else:
            continue
        a1.appendleft(data1)
        datatoplot = a1.pop()
        line.set_ydata(a1)
        fig.canvas.draw()
        time.sleep(0.1)
    except KeyboardInterrupt:
        break                   #add this it will be OK.
