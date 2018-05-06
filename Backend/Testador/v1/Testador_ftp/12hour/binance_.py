import numpy as np
from binance.client import Client 
from datetime import datetime
import numpy as np
import requests
import helpers
import sys

class ApiData:

    __key = ""
    __secret = ""

    def __init__(self):
        self.__key = ('q4r6zw4CXMGynsdQhRgzcs1PuOBfT1uCCwBG2op0fue7Qr33XvH23Cn0W5SMgWGU') #mykey
        self.__secret = ('8PVopsBzr0piU66t3dEiPoxTuZUfVCemWdkjI5zN9OhEZcyPxgeO4UaAD1jM0zG0') #mysecret
    
    def getKey(self):
        return self.__key

    def getSecret(self):
        return self.__secret

    def checkLogin(self):
        client = Client(self.__key , self.__secret)
        status = client.get_system_status()
        if (status['msg'] == 'normal'):
            print ("Market UP, Successful login")
            print (client.get_server_time())
        else:
            sys.exit(0)


login = ApiData()
client = Client(login.getKey(), login.getSecret())
login.checkLogin()


class Binance_opr:
    def getSymbolList(self):
        symbols = []
        client.get_exchange_info()["symbols"][100]["symbol"]
        for x in range (0, 100):
            symbols.append(client.get_exchange_info()["symbols"][x]["symbol"])         
        symbols = symbols[0:100]
        return symbols

    def getCandles(self, coin):
        candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_12HOUR)
        candles = candles[len(candles)-501:len(candles)-1]

        '''
            API TURNS MODEL
            1499040000000,      // Open time
            "0.01634790",       // Open
            "0.80000000",       // High
            "0.01575800",       // Low
            "0.01577100",       // Close
            "148976.11427815",  // Volume
            1499644799999,      // Close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "17928899.62484339" // Ignore
        '''
        #map
        opentime = []
        lopen = []
        lhigh = []
        llow = []
        lclose = []
        lvol = []
        closetime = []


        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])
        
        lopen = np.array(lclose).astype(np.float)
        lhigh = np.array(lhigh).astype(np.float)
        llow = np.array(llow).astype(np.float)
        lclose = np.array(lclose).astype(np.float)
        lvol = np.array(lvol).astype(np.float)
        return lopen, lhigh, llow, lclose, lvol, closetime      


    def getStoricalCandles(self, coin, day):
        #klines = client.get_historical_klines(coin, client.KLINE_INTERVAL_30MINUTE, str(day) +" Jan, 2018")
        klines = client.get_historical_klines(coin, Client.KLINE_INTERVAL_12HOUR, "1 Jan, 2017", "1 Mar, 2018")
        #klines = klines[len(klines)-1001:len(klines)-1]

        opentime = []
        lopen = []
        lhigh = []
        llow = []
        lclose = []
        lvol = []
        closetime = []


        for candle in klines:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])
        
        lopen = np.array(lclose).astype(np.float)
        lhigh = np.array(lhigh).astype(np.float)
        llow = np.array(llow).astype(np.float)
        lclose = np.array(lclose).astype(np.float)
        lvol = np.array(lvol).astype(np.float)
        
        return lopen, lhigh, llow, lclose, lvol, closetime        

    def getMean(self, coin):
        lclose = self.getCandles(coin)
       	lclose = np.array(lclose).astype(np.float)
        lclose = lclose[len(lclose)-30:len(lclose)]
        return lclose.mean()
    
    def getPriceNow(self, coin):
        r = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=" + coin)
        r = r.content
        r = r[len(r) - 12: len(r)-2]
        return float(r)


