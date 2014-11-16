import urllib2
from datetime import datetime
import time

def getCurrentImg(outFileName):
    response = urllib2.urlopen('http://10.9.167.106:8080/shot.jpg')
    f = response.read()
    fileOut = open(outFileName, 'w')
    fileOut.write(f)

# Root dir must not end in a slash
def takePicsEvery(numSeconds, rootDir):
    while True:
        now = datetime.now()
        dte = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        filename = rootDir + "/" + dte + ".jpg"
        getCurrentImg(filename)
        time.sleep(numSeconds)
        print "Took pic"

takePicsEvery(2,"./ippics", )
