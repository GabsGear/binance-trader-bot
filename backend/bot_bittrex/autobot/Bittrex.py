import Lib as _LIB
import db
import time
import datetime
import pytz
import sys
import Bot as _BOT
import User as _USER

class Bittrex():
	def __init__(self, bot_id):
		self.bot   = db.getInstanceBot(bot_id)
		self.user  = _USER.User(self.bot.user_id)
		self.api_1 = _LIB.Bittrex('', '', api_version='v1.1')
		self.api_2 = _LIB.Bittrex('', '', api_version='v2.0')
		self.auth  = _LIB.Bittrex(self.user.key, self.user.secret, api_version='v1.1')


	def getCandles(self, pair):
		return self.api_2.get_candles(pair, self.bot.timeframe)['result']

	def getCandleList(self, pair): 
		candles = None
		while(candles == None):
			candles = self.getCandles(pair)
			time.sleep(10)
		###################
		o, h, c, l = [], [], [], []
		####################
		size = len(candles)-101
		total = 0
		for i in range(size, len(candles)-1):
			o.append(candles[i]['O'])
			h.append(candles[i]['H'])
			c.append(candles[i]['C'])
			l.append(candles[i]['L'])
		return o, h, c, l
		

	def getTicker(self, pair):
		return float(self.api_1.get_ticker(pair)['result']['Last'])

	def getMarketCurrency(self):
		return self.api_1.get_markets()['result']

	def checkConnApi(self):
		return self.api_2.get_balance('BTC')['success']

	def getOrder(self):
		return self.api_2.get_order(uuid)

	def getBalance(self):
		if(self.bot.market == 'USDT'):
			return self.api_2.get_balance('USDT')['result']['Available']
		else:
			return self.api_2.get_balance('BTC')['result']['Available']

