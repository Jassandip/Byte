#!/usr/bin/env python3

from flask import Flask,render_template,request,session,Blueprint,redirect,url_for

from src.model import model

controller = Blueprint('public',__name__)


@controller.route('/',methods=['GET'])
def hompepage():
    dump = model.dump()
    return render_template('index.html',dump=dump)
        


@controller.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        message = 'Welcome to toot'
        return render_template('login.html',message=message)
    elif request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        try:
            saved_password = model.user_check(username)
            if saved_password == password:
                session['username'] = username
                try:
                    return redirect('/dashboard')
                except:
                    return redirect(url_for("dashboard"))
        except:
            message = "Invalid username. Please try another again or sign up"
            return render_template('login.html',message=message)


@controller.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        message = 'Welcome to toot'
        return render_template('signup.html',message=message)
    elif request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        session['username'] = username
        model.sign_up(username,password)
        model.add_friend(session['username'],friend)
        return redirect('/dashboard')

@controller.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        dump = model.dump()
        friends = model.get_friends(session['username'])
        print(friends)
        print(dump)
        return render_template('dashboard.html',dump=dump,friends=friends)
    elif request.method == 'POST':
        friends = model.get_friends(session['username'])
        tweet = request.form["tweet"]
        model.tweet(session['username'],tweet)
        dump = model.dump()
        return render_template('dashboard.html',dump=dump,friends=friends)
        
@controller.route('/addfriend',methods=['GET','POST'])
def addfriend():
    if request.method == 'GET':
        message = '{} lets add some friends'.format(session['username'])
        return render_template('addfriend.html',message=message)
    elif request.method == 'POST':
        friend = request.form["friend"]
        #try:
        model.add_friend(session['username'],friend)
        message = "Congratulations, {} is your friend now!".format(friend)
        return render_template('addfriend.html',message=message)
        #except:
        #    message = "Something went wrong with the buy function"
        #    return render_template('buy.html',message=message)

@controller.route('/profile',methods=['GET','POST'])
def profile():
    if request.method == 'GET':
        friend = session['friends']
        print(1)
        print(friend)
        message = "You are now following {}!".format(friend)
        model.add_friend(session['username'],friend)
        return render_template('profile.html',message=message)
    elif request.method == 'POST':
        msg = request.form['search']
        session['friends'] = msg
        print(msg)
        message = "{} do you want to follow {}?".format(session['username'],msg)
        return render_template('profile.html',msg=msg,message=msg)
        #except:
        #    message = "Something went wrong with the buy function"
        #    return render_template('buy.html',message=message)














@controller.route('/sell',methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        message = 'What do you wanna sell {}?'.format(session['username'])
        return render_template('sell.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        trade_volume = request.form["quantity"]
        message = model.sell(session['username'],ticker,trade_volume)
        return render_template('sell.html',message=message)

@controller.route('/lookup',methods=['GET','POST'])
def lookup():
    if request.method == 'GET':
        message = 'What do you wanna to look up {}?'.format(session['username'])
        return render_template('lookup.html',message=message)
    elif request.method == 'POST':
        ticker = request.form["ticker"]
        message = model.lookup(ticker)
        return render_template('lookup.html',message=message)

