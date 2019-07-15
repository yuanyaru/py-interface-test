#!/usr/bin/python
#-*-coding:utf-8-*-
#测试内容：3个线程，同一个点，同一个功能：读取不同时期的值
#测试结果：ok

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea
import time, threading

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
        
    pIDs = []
    ycdata = []
    for i in range(5):
        pIDs.append(i)
        structycdata = YCArea.DxDTYC(i, i+2.1, i)
        ycdata.append(structycdata)
    #print(ycdata)
    
    pID = 0
    datetime = "20190418"
    
    DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
    #DataCommand.RPCSaveYCData(pIDs, ycdata)
    
    class myThread(threading.Thread):
        def __init__(self, pID, name):
            threading.Thread.__init__(self)
            self.pID = pID
            self.name = name
        
        def run(self):                           
            print "Starting " + self.name
            print_data(self.pID, self.name)
            print "Exiting " + self.name  

    def print_data(pID, threadName):
        ycdata = DataCommand.RPCGetDayYCData(datetime, pID)
        for i in range(len(ycdata)):
            print("%s: %s, %s, %s" %(threadName, ycdata[i].status, ycdata[i].value, ycdata[i].timetag))

    thread1 = myThread(0, "Thread-1")
    thread2 = myThread(0, "Thread-2")
    thread3 = myThread(0, "Thread-3")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    
except:
    traceback.print_exc()
    status = 1

if ic:
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1
sys.exit(status)
