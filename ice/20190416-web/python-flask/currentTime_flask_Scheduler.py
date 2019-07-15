#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import request, json
from flask_apscheduler import APScheduler
import time

class Config(object):  # 创建配置，用类
    JOBS = [  # 任务列表
        {  # 第一个任务，每隔3S执行一次
            'id': 'job2',
            'func': '__main__:job_1',
            'trigger': 'interval',
            'seconds': 3,
        },

    ]

app = Flask(__name__)
# 为实例化的flask引入配置
app.config.from_object(Config())
  
@app.route("/")
def job_1():
    ctime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    print(ctime)
    return render_template('flask_time1.html',ctime = ctime)
 
if __name__ == '__main__':
    scheduler=APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0')    
