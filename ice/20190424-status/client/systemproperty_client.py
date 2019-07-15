#!/usr/bin/python2
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, SystemArea

status = 0
ic = None

name = []
nstation = 1
for i in range(80):
    name.append(i+10)
    #print(name[i])
#print(name)
structsystem = SystemArea.DxPropertySystem(name, nstation)

try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
	
    systemstatus = DataCommand.RPCSetSystemProperty(structsystem)
    print(systemstatus)
    systemstatus,structsystem = DataCommand.RPCGetSystemProperty()
    print(systemstatus)
    print("读取的系统属性：%s %s " % (name[79], structsystem.nstation))

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
