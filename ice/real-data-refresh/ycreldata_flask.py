# !/usr/bin/python
# encoding:utf-8

from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock
from socket import *
import time
from iceCon import ice_con
import Ice
Ice.loadSlice("./ice-redis.ice")
import YCArea

async_mode = None
app = Flask(__name__)
app.threaded = True
app.config['SECRET_KEY'] = 'secret!'

thread = None
thread_lock = Lock()

socketio = SocketIO(app, async_mode=async_mode)


def background_thread():
    # print("线程启动！")
    DataCommand = ice_con()
    while True:
        socketio.sleep(1)
        pIDs = []
        ycdata = []
        for i in range(1000):
            pIDs.append(i)
            structycdata = YCArea.DxDTYC(i, i+1.1, i)
            ycdata.append(structycdata)

        print("........开始写入遥测数据.......")
        start = time.time()
        # 写入redis
        # DataCommand.RPCSetRealtimeYCData(pIDs, ycdata)
        # 写入cassandra
        DataCommand.RPCSaveYCData(pIDs, ycdata)
        elapsed = time.time() - start
        print("write time use: %s " % elapsed)

        print("........开始读取遥测最新数据.......")
        start = time.time()
        ycstatus, ycdata = DataCommand.RPCGetRealtimeYCData(pIDs)
        elapsed = time.time() - start
        print("read time use: %s " % elapsed)
        print(ycstatus)
        ycdatanum = len(ycdata)
        print("总计读取遥测数据：%d " % ycdatanum)
        """
        for i in range(len(ycdata)):
            print(ycdata[i].status, ycdata[i].value, ycdata[i].timetag)
        """
        # print(ycdata)
        data0 = [elapsed, ycdatanum]
        data1 = []
        for i in range(len(ycdata)):
            data1.append({'status': ycdata[i].status,
                          'value': ycdata[i].value,
                          'timetag': ycdata[i].timetag})
        data = [data0, data1]
        socketio.emit('server_response', 
                      data,
                      namespace='/test')


@app.route('/')
def index():
    # print("渲染界面！")
    return render_template('ycRelData_flask.html', async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def test_connect():
    # print("查看线程！")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    socketio.run(app, port=5001)
