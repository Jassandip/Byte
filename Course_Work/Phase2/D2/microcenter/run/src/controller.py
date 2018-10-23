#!/usr/bin/env python3

from flask import FLask,render_template

import model

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        pass

@app.route('/phones/iphones-<',methods=['GET','POST'])
def iphone(version):
    stock = [5,6,7,8]
    if int(version) in stock:
        return render_template('index.html',version=_version)
    else:
        error_message: = 'That item is not in stock'
        return render_template('404.html',message=error_message)

@app.route('/',methods=['GET','POST'])
def f():
    pass


if __name__=='__main__':
    app.run(debug=True)
