#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, YCArea

status = 0
ic = None

name = []
unit = []
for i in range(41):
    name.append(i+10)
    #print(name[i])
for i in range(11):
    unit.append(i+10)
    #print(unit[i])
structycproperty = YCArea.DxPropertyYC(name, unit, 1.1, 1.2, 1, 2.1, 2.1, 2.3, 10, 11,12, True, False, True, True, True, False, False, False, True, False, True, 20, True, False, 30, 31, 3.1, 3.2, 3.3, 3.4)

try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
    DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
    if not DataCommand:
        raise RuntimeError("Invalid proxy")
	
    #DataCommand.RPCSetYCProperty(structycproperty, 1)
    structycproperty = DataCommand.RPCGetYCProperty(1)
    print("读取的遥测属性name：%s " % name[40])
    print("读取的遥测属性unit: %s " % unit[10])
    print("读取的遥测属性k：%s " % structycproperty.k)
    print("读取的遥测属性b：%s " % structycproperty.b)
    print("读取的遥测属性precision：%s" % structycproperty.precision)
    print("读取的遥测属性fullvalue：%s " % structycproperty.fullvalue)
    print("读取的遥测属性mindelta：%s " % structycproperty.mindelta)
    print("读取的遥测属性zerovalue：%s " % structycproperty.zerovalue)
    print("读取的遥测属性flog：%s " % structycproperty.flog)
    print("读取的遥测属性fplan：%s " % structycproperty.fplan)
    print("读取的遥测属性fcache：%s " % structycproperty.fcache)
    print("读取的遥测属性fTrans：%s " % structycproperty.fTrans)
    print("读取的遥测属性fMin：%s " % structycproperty.fMin)
    print("读取的遥测属性fMax：%s " % structycproperty.fMax)
    print("读取的遥测属性fAvrg：%s " % structycproperty.fAvrg)
    print("读取的遥测属性fRatio：%s " % structycproperty.fRatio)
    print("读取的遥测属性fUpper：%s " % structycproperty.fUpper)
    print("读取的遥测属性fLower：%s " % structycproperty.fLower)
    print("读取的遥测属性fUpper2：%s " % structycproperty.fUpper2)
    print("读取的遥测属性fLower2：%s " % structycproperty.fLower2)
    print("读取的遥测属性fMinTime：%s " % structycproperty.fMinTime)
    print("读取的遥测属性fMaxTime：%s " % structycproperty.fMaxTime)
    print("读取的遥测属性padding：%s " % structycproperty.padding)
    print("读取的遥测属性fMax2：%s " % structycproperty.fMax2)
    print("读取的遥测属性fMaxTime2：%s " % structycproperty.fMaxTime2)
    print("读取的遥测属性yxno：%s " % structycproperty.yxno)
    print("读取的遥测属性alevel：%s " % structycproperty.alevel)
    print("读取的遥测属性uppervalue：%s " % structycproperty.uppervalue)
    print("读取的遥测属性lowervalue：%s " % structycproperty.lowervalue)
    print("读取的遥测属性uppervalue2：%s " % structycproperty.uppervalue2)
    print("读取的遥测属性lowervalue2：%s " % structycproperty.lowervalue2)
	
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
