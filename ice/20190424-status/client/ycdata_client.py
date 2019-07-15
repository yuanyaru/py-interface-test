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
    # 单点id赋值
    pIDs.append(0)
    ycdata = []
    for i in range(3):
        # 多点id赋值
        #pIDs.append(i)
        structycdata = YCArea.DxDTYC(i, i+1.1, i)
        ycdata.append(structycdata)
        
        # 单点写入redis
        ycstatus = DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
        #print(ycstatus)
        # 单点写入cassandra
        ycstatus = DataCommand.RPCSaveYCData (pIDs, ycdata)
        #print(ycstatus)
        ycdata.pop()
        
    """
    # 多点写入redis
    ycstatus = DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
    print(ycstatus)
    # 多点写入cassandra
    ycstatus = DataCommand.RPCSaveYCData (pIDs, ycdata)
    print(ycstatus)
    """ 

    # 实时数据读取
    ycstatus, ycdata = DataCommand.RPCGetRealtimeYCData (pIDs)
    datetime = "20190424120000"
    # 时间点数据读取
    #ycstatus, ycdata = DataCommand.RPCGetTimePointYCData (datetime,pIDs)
    pID = 0
    datetime = "20190425"
    datetime0 = "20190424080000"
    datetime1 = "20190424180000"
    # 单点某天全部数据读取
    #ycstatus, ycdata = DataCommand.RPCGetDayYCData (datetime, pID)
    print("........开始获取遥测当天数据.......")
    start = time.time()
    # 多点某天全部数据读取
    #ycstatus, pIDNum, ycdata = DataCommand.RPCGetDayYCDatas (datetime, pIDs)
    elapsed = (time.time() - start)
    print("time use: %s " % elapsed)
    # 单点某天的最大最小和平均值
    #ycstatus, max, min, average = DataCommand.RPCGetProcessYCData (datetime, pID)
    #print("........开始计算遥测数据最大最小平均值.......")
    #start = time.time()
    # 多点某天的最大最小和平均值
    #ycstatus, maxseq, minseq, averageseq = DataCommand.RPCGetProcessYCDatas (datetime, pIDs)
    #elapsed = (time.time() - start)
    #print("time use: %s " % elapsed)
    # 单点时间段数据
    #ycstatus, ycdata = DataCommand.RPCGetPeriodYCData (datetime0, datetime1, pID)
    print(ycstatus)
    #print(pIDNum)
    #print("最大值：%s, 最小值：%s，平均值：%s " %(max,min,average))
    #print("最大值：%s, 最小值：%s，平均值：%s " %(maxseq,minseq,averageseq))
    
    
    print("总共读取遥测数据：%s个" %len(ycdata))
    for i in range(len(ycdata)):
        print(ycdata[i].status,ycdata[i].value,ycdata[i].timetag)
    

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
