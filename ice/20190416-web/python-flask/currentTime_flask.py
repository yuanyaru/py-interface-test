#!/usr/bin/pythoni
#-*- coding:utf-8 -*-

from flask import Flask, render_template
import time

app = Flask(__name__)
  
@app.route("/")
def job_2():
    ctime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
    #print(ctime)
    #return ctime
    return render_template('flask_time.html', ctime = ctime)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')    
