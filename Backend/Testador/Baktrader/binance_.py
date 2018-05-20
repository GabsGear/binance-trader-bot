# coding=utf-8
# pylint: disable=W0612

from datetime import datetime
from binance.client import Client
client = Client("", "")

import numpy as np
import time
import helpers 
import sys

hp = helpers.Helpers() 

class Binance_opr():
    def getCandles(self, coin, period):
        """This function returns a candlestick list in a especific time interval

        Arguments:
            coin {[string]} -- Coin in binance format
            period {[interval]} -- Candlestic interval

        Returns:
            [list] -- CandleList
        """
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
        if(period == 'Day'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_1DAY, "19 Jul, 2017", "18 May, 2018")
        elif(period == 'hour'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_1HOUR, "19 Jul, 2017", "18 May, 2018")
        elif(period == 'thirtyMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_30MINUTE, "19 Nov, 2017", "18 May, 2018")
        elif(period == 'fiveMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_5MINUTE, "19 Nov, 2017", "18 May, 2018")
        elif(period == 'oneMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_1MINUTE, "19 Nov, 2018", "18 Mai, 2018")
        # map
        opentime=[]
        lopen=[]
        lhigh=[]
        llow=[]
        lclose=[]
        lvol=[]
        closetime=[]

        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])

            candle[6] = hp.tstampToData(candle[6])
            closetime.append(candle[6])
            
        lopen=np.array(lopen).astype(np.float)
        lhigh=np.array(lhigh).astype(np.float)
        llow=np.array(llow).astype(np.float)
        lclose=np.array(lclose).astype(np.float)
        lvol=np.array(lvol).astype(np.float)
        return lopen, lhigh, llow, lclose, lvol, closetime

    def getDatabase(self, coin, period): 
        start  = 'Jul, 2017' 
        end = 'May, 2018'
        lopen, lhigh, llow, lclose, lvol, closetime = self.getCandles(coin, period)
        hp.saveDatabase(lopen, lhigh, llow, lclose, lvol, closetime,  coin, period, start, end)

    def getCoins(self):
        products = client.get_products()
        coins = []
        for x in range (0, len(products['data'])):
            coin = products['data'][x]['symbol']
            if (coin[len(coin) - 3: len(coin)] == 'BTC'):
                coins.append(str(products['data'][x]['symbol']))
        return coins

    def getAllDatabases(self):
        coins = self.getCoins()
        periods = ['Day', 'hour', 'thirtyMin']
        start  = 'Jul, 2017' 
        end = 'May, 2018'

        for coin in coins:
            print(coin)
            for period in periods:
                lopen, lhigh, llow, lclose, lvol, closetime = self.getCandles(coin, period)
                hp.saveDatabase(lopen, lhigh, llow, lclose, lvol, closetime, coin, period, start, end)

    