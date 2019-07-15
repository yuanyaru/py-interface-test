#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea
import time
# 导入flask库
from flask import Flask

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
        for i in range(288):
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
            # 单点写入redis
            ycstatus = DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
            # 单点写入cassandra
            ycstatus = DataCommand.RPCSaveYCData (pIDs, ycdata)
            DataCommand.RPCGetRealtimeYCData(pIDs)
            ycdata.pop()
        

        pID = 0
        datetime = "20190513"
        
        # 单点某天全部数据读取
        ycstatus, ycdata = DataCommand.RPCGetDayYCData (datetime, pID)    

        print("........开始计算遥测数据最大最小平均值.......")
        start = time.time()
        # 单点某天的最大最小和平均值
        ycstatus, max, min, average = DataCommand.RPCGetProcessYCData (datetime, pID)
        elapsed = (time.time() - start)
        print("time use: %s " % elapsed)
    
        """
        print("........开始计算遥测数据最大最小平均值.......")
        start = time.time()
        # 多点某天的最大最小和平均值
        ycstatus, maxseq, minseq, averageseq = DataCommand.RPCGetProcessYCDatas (datetime, pIDs)
        elapsed = (time.time() - start)
        print("time use: %s " % elapsed)
        """
    
        print(ycstatus)
    
        print("最大值：%s, 最小值：%s，平均值：%s " %(max,min,average))
        #print("最大值：%s, 最小值：%s，平均值：%s " %(maxseq,minseq,averageseq))
    
        return "读取单点最大最小平均值需要时间：" + str(elapsed) + "<br><br>" +"总共读取遥测数据：" + str(len(ycdata)) + "<br><br>" + "最大值：" + str(max) + "<br><br>" + "最小值: " + str(min) + "<br><br>" + "平均值: " + str(average)

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
