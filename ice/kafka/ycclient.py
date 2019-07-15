#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./kafkaICE.ice")
import kafkaICE

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("Kafka:default -h 192.168.100.168 -p 10000")
    DataOperateA = kafkaICE.DataOperatePrx.checkedCast(base)
    if not DataOperateA:
        raise RuntimeError("Invalid proxy")
        
    for i in range(9,11):
        msg = "station1_YC" + str(i);
        #result = DataOperateA.KafkaLongConnectData("gongcheng", msg, "gmt")
        result = DataOperateA.KafkaProduceData("goncheng", "./log", "./config", msg, "gmt")
        if result == 0:
            print("产生数据失败：%d" %i)
        elif result == -1:
            print("主题不存在")
        else:
            print("发送成功！")    
        
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
