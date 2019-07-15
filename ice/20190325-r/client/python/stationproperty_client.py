#!/usr/bin/python2
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, StationArea

status = 0
ic = None

name = []
protocol = []
addr1 = []
addr2 = []
devName = []
for i in range(21):
    name.append(i+10)
    #print(name[i])
for i in range(21):
    protocol.append(i+20)
for i in range(16):
    addr1.append(i+30)
for i in range(16):
    addr2.append(i+40)
for i in range(32):
    devName.append(i+10)
structstationproperty = StationArea.DxPropertyStation(name, 10, 11, 1, protocol, addr1, addr2, 3006, 21, devName, 30, 31, 32, 255, 40, 41)

try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.24 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
	
    DataCommand.RPCSetStationProperty(structstationproperty)
    structstationproperty = DataCommand.RPCGetStationProperty()
    print("读取的厂站属性name：%s " % name[20])
    print("读取的厂站属性nYX：%s " % structstationproperty.nYX)
    print("读取的厂站属性nYC：%s " % structstationproperty.nYC)
    print("读取的厂站属性type：%s " % structstationproperty.type)
    print("读取的厂站属性protocol: %s " % protocol[20])
    print("读取的厂站属性addr1: %s " % addr1[15])
    print("读取的厂站属性addr2: %s " % addr2[15])
    print("读取的厂站属性port：%s " % structstationproperty.port)
    print("读取的厂站属性slaveAddr：%s " % structstationproperty.slaveAddr)
    print("读取的厂站属性devName: %s " % devName[31])
    print("读取的厂站属性baud：%s " % structstationproperty.baud)
    print("读取的厂站属性dataBits：%s " % structstationproperty.dataBits)
    print("读取的厂站属性stopBits：%s " % structstationproperty.stopBits)
    print("读取的厂站属性parity：%s " % structstationproperty.parity)
    print("读取的厂站属性timeout：%s " % structstationproperty.timeout)
    print("读取的厂站属性reserved：%s " % structstationproperty.reserved)
	
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
