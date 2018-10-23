#!/usr/bin/env python3

from flask import Flask,render_template,request
import model


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    if request.method == 'GET':
        message = 'Welcome to this website, please sign-up'
        return render_template('home_page.html',message=message)
    elif request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            model.sign_up(username,password)
            message = 'Signed-up'
            return render_template('home_page.html',message=message)
        else: 
            message = 'Please enter something valid'
            return render_template('home_page.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)
