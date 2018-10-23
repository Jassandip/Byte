#import sys
import pprint

def readcurrency():
    with open('currency.txt', 'r') as f:
        c = {}
        y = []
        x = f.readlines()
        for i in x:
            i = i.split()
            c["symbol: " +i[0]]= "rate: "+i[1]
            c["symbol"] = i[0]
            c["rate"] = i[1]
            """
            This is the syntax to create a new dictionary-
            the previous statement was a list made up of two strings separated by a ':', 
            instead of two separate entries for "symbol" and "rate"
            """
            c = {"symbol":i[0], "rate":float(i[1])}

            y.append(c)

        pprint.pprint(y)        

readcurrency()