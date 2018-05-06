# coding=utf-8
import numpy as np
from binance.client import Client
import botconfig
from datetime import datetime
import numpy as np
import requests
import helpers
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
            candles = client.get_klines(
                symbol=coin, interval=Client.KLINE_INTERVAL_1DAY)
            candles = candles[len(candles)-100:len(candles)-1]
        elif(period == 'hour'):
            candles = client.get_klines(
                symbol=coin, interval=Client.KLINE_INTERVAL_1HOUR)
            candles = candles[len(candles)-100:len(candles)-1]
        elif(period == 'thirtyMin'):
            candles = client.get_klines(
                symbol=coin, interval=Client.KLINE_INTERVAL_30MINUTE)
            candles = candles[len(candles)-100:len(candles)-1]
        elif(period == 'fiveMin'):
            candles = client.get_klines(
                symbol=coin, interval=Client.KLINE_INTERVAL_5MINUTE)
            candles = candles[len(candles)-100:len(candles)-1]
        elif(period == 'oneMin'):
            candles = client.get_klines(
                symbol=coin, interval=Client.KLINE_INTERVAL_1MINUTE)
            candles = candles[len(candles)-100:len(candles)-1]
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

    def createBuyOrder(self, data, bot_config, data_decision):
        hp = helpers.Helpers()
        check = routines.Routines()
        if not (check.orderBuyStatus(bot_config, data_decision)):
            db = botconfig.Db()
            if not (bot_config['active']):
                log = ('Inserindo simulada')
                hp.writeOutput(bot_config['id'], log)
                db.insertBuyOrder(data)

    def createSellOrder(self, data, bot_config, data_decision):
        hp = helpers.Helpers()
        log = ('entrou na funcao de venda')
        hp.writeOutput(bot_config['id'], log)
        db = botconfig.Db()
        if not (bot_config['active']):
            log= ('inserindo os dados de venda no bd')
            hp.writeOutput(bot_config['id'], log)
            db.commitSellOrder(data)