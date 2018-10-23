#!/usr/bin/env python3

import json

from mapper import Database 

import requests

def sign_up(username,password):
    with Database('master.db') as db:
        db.sign_up(username,password)






        












