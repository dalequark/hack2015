import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np
import random
import sys, serial
SERIAL = True
#SERIAL_PORT = '/tmp/tty.LightBlue-Bean'
SERIAL_PORT = '/dev/tty.usbmodem1411'
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
    maxpoints=120      # (!) keep a max of 120 pts on screen
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

data = Data([trace1, trace2])

# Add title to layout object
layout = Layout(title='Arduino Data')

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='arduino data')

import datetime
import time
s1 = py.Stream(stream_ids[0])
s2 = py.Stream(stream_ids[1])
s1.open()
s2.open()

SECOND_CHANNEL = False
i = 0
while True:
    x=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if SERIAL:
        line = ser.readline()
        line = line.split()
        if(len(line) < 2):  continue
        if(line[0].isdigit()):
            data1 =  (float(line[0]) * 5 / 1023 )
            data2 =  (float(line[1]) * 5 / 1023 )
            print data1
            if(i%5 == 0):   s1.write( dict( x=x, y= data1 ))
            i += 1

        if(SECOND_CHANNEL):
            if(line[1].isdigit()):
                s2.write( dict(x=x, y=data2) )
    else:
        int1 =random.randint(0,10)
        int2 =random.randint(0,10)
        s1.write(dict(x=x,y=int1))
        s2.write(dict(x=x,y=int2))

if SERIAL:
    s1.close()
    s2.close()
