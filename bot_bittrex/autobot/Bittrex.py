import Lib as _LIB
import db
import time
import datetime
import pytz
import sys
import Bot as _BOT
import User as _USER

class Bittrex():
	def __init__(self):
		self.api_1 = _LIB.Bittrex('', '', api_version='v1.1')
		self.api_2 = _LIB.Bittrex('', '', api_version='v2.0')


	def getCandles(self, pair):
		#print(self.api_2.get_candles(pair, 'hour')['result'])
		return self.api_2.get_candles(pair, 'hour')['result']

	def getCandleList(self, pair): 
		candles = None
		while(candles == None):
			print("[+] Request Schedule to Bittrex...")
			candles = self.getCandles(pair)
			time.sleep(10)
		###################
		t, o, h, c, l, v = [], [], [], [], [], []
		####################
		size = len(candles)-101
		total = 0
		for i in range(size, len(candles)-1):
			t.append(candles[i]['T'])
			o.append(candles[i]['O'])
			h.append(candles[i]['H'])
			c.append(candles[i]['C'])
			l.append(candles[i]['L'])
			v.append(candles[i]['V'])
		return t, o, h, c, l, v
		

	def getTicker(self, pair):
		return float(self.api_1.get_ticker(pair)['result']['Last'])

	def getMarketCurrency(self):
		return self.api_1.get_markets()['result']

	def checkConnApi(self):
		return self.api_2.get_balance('BTC')['success']

	def getOrder(self):
		return self.api_2.get_order(uuid)

	def getBalance(self, market):
		return self.api_2.get_balance(market)['result']['Available']

