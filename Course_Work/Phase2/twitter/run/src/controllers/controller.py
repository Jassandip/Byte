#!/usr/bin/env python3

from flask import Flask,render_template,request,session,Blueprint,redirect,url_for

from src.model import model
import sqlite3

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
        if model.check_username(username):
            session['username'] = username
            model.sign_up(username,password)
            model.add_friend(session['username'],session['username'])
            return redirect('/dashboard')
        else:
            message = "That username is already taken, try again!"
            return render_template('signup.html',message=message)

@controller.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if request.method == 'GET':
        dump = model.dump()
        friends = model.get_friends(session['username'])
        return render_template('dashboard.html',dump=dump,friends=friends,username=session['username'])
    elif request.method == 'POST':
        friends = model.get_friends(session['username'])
        tweet = request.form["tweet"]
        try:
            model.tweet(session['username'],tweet)
            dump = model.dump()
            return render_template('dashboard.html',dump=dump,friends=friends,username=session['username'])
        except:
            message="Your tweet syntax broke my system, nice"
            return render_template('404.html',message=message,username=session['username'])
            

        
@controller.route('/addfriend',methods=['GET','POST'])
def addfriend():
    if request.method == 'GET':
        message = '{} lets add some friends'.format(session['username'])
        users = model.get_users(session['username'])
        return render_template('addfriend.html',message=message,username=session['username'],users=users)
    elif request.method == 'POST':
        message = "There is no person by that name"
        users = model.get_users(session['username'])
        return render_template('addfriend.html',message=message,username=session['username'],users=users)




@controller.route('/profile',methods=['GET','POST'])
def profile():
    if request.method == 'GET':
        friend = session['friends']
        message = "You are now following {}!".format(friend)
        model.add_friend(session['username'],friend)
        tweets = model.get_tweets(friend)
        return render_template('profile.html',message=message,tweets=tweets,username=session['username'])
    elif request.method == 'POST':
        msg = request.form['search']
        if model.check_user(session['username'],msg):
            session['friends'] = msg
            tweets = model.get_tweets(msg)
            show = True 
            return render_template('profile.html',msg=msg,message=msg,tweets=tweets,username=session['username'],show=show)
        else: 
            message = "There is no person by that name to follow"
            show = False
            return render_template('profile.html',message=message,username=session['username'],show=show)
            

@controller.route('/killboard',methods=['GET','POST'])
def killboard():
    if request.method == 'GET':
        message = 'R.I.P.'
        users = model.get_users(session['username'])
        return render_template('killboard.html',message=message,users=users,username=session['username'])
    elif request.method == 'POST':
        user = request.form["user"]
        model.delete_user(user)
        users = model.get_users(session['username'])
        message = 'R.I.P.'
        return render_template('killboard.html',message=message,users=users,username=session['username'])

