import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
import time


# class that holds analog data for N samples
class AnalogData:
  # constr
  def __init__(self, maxLen):
    self.ax = deque([0.0]*maxLen)       # maxLen = no. of samples?
    self.ay = deque([0.0]*maxLen)
    self.maxLen = maxLen

  # ring buffer
  def addToBuf(self, buf, val):
    if len(buf) < self.maxLen:
      buf.append(val)
    else:
      buf.pop()
      buf.appendleft(val)

  # add data
  def add(self, data):
    assert(len(data) == 2)
    self.addToBuf(self.ax, data[0])
    self.addToBuf(self.ay, data[1])

# plot class
class AnalogPlot:
  # constr
  def __init__(self, analogData):
    hi = "dog"
    # set plot to animated
    #plt.ion()
    #self.axline, = plt.plot(analogData.ax)
    #pself.ayline, = plt.plot(analogData.ay)
    #plt.ylim([0,10])
   # update plot
  def update(self, analogData):
    self.axline.set_ydata(analogData.ax)
    self.ayline.set_ydata(analogData.ay)
    #plt.draw()
def main():                           # main() function
  analogData = AnalogData(200)        # data range (maxLen)
  analogPlot = AnalogPlot(analogData)
  print 'plotting data...'
  # open serial port
  ser = serial.Serial('/tmp/tty.LightBlue-Bean', 9600)
  blt = 0
  blot = []
  for i in range(100) : # total data points to plot
      line = ser.readline()
      data = [float(val) for val in line.split(" ")]
      blt = blt+1
      blot.append(float(val))
      #print blot
      print data
      if(len(data) == 2):
        analogData.add(data)
        analogPlot.update(analogData)
  #close serial
  ser.flush()
  ser.close()
  time.sleep(1)
  #plt.close("all")
  f=open("plot_store_1", "w")
  f.write("\n".join(str(x) for x in blot))
  #plt.close("all")
# call main
if __name__ == '__main__':
  main()
