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
    ycdata = []
    for i in range(5):
        pIDs.append(0)
        structycdata = YCArea.DxDTYC(i, i+2.1, i)
        ycdata.append(structycdata)
    #print(ycdata)
    
    pID=0
    datetime1 = "20190410000000"
    datetime2 = "20190412180000"
    datetime = "20190412"
    """
    print("........Redis遥测数据写入start.......")
    start = time.time()
    DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
    elapsed = (time.time() - start)
    print("redis write ycdata time use: %s " % elapsed)
    
    print("........Cassandra遥测数据写入start.......")
    start = time.time()
    DataCommand.RPCSaveYCData(pIDs, ycdata)
    elapsed = (time.time() - start)
    print("cassandra write ycdata time use: %s " % elapsed)
    """
    print("........Redis遥测数据读取start.......")
    start = time.time()
    ycdata = DataCommand.RPCGetRealtimeYCData (pIDs)
    elapsed = (time.time() - start)
    print("redis read ycdata time use: %s " % elapsed)
    print("总计读取遥测数据：%d " % len(ycdata))
    
    #ycdata = DataCommand.RPCGetPeriodYCData(datetime1, datetime2, pID)
    #ycdata = DataCommand.RPCGetDayYCData (datetime, pID)
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
