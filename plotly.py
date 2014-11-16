import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np
import random
import sys, serial
import urllib2


#Python backend server
BACKEND_SERVER = 'http://127.0.0.1:5000'
# Where to save data for this file
FILE_SAVE = "test1"
f = open(FILE_SAVE, 'w')

# Test with our without real serial data (otherwise random)
SERIAL = True
# Plot both channels
SECOND_CHANNEL = True
# Serial port of light blue bean
SERIAL_PORT = '/tmp/tty.LightBlue-Bean'

#Data processing:
slidingWindow1 = [5 for n in range(10)]
thresh = 512


if SERIAL:
    ser = serial.Serial(SERIAL_PORT, 57600)

random.seed()
py.sign_in("dalequark", "zgfdgx1clm")

tls.set_credentials_file(stream_ids=[
    "vbjdnxnbo8",
    "idwewk38ut",
    "t2zo0cl5ze",
    "vv91n5pc3k"
])

stream_ids = tls.get_credentials_file()['stream_ids']


# Make instance of stream id object
stream1 = Stream(
    token=stream_ids[0],  # (!) link stream id to 'token' key
    maxpoints=300      # (!) keep a max of 120 pts on screen
)
stream2 = Stream(
    token=stream_ids[1],  # (!) link stream id to 'token' key
    maxpoints=300      # (!) keep a max of 120 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream1         # (!) embed stream id, 1 per trace,

)

trace2 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream2         # (!) embed stream id, 1 per trace

)

data1 = Data([trace1])
data2 = Data([trace2])

# Add title to layout object
layout1 = Layout(title='EndoDermal Skin Response',
    xaxis=XAxis(
        title="Timestamp"
    ),
    yaxis=YAxis(
        title="Volts"
    )
)
layout2 = Layout(title='HeartRate',
    xaxis=XAxis(
        title="Timestamp"
    ),
    yaxis=YAxis(
        title="Beats per Minute"
    )
)
# Make a figure object
fig1 = Figure(data=data1, layout=layout1)
fig2 = Figure(data=data2, layout=layout2)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url1 = py.plot(fig1, filename='gsr')
unique_url2 = py.plot(fig2, filename='heartrate')

import datetime
import time
s1 = py.Stream(stream_ids[0])
s2 = py.Stream(stream_ids[1])
s1.open()
s2.open()
f = open(FILE_SAVE, 'w')
i = 0
while True:
    # For each readline, you get a string that's float1 float2\n
    x=time.time()   #datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S.%f')
    if SERIAL:
        line = ser.readline()
        line = line.split()
        if(len(line) < 2):  continue
        if(line[0].isdigit()):
            gsrData =  (float(line[0]) * 5 / 1023 )
            heartData =  (float(line[1]) * 5 / 1023 )
            slidingWindow1.pop(0)
            slidingWindow1.append(gsrData)
            deviation = abs(slidingWindow1[len(slidingWindow1) - 2] - (slidingWindow1[len(slidingWindow1) - 1] + slidingWindow1[len(slidingWindow1) - 3]) / 2)
            print "deviation "
            print deviation
            if(slidingWindow1[len(slidingWindow1) - 2] - slidingWindow1[0] > .06 and deviation < .05):
                #Send request to python server, alerting of event
                print "Got trigger"
                urllib2.urlopen(BACKEND_SERVER+"/trigger")
            else:

                urllib2.urlopen( BACKEND_SERVER+"/setarousallevel/" + str(20*gsrData) )
            # sends data to plotly. ONly send it every 5 cycles because
            # plotly is too slow
            s1.write( dict( x=x, y= gsrData ))

        if(SECOND_CHANNEL):
            if(line[1].isdigit()):
                s2.write( dict(x=x, y=heartData) )
            print "%f, %f, %f" % (time.time(), gsrData, heartData)

    else:
        int1 =random.randint(0,10)
        int2 =random.randint(0,10)
        s1.write(dict(x=x,y=int1))
        s2.write(dict(x=x,y=int2))

if SERIAL:
    s1.close()
    s2.close()
