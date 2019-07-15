#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import time
from flask_socketio import SocketIO, emit
from threading import Lock
from socket import *
import threading

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
        socketio.sleep(2)

        a = 0.5
        b = 100
        data1 = [a,b]

        data2 = []
        d1 = {
            'status': 1,
            'value': 1.10000002384,
            'timetag': 1
        }
        d2 = {
            'status': 2,
            'value': 2.10000002384,
            'timetag': 2
        }
        data2.append(d1)
        data2.append(d2)
        socketio.emit('server_response', data2,
                          namespace='/test')
        
@app.route('/')
def index():
    #print("渲染界面！")
    return render_template('test.html', async_mode=socketio.async_mode)

@socketio.on('connect',namespace='/test')
def test_connect():
    #print("查看线程！")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port = 5000, debug=True)    
