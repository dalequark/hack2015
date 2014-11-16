import serial
import time
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

SERIAL_PORT = "/dev/tty.usbmodem1411"
FILE_SAVE = "./testdata.csv"
ser = serial.Serial(SERIAL_PORT, 57600)

f = open(FILE_SAVE, 'w')
numDataPoints = 0
currentMean = 0
currentStdDev = 0
weightMean = 0.2
weightStdDev = 0
while True:
    line = ser.readline()
    line = line.split()
    if(len(line) < 2):  continue
    if(line[0].isdigit()):
        data1 =  (float(line[0]) * 5 / 1023 )
        s.send(str(data1))
        data2 =  (float(line[1]) * 5 / 1023 )
        numDataPoints += 1

        currentMean = weightMean*data1 + currentMean*(1-weightMean)
        delta = abs(currentMean - data1)
        if(abs(currentMean - data1) > 1.5*currentStdDev):
            print "Out of stddev!"
            print time.time()
            print "Std dev is "
            print currentStdDev
            print "Mean is "
            print currentMean
            print "currentData is"
            print data1
        currentStdDev = float(delta)/numDataPoints + currentStdDev*(numDataPoints-1)/float(numDataPoints)
        print "%f, %f, %f" % (time.time(), data1, data2)
        f.write("%f, %f, %f\n" % (time.time(), data1, data2))
