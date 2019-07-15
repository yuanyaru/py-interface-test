#!/usr/bin/python2
#-*-coding:utf-8-*-

import sys, traceback, Ice, time
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.24 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
        
    pIDs = []
    ycdata = []
    for i in range(10000):
        pIDs.append(i)
        structycdata = YCArea.DxDTYC(i, i+1.1, i)
        ycdata.append( structycdata )
#	print(ycdata[0].value)

    print("........遥测数据写入start.......")
    start = time.time()
    DataCommand.RPCSetRealtimeYCData(pIDs,ycdata)
    elapsed = (time.time() - start)
    print("write ycdata time use: %s " % elapsed)

    print("........遥测数据读取start.......")
    start = time.time()
    ycdata = DataCommand.RPCGetRealtimeYCData(pIDs)
    elapsed = (time.time() - start)
    print("read ycdata time use: %s " % elapsed)
    print("总计读取遥测数据：%d " % len(ycdata))

    print("读取的第9999个遥测数据：%d %f %d " % (ycdata[9999].status, ycdata[9999].value, ycdata[9999].timetag))
#	for i in range(10000):
#		print("读取的遥测数据：%d %f %d " % (ycdata[i].status, ycdata[i].value, ycdata[i].timetag))

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
