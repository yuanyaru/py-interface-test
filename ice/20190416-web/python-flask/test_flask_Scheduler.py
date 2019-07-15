#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import request, json
from flask_apscheduler import APScheduler
import time

class Config(object):  # 创建配置，用类
    JOBS = [  # 任务列表
        {  # 第一个任务，每隔1S执行一次
            'id': 'job1',
            'func': '__main__:job_1',
            'trigger': 'interval',
            'seconds': 1,
        },
        {  # 第二个任务，每隔2S执行一次
            'id': 'job2',
            'func': '__main__:job_2',
            'trigger': 'interval',
            'seconds': 2,
        },

    ]

def job_1():
    CurrentTime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    #print("当前时间：%s" %CurrentTime)

app = Flask(__name__)
# 为实例化的flask引入配置
app.config.from_object(Config())
  
@app.route("/", methods=['GET','POST'])
def job_2():
    CurrentTime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    ctime = "%s" %CurrentTime
    print(ctime)
    return ctime
 
if __name__ == '__main__':
    scheduler=APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0')    
