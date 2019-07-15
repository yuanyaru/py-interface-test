#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import time
from flask_socketio import SocketIO
from threading import Lock
from socket import *

async_mode = None

app = Flask(__name__)
app.threaded=True
app.config['SECRET_KEY'] = 'secret!'

thread = None
thread_lock = Lock()

socketio = SocketIO(app, async_mode=async_mode)

def background_thread():
    print("线程启动！")
    while True:
        socketio.sleep(2)
        data = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
        # print(data)
        socketio.emit('server_response', data,
                          namespace='/test')
        
@app.route('/')
def index():
    print("渲染界面！")
    return render_template('websocket_time.html', async_mode=socketio.async_mode)

@socketio.on('connect',namespace='/test')
def test_connect():
    print("查看线程是否启动！")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port = 5000, debug=True)    
