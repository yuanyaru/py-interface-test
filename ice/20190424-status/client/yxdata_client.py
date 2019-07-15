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
    datetime1 = "20190412000000"
    datetime2 = "20190424180000"
    datetime = "20190424120000"
    datetime0 = "20190424"
    
    # redis写入遥信数据
    #yxstatus = DataCommand.RPCSaveYXData(pIDs, yxdata)
    #print(yxstatus)
    # 实时数据读取
    #yxstatus,yxdata = DataCommand.RPCGetRealtimeYXData (pIDs)
    # 时间点数据读取
    #yxstatus,yxdata = DataCommand.RPCGetTimePointYXData (datetime, pIDs)
    # 单点某天全部数据读取
    #yxstatus,yxdata = DataCommand.RPCGetDayYXData (datetime0, pID)
    # 多点某天全部数据读取
    #yxstatus,pIDNum,yxdata = DataCommand.RPCGetDayYXDatas (datetime0, pIDs)
    # 单点时间段数据获取函数
    yxstatus,yxdata = DataCommand.RPCGetPeriodYXData(datetime1, datetime2, pID)
    print(yxstatus)
    #print(pIDNum) 
    
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
