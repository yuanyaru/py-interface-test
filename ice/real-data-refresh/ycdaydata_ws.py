# !/usr/bin/python
# encoding:utf-8

from flask import Flask, render_template
from flask_socketio import SocketIO
from apscheduler.schedulers.background import BackgroundScheduler
from iceCon import ice_con
import time
import Ice
Ice.loadSlice("./ice-redis.ice")
import YCArea

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('ycDayData_ws.html')


@socketio.on('connect')
def handle_connect():
    socketio.emit('server_response', 'success!')


@socketio.on('my event')
def handle_custom_event(json):
    print("received custom event from client: " + str(json))
    # while True:
    socketio.sleep(3)
    data = load_real_data()
    print("send message: " + str(data))
    socketio.emit('server_response', data)


def load_real_data():
    DataCommand = ice_con()
    """
    pIDs = []
    pIDs.append(0)
    ycdata = []
    for i in range(1000):
        structycdata = YCArea.DxDTYC(i, i + 1.1, i)
        ycdata.append(structycdata)

        # 写入redis
        DataCommand.RPCSetRealtimeYCData(pIDs, ycdata)
        # 写入cassandra
        DataCommand.RPCSaveYCData(pIDs, ycdata)
        DataCommand.RPCGetRealtimeYCData(pIDs)
        ycdata.pop()
    """

    pID = 0
    datetime = "20190527"
    print("........开始获取遥测当天数据.......")
    start = time.time()
    ycstatus, ycdata = DataCommand.RPCGetDayYCData(datetime, pID)
    elapsed = time.time() - start
    print("read time use: %s " % elapsed)
    ycdatanum = len(ycdata)
    # print(ycstatus)
    # print("总计读取遥测数据：%d " % ycdatanum)
    data0 = [elapsed, ycdatanum]
    data1 = []
    for i in range(len(ycdata)):
        data1.append({'status': ycdata[i].status,
                      'value': ycdata[i].value,
                      'timetag': ycdata[i].timetag})
    data = [data0, data1]
    return data


def generate_and_send_message():
    data = load_real_data()
    socketio.emit('server_response', data)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_and_send_message, 'interval', seconds=2)
    scheduler.start()
    socketio.run(app)

