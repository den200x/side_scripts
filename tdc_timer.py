import datetime
import time

tl=[]
startTime = ''
class timeTool:
    def runTime(self):
        global startTime
        startTime = datetime.datetime.now()
        return

    def datetimeConverter(self):
        global tl
        self.runTime()
        #print(type(startTime))
        startTimestring = str(startTime)
        startTimelist = startTimestring.split()
        tS = list(map(float,startTimelist[1].split(':')))
        csT= tS[0]*3600+tS[1]*60+tS[2]
        tl.append(csT)

        #print(tl)
        print(csT)
        return


    def ProcessingTime(self):
        self.datetimeConverter()
        tdc = tl[1]-tl[0]
        print(tdc)
        del tl[:]
        return