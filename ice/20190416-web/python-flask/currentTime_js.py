#!/usr/bin/python
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import time
app = Flask(__name__)
@app.route("/")

def hello():
     
    #CurrentTime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    #return "当前时间：" + str(CurrentTime)
 
    return render_template('time.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
