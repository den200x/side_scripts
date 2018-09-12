import datetime
import time
import threading

print('starting')

def startTime():
    return datetime.datetime.now()
tl=[]
def datetimeConverter():
    startTimestring = str(startTime())
    startTimelist = startTimestring.split()
    tS = list(map(float,startTimelist[1].split(':')))
    csT= tS[0]*3600+tS[1]*60+tS[2]
    tl.append(csT)

    print(tl)
    print(csT)
    return



def ProcessingTime():
    datetimeConverter()
    tdc = tl[1]-tl[0]
    print(tdc)
    del tl[:]
    return


print(tl)

datetimeConverter()

time.sleep(3)

ProcessingTime()
print(tl)
