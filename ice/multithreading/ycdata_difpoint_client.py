#!/usr/bin/python
#-*-coding:utf-8-*-
#测试内容：5个线程，5个不同的点，1个点1000个数据，读取1天5点5000个数据的时间测试
#测试结果：读取1天5点5000个数据的时间是读取1天1点1000个数据的5倍

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
    datetime = "20190418"
    ycdata = []
    for i in range(5):
        pIDs.append(i)
        structycdata = YCArea.DxDTYC(i, i+2.1, i)
        ycdata.append(structycdata)
        DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
            
    datetime = "20190418"
    
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
    start = time.time()
    thread1 = myThread(0, "Thread-1")
    thread2 = myThread(1, "Thread-2")
    thread3 = myThread(2, "Thread-3")
    thread4 = myThread(3, "Thread-4")
    thread5 = myThread(4, "Thread-5")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    elapsed = (time.time() - start)
    print("read ycdata time use: %s " % elapsed) 
    
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
