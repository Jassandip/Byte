#!/usr/bin/env python3

import os

def start_up_menu():
    return(input('[s]ign up or [l]ogg in?\n'))

def sign_up_menu():
    return input('User name: '),input('Passowrd: ')

def logg_in_menu():
    return input('User name: '),input('Passowrd: ')

def transaction_menu(balance,ticker_symbol,price):
    print("Your current balance is {}.\nThe price to purchase {} is ${}.".format(
        balance,ticker_symbol,price))
    return input('How many do you want to purchase? ')


def lookup_menu():
    return input('Company name: ')


def quote_menu():
    return input('Ticker Symbol: ')


def header():
    #os.system('clear')
    print('\n* Terminal Trader *\n')
    os.system('cowsay -s "Welcome to Terminal Trader -$(whoami)"')


def main_menu():
    header()
    print('[b] Buy\n[s] Sell\n[l] Look-up\n[q] Quote\n[e] Exit\n[v] View\n')
    return input('What do you want to do? ')


def sell_menu():
    return input('How many do you want to sell?: ')

def show_balance(balance):
    print("\nYour curent balance is: ${}\nYour current holdings are:\n".format(balance))

def leader_board():
    print('The leaders board is:\n')