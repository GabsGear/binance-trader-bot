import bittrex_lib as bit
import backtrader.feeds as btfeed

class OHLC(btfeef.GenericCSVData):
    params = (
        ('fromdate', datetime.datetime(2000, 1, 1)),
        ('todate', datetime.datetime(2000, 12, 31)),
        ('nullvalue', 0.0),
        ('dtformat', ('%Y-%m-%d')),
        ('tmformat', ('%H.%M.%S')),

        ('datetime', 0),
        ('time', 1),
        ('high', 2),
        ('low', 3),
        ('open', 4),
        ('close', 5),
        ('volume', 6),
        ('openinterest', -1)
    )

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



print(getCandleList('BTC-SC', 'hour')['o'])