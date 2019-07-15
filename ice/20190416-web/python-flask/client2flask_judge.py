#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock
from socket import *
import sys, traceback, Ice
Ice.loadSlice("./ice-redis.ice")
import CommandArea, DemoArea, YCArea

async_mode = None

app = Flask(__name__)
app.threaded=True
app.config['SECRET_KEY'] = 'secret!'

thread = None
thread_lock = Lock()

socketio = SocketIO(app, async_mode=async_mode)

def background_thread():
    #print("线程启动！")
    while True:
        socketio.sleep(3)

        status = 0
        ic = None
            
        ic = Ice.initialize(sys.argv)
        base = ic.stringToProxy("DataCommand:default -h 192.168.100.170 -p 10000")
        DataCommand = CommandArea.DataCommandPrx.checkedCast(base)
        if not DataCommand:
            raise RuntimeError("Invalid proxy")
        
        pID = 0
        datetime = "20190520"

        ycstatus,ycdata0 = DataCommand.RPCGetDayYCData (datetime, pID)
        ycdatanum0 = len(ycdata0)    
        print("第一次读取遥测数据：%d " % ycdatanum0)
        data0 = [ycdatanum0]
        data1 = []
        for i in range(ycdatanum0):
            data1.append({'status': ycdata0[i].status, 'value': ycdata0[i].value, 'timetag': ycdata0[i].timetag})
        data = [data0, data1]
        socketio.emit('server_response',
                          data,
                          namespace='/test')
        
        pIDs = []
        pIDs.append(0)
        ycdata = []
        for i in range(1000):
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)
            
            # 写入redis
            DataCommand.RPCSetRealtimeYCData (pIDs, ycdata)
            # 写入cassandra
            DataCommand.RPCSaveYCData (pIDs, ycdata)
            DataCommand.RPCGetRealtimeYCData(pIDs)
            ycdata.pop()
        
        ycstatus,ycdata = DataCommand.RPCGetDayYCData (datetime, pID)
        ycdatanum = len(ycdata)
        print("第二次读取遥测数据：%d " % ycdatanum)
        
        if ycdatanum > ycdatanum0:
            print("数据有更新，再次提交！")
            data0 = [ycdatanum]
            data1 = []
            for i in range(ycdatanum):
                data1.append({'status': ycdata[i].status, 'value': ycdata[i].value, 'timetag': ycdata[i].timetag})
            data = [data0, data1]
            socketio.emit('server_response', 
                          data,
                          namespace='/test')
                

@app.route('/')
def index():
    #print("渲染界面！")
    return render_template('ycdaydata_flask_judge.html', async_mode=socketio.async_mode)

@socketio.on('connect',namespace='/test')
def test_connect():
    #print("查看线程！")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port = 5000, debug=True)    
