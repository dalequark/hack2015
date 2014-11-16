import urllib2
from datetime import datetime
import time
from os import listdir, remove
from os.path import isfile, join

def getCurrentImg(outFileName):
#    response = urllib2.urlopen('http://10.9.167.106:8080/shot.jpg')
    response = urllib2.urlopen('http://i.imgur.com/FAcssWK.jpg')
    f = response.read()
    fileOut = open(outFileName, 'w')
    fileOut.write(f)

# keeps the latest n files in rootDir
def keepLast(rootDir, n):
    allFiles = sorted([f for f in listdir(rootDir) if isfile(join(rootDir, f))])
    filesToDelete = allFiles[:-(n-1)] # off by 1 lol wtf
    for f in filesToDelete:
        remove(rootDir + '/' + f)

# Root dir must not end in a slash
def takePicsEvery(numSeconds, rootDir):
    while True:
        now = datetime.now()
        dte = str(now.year) + ':' + str(now.month) + ':' + str(now.day) + ':' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
        filename = rootDir + '/' + dte + '.jpg'
        getCurrentImg(filename)
        time.sleep(numSeconds)

        # for testing purposes only want to keep last 1000 files
        keepLast(rootDir, 1000)

takePicsEvery(5, './website/pics', )
