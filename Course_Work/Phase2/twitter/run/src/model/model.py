#!/usr/bin/env python3

import json

from src.mapper.mapper import Database 
from src.wrapper.wrapper import Markit
from datetime import datetime

import requests

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

















        












