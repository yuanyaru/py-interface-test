#!/usr/bin/python
#-*-coding:utf-8-*-
#测试内容：3个线程，同一个点，不同功能
#测试结果：

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea
import time, threading, thread

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
   
    pIDs = []
    pIDs.append(0)
    ycdata = []
    ycdata1 = []
    
    """
    i = 2
    structycdata = YCArea.DxDTYC(i, i+1.1, i)
    ycdata.append(structycdata)
    """

    pID = 0
    datetime = "20190419"
    
    def write_data(threadName):
       
        for i in range(2,5):
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
            DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
            #DataCommand.RPCGetRealtimeYCData(pIDs)
            ycdata.pop()
        
        #DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
        print("%s执行了写数据" %threadName)
    
    def get_data(threadName):
        ycdata1 = DataCommand.RPCGetDayYCData(datetime, pID)
        for i in range(len(ycdata1)):
            print("%s: %s, %s, %s" %(threadName, ycdata1[i].status, ycdata1[i].value, ycdata1[i].timetag))

    def get_realdata(threadName):
        ycdata = DataCommand.RPCGetRealtimeYCData(pIDs)
        print("读取遥测数据%s" %len(ycdata))
        for i in range(len(ycdata)):
            print("%s: %s, %s, %s" %(threadName, ycdata[i].status, ycdata[i].value, ycdata[i].timetag))
    
    threads = []
    t1 = threading.Thread(target=get_data, args=("thread-1",))
    t2 = threading.Thread(target=write_data, args=("thread-2",))
    t3 = threading.Thread(target=get_data, args=("thread-3",))
    #t4 = threading.Thread(target=write_data, args=("thread-4",))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    #threads.append(t4)
    
    if __name__ == '__main__':
        for t in threads:
            t.start()
    
    for t in threads:
        t.join()
    
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
