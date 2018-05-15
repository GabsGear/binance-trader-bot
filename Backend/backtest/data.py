import bittrex_lib as bit
import backtrader.feeds as btfeed
import pandas as pd

def getCandles(market, time):
	bittrex = bit.Bittrex('', '', api_version='v2.0')
	return bittrex.get_candles(market, time)['result']

def getCandleList(market, time): 
	candles = getCandles(market, time)
	###################
	o, h, l, c, v, t = [], [], [], [], [], []
	####################
	try:
		for candle in candles:
			o.append(candle['O'])
			h.append(candle['H'])
			l.append(candle['L'])
			c.append(candle['C'])
			v.append(candle['BV'])
			t.append(candle['T'])
		data = {
			'o': o, 
			'h': h, 
			'l': l, 
			'c': c,
			'v': v,
			't': t, }
		return data
	except:
		print("Erro getcandlelist.")
		

candles = getCandleList('BTC-SC', 'hour')
d = {'o': candles['o'], 'c': candles['c']}
df = pd.DataFrame(data=d)
