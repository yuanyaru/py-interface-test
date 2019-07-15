#!/usr/bin/python
#-*- coding:utf-8 -*-

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
        ycdata = []
        for i in range(1000):
            pIDs.append(i)
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
        
        print("........redis开始写入遥测数据.......")
        start = time.time()
        # 多点写入redis
        ycstatus = DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
        rediswrite = (time.time() - start)
        print("redis write 1k time use: %s " % rediswrite)
        print(ycstatus)
        
        print("........cassandra开始写入遥测数据.......")
        start = time.time()
        # 多点写入cassandra
        ycstatus = DataCommand.RPCSaveYCData (pIDs, ycdata)
        cassandrawrite = (time.time() - start)
        print("cassandra write 1k time use: %s " % cassandrawrite)
        print(ycstatus)
        
        print("........redis开始读取遥测数据.......")
        start = time.time()
        # 实时数据读取
        ycstatus,ycdata = DataCommand.RPCGetRealtimeYCData (pIDs)
        redisread = (time.time() - start)
        print("redis read 1k time use: %s " % redisread)
        print(ycstatus)
        print("总计读取遥测数据：%d " % len(ycdata))
        
        for i in range(len(ycdata)):
            print(ycdata[i].status, ycdata[i].value, ycdata[i].timetag)
        
        return "redis写1k个点需要时间: " + str(rediswrite)+ "<br><br>" + "cassandra写1k个点需要时间 :" + str(cassandrawrite) + "<br><br>" + "redis读1k个点需要时间: " + str(redisread) + "<br><br>"+ "读取的遥测数据如下: " + "<br><br>" + str(ycdata)

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
