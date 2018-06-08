import requests  
import json

def getPriceNow(coin):
    """Price now
    
    Arguments:
        coin {[string]} -- currency in binance format
    
    Returns:
        [float] -- this function returns the atual currency price
    """
    r = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=" + coin)
    r = r.content
    jsonResponse = json.loads(r.decode('utf-8'))
    print(float(jsonResponse['price']))

    return float(jsonResponse['price'])

getPriceNow('ETHBTC')