import talib as tb
import numpy as np

def getRSISmall(data):
	size = len(data['c'])
	data['c']= np.array(data['c'], dtype=float)
	for c in data['c']:
		c = c*100
	rsi = tb.RSI(data['c'], timeperiod=20)
	return rsi[size-1]

def getRSI(data):
	size = len(data['c'])
	data['c'] = np.array(data['c'], dtype=float)
	rsi = tb.RSI(data['c'], timeperiod=20)
	#print rsi[size-1]
	if(rsi[size-1] > 0.0):
		return rsi[size-1]
	else:
		return getRSISmall(data)

def getWMA(data):
	size = len(data['c'])
	data['c'] = data['c'][size-30:size]
	return talib.WMA(data['c'], timeperiod=30)

