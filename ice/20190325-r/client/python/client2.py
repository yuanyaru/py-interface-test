#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, traceback, Ice, time
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YXArea, YCArea

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.24 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
        
    pIDs = []
    yxdata = []
    for i in range(10000):
        pIDs.append(i)
        structyxdata = YXArea.DxDTYX(i, i+1, i)
        yxdata.append( structyxdata )
	#print(yxdata[0].value)

    for i in range(1000):        
        print("........遥信数据第 %d 次写入start......." % i)
	start = time.time()
	DataCommand.RPCSaveYXData(pIDs,yxdata)
	elapsed = (time.time() - start)
	print("write yxdata time use: %s " % elapsed)
	
	print("........遥信数据读取第 %d 次start......." % i)
	start = time.time()
	yxdata = DataCommand.RPCGetRealtimeYXData(pIDs)
	elapsed = (time.time() - start)
	print("read yxdata time use: %s " % elapsed)
	print("总共读取遥信数据：%d" % len(yxdata))

#	print("读取的第9999个遥信：%d %d %d " % (yxdata[9999].status, yxdata[9999].value, yxdata[9999].timetag))
#	for i in range(30000):
#		print("读取的遥信：%d %d %d " % (yxdata[i].status, yxdata[i].value, yxdata[i].timetag))

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
