def currency_converter(amount):
    currencyn = [100,50,20,10,1,.25,.10,.05,.01]
    currencyw = ["Hundreds","Fifties","Twenties","Tens","Ones","Quarters","Dimes","Nickels","Pennies"]

    for i in range(0,9):
        if amount >= currencyn[i]:
            print(amount)
            x = str(amount//currencyn[i])
            print(currencyw[i]+" needed: "+x )
            amount = amount % currencyn[i]
            
if __name__ == "__main__":
    currency_converter(float(input("How much money are you converting? ")))

