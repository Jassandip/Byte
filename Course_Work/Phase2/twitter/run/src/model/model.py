#!/usr/bin/env python3

import json

from src.mapper.mapper import Database 
from datetime import datetime


def sign_up(username,password):
    with Database('master.db') as db:
        db.sign_up(username,password)

def user_check(username):
    with Database('master.db') as db:
        username = db.user_check(username)
        return username

def get_friends(username):
    with Database('master.db') as db:
        rough = db.get_friends(username)
    friends = []    
    for row in rough:
        friends.append(row[0])
    return friends                   

def add_friend(username,friend):
    with Database('master.db') as db:
        return db.add_friend(username,friend)

def tweet(username,tweet):
    with Database('master.db') as db:
        db.insert_3('tweets','username','tweet','date',username,tweet,datetime.now())

def dump():
    with Database('master.db') as db:
        return db.dump()
        
def newsfeed(username):
    with Database('master.db') as db:
        return db.newsfeed(username)

def get_users(username):
    with Database('master.db') as db:
        return db.get_users(username)

def delete_user(username):
    with Database('master.db') as db:
        return db.delete_user(username)
        
def get_tweets(username):
    with Database('master.db') as db:
        return db.get_tweets(username)

def check_user(looker,lookie):
    with Database('master.db') as db:
        users = db.get_users(looker)
    users1 = []
    for row in users:
        users1.append(row[0])
    print(users1)
    if lookie in users1:
        return True
    else:
        return False 

def check_username(username):
    with Database('master.db') as db:
        usernames = db.usernames()
    usernames1 = []
    print(usernames1)
    for row in usernames:
        usernames1.append(row[0])
    if username not in usernames1:
        return True
    else:
        return False

        

















        












