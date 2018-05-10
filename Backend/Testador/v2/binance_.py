# coding=utf-8
# pylint: disable=W0612
import numpy as np
from binance.client import Client
import botconfig
from datetime import datetime
import numpy as np
import requests
import sys
import json
import routines
import time


class ApiData:
    def checkLogin(self, idt, key):
        client = Client(idt, key)
        status = client.get_system_status()
        if (status['msg'] == 'normal'):
            print("Iniciando\n")
        else:
            sys.exit(0)


login = ApiData()
client = Client("", "")
login.checkLogin("", "")


class Binance_opr(ApiData):
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
                coin, Client.KLINE_INTERVAL_1DAY, "16 Jul, 2017", "5 May, 2018")
        elif(period == 'hour'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_1HOUR, "25 Jul, 2017", "5 May, 2018")
        elif(period == 'thirtyMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_30MINUTE, "19 Nov, 2017", "5 May, 2018")
        elif(period == 'fiveMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_5MINUTE, "19 Nov, 2017", "5 May, 2018")
        elif(period == 'oneMin'):
            candles = client.get_historical_klines(
                coin, Client.KLINE_INTERVAL_1MINUTE, "19 Nov, 2018", "1 Mai                                                                                                                                                              , 2018")
        # map
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

    def getBTCCandles(self, period):
        return self.getCandles('BTCUSDT', period)
    
    def getMean(self, coin, bot_config):
        lclose = self.getCandles(coin, bot_config['period'])
        lclose = np.array(lclose).astype(np.float)
        lclose = lclose[len(lclose)-30:len(lclose)]
        return lclose.mean()

    def createBuyOrder(self, data, bot_config, data_decision, price_now):
        check = routines.Routines()
        wallet = bot_config['wallet']
        wallet = float(wallet)*(1 - bot_config['order_value'])
        data['wallet'] = wallet
        data['buy_wallet'] = data['wallet']
        print(data['wallet'])
        if not (check.orderBuyStatus(bot_config, data_decision)):
            db = botconfig.Db()
            if not (bot_config['active']):
                db.insertBuyOrder(data, bot_config['id'])

    def createSellOrder(self, data, bot_config, data_decision, price_now, pos):
        db = botconfig.Db()
        open_order, trans = db.getBuyOrders(bot_config['id'])
        wallet = trans['buy_wallet']
        wallet = float(wallet) + trans['quantity'] * price_now
        data['wallet'] = wallet
        data['sell_wallet'] = data['wallet']
        data['data'] = data_decision['t'][pos+1]
        print(data['wallet'])
        if not (bot_config['active']):
            db.commitSellOrder(data, bot_config['id'])

