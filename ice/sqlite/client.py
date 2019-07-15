#!/usr/bin/python
# encoding:utf-8

import sys, traceback, Ice
Ice.loadSlice("./sqliteIce.ice")
import SqliteICE

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("Kafka:default -h 192.168.100.168 -p 10000")
    DataOperateA = SqliteICE.DataOperatePrx.checkedCast(base)
    if not DataOperateA:
        raise RuntimeError("Invalid proxy")
    pIDs = [i for i in range(1,13)]
    reval, data, max, min, average = DataOperateA.tableSelectOneday (pIDs, "2019-05-25");
    
    print(reval)
    print(data)
    print(max)
    print(min)
    print(average)
        
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
