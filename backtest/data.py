import bittrex_lib as bit
import backtrader.feeds as btfeed
import pandas as pd
import sys
import os.path
import datetime
import ccxt
import time
from dateutil import tz



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



def writeOutput(msg, market, currency, timeframe):
	path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles'''
	x = (path+'\\'+str(market)+"-"+str(currency)+"-"+str(timeframe)+".csv")
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

def get_date(date):
	utc = tz.tzutc()
	date = datetime.datetime.fromtimestamp(
			int(date)/1000.0
		).strftime('%Y-%m-%d %H:%M:%S')
	date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
	date = date.replace(tzinfo=utc)
	return date.strftime("%Y-%m-%d %H:%M:%S")

def create_data(market, currency, timeframe):
	_BINANCE = ccxt.binance()
	_CANDLES = []
	_UTC = tz.tzutc()
	_MINUTE = 60 * 1000
	###########
	from_timestamp = _BINANCE.parse8601('2018-02-01 00:00:00')
	#########

	while(from_timestamp < _BINANCE.milliseconds()):
		print(_BINANCE.milliseconds(), 'Fetching candles starting from', _BINANCE.iso8601(from_timestamp))
		ohlcvs = _BINANCE.fetch_ohlcv(currency+"/"+market, timeframe, from_timestamp)
		print(_BINANCE.milliseconds(), 'Fetched', len(ohlcvs), 'candles')
		first = ohlcvs[0][0]
		last = ohlcvs[-1][0]
		print('First candle epoch', first, _BINANCE.iso8601(first))
		print('Last candle epoch', last, _BINANCE.iso8601(last))
		from_timestamp += len(ohlcvs) * _MINUTE * 30
		_CANDLES += ohlcvs

	for CANDLE in _CANDLES:
		msg = "%s, %s, %s, %s, %s, %s"% (get_date(CANDLE[0]), CANDLE[1], CANDLE[2], CANDLE[3], CANDLE[4],  CANDLE[5])
		#writeOutput(msg, market, currency, timeframe)

path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles'''
path = (path+'\\'+str(sys.argv[1])+"-"+str(sys.argv[2])+"-"+str(sys.argv[3])+".csv")
#if(os.path.exists(path) == False):
#create_data(sys.argv[1], sys.argv[2], sys.argv[3])

