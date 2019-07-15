#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea
import time
# 导入flask库
from flask import Flask, render_template

# 创建一个 web app 对象
app = Flask(__name__)

# 装饰器：注册url,把路由映射到试图函数
@app.route("/")
# 试图函数，在浏览器上面进行数据展示
def hello():
    status = 0
    ic = None
    try:
        ic = Ice.initialize(sys.argv)
        base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
        DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
        if not DataCommand:
            raise RuntimeError("Invalid proxy")
        
        pIDs = []
        pIDs.append(0)
        ycdata = []
        for i in range(1000):
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
            
            # 写入redis
            #DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
            # 写入cassandra
            DataCommand.RPCSaveYCData (pIDs, ycdata)
            DataCommand.RPCGetRealtimeYCData(pIDs)
            ycdata.pop()
        
        pID = 0
        datetime = "20190520"
        print("........开始获取遥测当天数据.......")
        start = time.time()
        ycstatus,ycdata = DataCommand.RPCGetDayYCData (datetime, pID)
        elapsed = (time.time() - start)
        print("time use: %s " % elapsed)
        print(ycstatus)
        print("总计读取遥测数据：%d " % len(ycdata))
        """
        for i in range(len(ycdata)):
            print(ycdata[i].status, ycdata[i].value, ycdata[i].timetag)
        """
        #return "读取单点某天全部数据需要时间：" + str(elapsed) + "<br><br>" + "总共读取遥测数据：" + str(len(ycdata)) + "<br><br>" + "读取的遥测数据如下：" + "<br><br>" + str(ycdata)
        return render_template('ycdaydata_js.html', elapsed = elapsed, ycdatanum = len(ycdata), ycdataval = ycdata )

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
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
