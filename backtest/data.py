import bittrex_lib as bit
import backtrader.feeds as btfeed
import pandas as pd
import sys
import os.path

def getCandles(market, time):
	bittrex = bit.Bittrex('', '', api_version='v2.0')
	return bittrex.get_candles(market, time)['result']


def btc_perc():
	datas = getCandleList('USDT-BTC', 'day') 
	###################
	p = []
	####################
	size = len(datas['o'])
	for i in range(820, size):
		varr = perc(datas['o'][i], datas['c'][i])
		if(varr >= 0.5):
			date = datas['t'][i].split("T")
			p.append(date[0])
	return p

def count_bars():
	datas = getCandleList('USDT-BTC', 'day') 
	###################
	P = 0
	N = 0
	P_T = 0
	N_T = 0
	####################
	size = len(datas['o'])
	for i in range(800, size):
		varr = perc(datas['o'][i], datas['c'][i])
		if(varr > 0):
			P = P + 1
			P_T = varr + P_T
		else:
			N = N + 1
			N_T = varr + N_T
	print("P:%s, N:%s"% (P, N))
	print("PT:%s, NT:%s"% (P_T, N_T))

def perc(buy, sell):
	x = sell*100/buy
	if x < 100:
		return float(-1*(100-x))*100
	if x > 100:
		return float(x-100)*100
	return float(0)*100

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


def writeOutput(msg, pair, timeframe):
	path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles'''
	x = datapath=(path+'\\'+str(pair)+"-"+str(timeframe)+".csv")
	file = open(x, 'a+')
	file.write(msg + "\n")
	file.close()

def write(msg):
	path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\outputs'''
	x = datapath=(path+"\\result.txt")
	file = open(x, 'a+')
	file.write(msg + "\n")
	file.close()

def btc_var(date):
	dates = []
	btc_data = btc_perc()
	size = len(btc_data['t'])
	for i in range(830, size):
		perc = 0
		BTC_DATE = btc_data['t'][i].split("T")
		if(BTC_DATE[0] == date):
			return btc_data['p'][i]
	return 0


def create_data(pair, timeframe):
	candles = getCandleList(pair, timeframe)

	d = {
		't': candles['t'], 
		'o': candles['o'],
		'h': candles['h'],
		'l': candles['l'],
		'c': candles['c'],
		'v': candles['v']
	}

	df = pd.DataFrame(data=d)

	for index, row in df.iterrows():
		DATE = row['t'].split("T")
		msg = "%s %s, %s, %s, %s, %s, %s"% (DATE[0], DATE[1], row['o'], row['h'], row['l'], row['c'],  row['v'])
		writeOutput(msg, pair, timeframe)

path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles'''
x = datapath=(path+'\\'+str(sys.argv[1])+"-"+str(sys.argv[2])+".csv")
if(os.path.exists(x) == False):
	create_data(sys.argv[1], sys.argv[2])
	
#create_data('BTC-STORJ', 'hour')
#btc_var('2018-06-03')
#count_bars()