#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea
import time

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
    datetime = "20190419"
    ycdata = []
    for i in range(2):
        structycdata = YCArea.DxDTYC(i, i+1.1, i)
        ycdata.append(structycdata)
       
        DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
        DataCommand.RPCSaveYCData(pIDs, ycdata)
        DataCommand.RPCGetRealtimeYCData(pIDs)
        ycdata.pop()
    
    pID = 0
    print("........遥测数据读取start.......")
    start = time.time()
    ycdata = DataCommand.RPCGetDayYCData (datetime, pID)
    #ycdata = DataCommand.RPCGetRealtimeYCData(pIDs)
    elapsed = (time.time() - start)
    print("read ycdata time use: %s " % elapsed)
    print("总计读取遥测数据：%d " % len(ycdata))
    for i in range(len(ycdata)):
        print(ycdata[i].status, ycdata[i].value, ycdata[i].timetag)
    
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
