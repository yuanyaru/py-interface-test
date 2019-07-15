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
    datetime = "20190416"
    yxdata = []
    for i in range(1000):
        pIDs.append(0)
        structyxdata = YXArea.DxDTYX(i, i+1, i)
        yxdata.append(structyxdata)
      
        DataCommand.RPCSaveYXData(pIDs, yxdata)
    
    pID = 0
    print("........遥信数据读取start.......")
    start = time.time()
    yxdata = DataCommand.RPCGetDayYXData (datetime, pID)
    elapsed = (time.time() - start)
    print("read yxdata time use: %s " % elapsed)
    print("总计读取遥信数据：%d " % len(yxdata))

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
