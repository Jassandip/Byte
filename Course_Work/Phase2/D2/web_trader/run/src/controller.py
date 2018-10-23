#!/usr/bin/env python3

from flask import Flask,render_template,request,session 
import model


app = Flask(__name__)
app.secret_key = "could be any random string"

@app.route('/',methods=['GET','POST'])
def loggin():
    if request.method == 'GET':
        message = 'Welcome to web trader, time to make some $$'
        return render_template('loggin.html',message=message)
    elif request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        loggin = request.form["loggin"]
        if loggin == "Loggin":
            try:
                session['username'] = model.user_check(password)
                if session['username'] == username:
                    message = session['username'] 
                    return render_template('homepage.html',message=message)
            except:
                message = "Invalid username. Please try another again or sign up"
                return render_template('loggin.html',message=message)
        else:
            model.sign_up(username,password)
            message = 'Signed-up, now logg in with the same credentials'
            return render_template('loggin.html',message=message)

        


@app.route('/homepage',methods=['GET','POST'])
def hompepage():
    if request.method == 'GET':
        message = 'Welcome to web trader, time to make some $$'
        return render_template('homepage.html',message=message)
    elif request.method == 'POST':
        look_up = request.form["look_up"] 
        ticker = request.form["ticker"]
        trade_volume = request.form["quantity"]
        if look_up:
            message = model.lookup(look_up)
            return render_template('homepage.html',message=message)
        elif trade_volume:
            model.buy(session['username'],ticker,trade_volume) 
            message = "Congratulations you have purchased stuff"
            return render_template('homepage.html',message=message)
        else:
            message = "Come again?"
            return render_template('homepage.html',message=message)

@app.route('/buy',methods=['GET','POST'])
def buy():
    if request.method == 'GET':
        message = 'Make your purchases {}'.format(session['username'])
        return render_template('buy.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        trade_volume = request.form["quantity"]
        try:
            message = model.buy(session['username'],ticker,trade_volume) 
            return render_template('buy.html',message=message)
        except:
            message = "Something went wrong with the buy function"
            return render_template('buy.html',message=message)

@app.route('/sell',methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        message = 'What do you wanna sell {}?'.format(session['username'])
        return render_template('sell.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        trade_volume = request.form["quantity"]
        message = model.sell(session['username'],ticker,trade_volume)
        return render_template('sell.html',message=message)

@app.route('/lookup',methods=['GET','POST'])
def lookup():
    if request.method == 'GET':
        message = 'What do you wanna to look up {}?'.format(session['username'])
        return render_template('lookup.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        message = model.lookup(ticker)
        return render_template('lookup.html',message=message)

@app.route('/quote',methods=['GET','POST'])
def quote():
    if request.method == 'GET':
        message = 'What do you wanna get a quote of {}?'.format(session['username'])
        return render_template('quote.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        message = model.quote(ticker)
        return render_template('quote.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)
