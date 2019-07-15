#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YXArea
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
    yxdata = []
    for i in range(5):
        pIDs.append(i)
        structyxdata = YXArea.DxDTYX(i, i+10, i)
        yxdata.append(structyxdata)
    #print(ycdata)
    
    pID=1
    datetime1 = "20190415000000"
    datetime2 = "20190416180000"
    datetime = "20190416"
    
    print("........Redis遥信数据写入start.......")
    start = time.time()
    DataCommand.RPCSaveYXData(pIDs, yxdata)
    elapsed = (time.time() - start)
    print("redis write yxdata time use: %s " % elapsed)

    print("........Redis遥测数据读取start.......")
    start = time.time()
    yxdata = DataCommand.RPCGetRealtimeYXData (pIDs)
    elapsed = (time.time() - start)
    print("read yxdata time use: %s " % elapsed)
    print("总计读取遥信数据：%d " % len(yxdata))
    
    yxdata = DataCommand.RPCGetPeriodYXData(datetime1, datetime2, pID)
    #yxdata = DataCommand.RPCGetDayYXData (datetime, pID)
    for i in range(len(yxdata)):
        print(yxdata[i].status, yxdata[i].value, yxdata[i].timetag)

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
