
import sys
import pprint

def readcurrency():
    with open('currency.txt', 'r') as f:
        c = {}
        y = []
        x = f.readlines()
        for i in x:
            i = i.split()
            c["symbol: " +i[0]]= "rate: "+i[1]
            
            y.append(c)
            c = {}
            
        pprint.pprint(y)


        
        

readcurrency()