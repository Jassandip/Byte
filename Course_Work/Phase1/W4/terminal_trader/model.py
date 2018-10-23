#!/usr/bin/env python3

import json

from mapper import Database 
from wrapper import Markit

import requests

def buy(user_id,ticker_symbol,trade_volume,price):
    with Database('master.db') as db:
        db.insert_4('orders','username','ticker_symbol','trade_volume','execution_price',user_id,ticker_symbol,trade_volume,-price)

def sell():
    pass

def lookup(company_name):
    #endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
    #response = json.loads(requests.get(endpoint).text)
    #return response[0]['Symbol']
    with Markit() as m:
        return m.lookup(company_name)

def quote(ticker_symbol):
    with Markit() as m:
        return m.quote(ticker_symbol)

def sign_up(username,password):
    with Database('master.db') as db:
        db.sign_up(username,password)

def user_check(password):
    with Database('master.db') as db:
        username = db.user_check(password)
        return username

def check_balance(user_id):
    with Database('master.db') as db:
        return db.check_balance(user_id)
3
def buy_holdings(user_name,ticker_symbol,trade_volume,price):
    with Database('master.db') as db:
        try:
            current = db.check_holdings(user_name,ticker_symbol)
            new_current = trade_volume + current 
            db.update_holding(user_name,ticker_symbol,new_current)
        except:
            db.new_holding(user_name,ticker_symbol,trade_volume,(price*trade_volume))

def update_cash(username,balance):
    with Database('master.db') as db:
        return db.update_cash(username,balance)

def sell_holdings(user_name,ticker_symbol,trade_volume,price,owned):
    with Database('master.db') as db:
        new_owned = owned - float(trade_volume) 
        db.update_holding(user_name,ticker_symbol,new_owned)
        balance = db.check_balance(user_name)
        new_balance = balance + (float(trade_volume)*float(price)) - 6.25
        db.update_cash(user_name,new_balance)
        db.insert_4('orders','username','ticker_symbol','trade_volume','execution_price',user_name,ticker_symbol,trade_volume,price)



def check_holdings(user_name,ticker_symbol):
    with Database('master.db') as db:
        try:
            return db.check_holdings(user_name,ticker_symbol)
        except:
            return False 

def get_users():
    with Database('master.db') as db:
        return db.get_users()

def get_holdings(user_name):
    with Database('master.db') as db:
        return db.get_holdings(user_name)

def holdings_volumes(user_name):
    with Database('master.db') as db:
        return db.holdings_volumes(user_name)




        












