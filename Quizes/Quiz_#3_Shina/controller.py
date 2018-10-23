import json
import requests
from model import Wrapper as rp
import view 


call = rp()
view.ask()
symbol = input()
view.show()
print(call.quote(symbol))


