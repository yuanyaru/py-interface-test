#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, YXArea

status = 0
ic = None

name = []
for i in range(41):
    name.append(i+10)
    #print(name[i])
structyxproperty = YXArea.DxPropertyYX(name, True, False, 255, 12, 13, 14, 15)

try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
	
    station = 1
    #yxpropertystatus = DataCommand.RPCSetYXProperty(structyxproperty, station)
    #print yxpropertystatus
    yxpropertystatus,structycproperty = DataCommand.RPCGetYXProperty(station)
    print(yxpropertystatus)
    print("读取的遥信属性name：%s " % name[40])
    print("读取的遥信属性fAlarm：%s " % structyxproperty.fAlarm)
    print("读取的遥信属性fAlarmCount：%s " % structyxproperty.fAlarmCount)
    print("读取的遥信属性unused：%s" % structyxproperty.unused)
    print("读取的遥信属性reserved：%s " % structyxproperty.reserved)
    print("读取的遥信属性ykno：%s " % structyxproperty.ykno)
    print("读取的遥信属性alarmtype：%s " % structyxproperty.alarmtype)
    print("读取的遥信属性alevel：%s " % structycproperty.alevel)
	
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
