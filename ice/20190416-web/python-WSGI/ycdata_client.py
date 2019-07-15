#-*- coding:utf-8 -*-
import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    status = 0
    ic = None
    try:
        ic = Ice.initialize(sys.argv)
        base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
        DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
        if not DataCommand:
            raise RuntimeError("Invalid proxy")
        
        pIDs = []
        ycdata = []
        for i in range(5):
            pIDs.append(i)
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
            DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
    
        ycstatus,ycdata = DataCommand.RPCGetRealtimeYCData (pIDs)
        print("总计读取遥测数据：%d " % len(ycdata))
        
       
        for i in range(len(ycdata)):
            print(ycdata[i].status, ycdata[i].value, ycdata[i].timetag)
        
        return str(ycdata)

    except:
        traceback.print_exc()
        status = 1

    if ic:
        try:
            ic.destroy()
        except:
            traceback.print_exc()
            status = 1    
