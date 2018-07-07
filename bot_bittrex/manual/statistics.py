import talib as tb
import numpy as np

def getRSISmall(data):
	size = len(data)
	data = np.array(data, dtype=float)
	for c in data:
		c = c*100
		print(c)
	rsi = tb.RSI(data, timeperiod=14)
	print("after generate")
	print(rsi)
	return rsi[size-1]

def getRSI(data):
	size = len(data)
	data = np.array(data, dtype=float)
	print(data)
	rsi = tb.RSI(data, timeperiod=14)
	print(rsi[size-1])
	if(rsi[size-1] > 0.0):
		return rsi[size-1]
	else:
		return getRSISmall(data)

def getWMA(data):
	size = len(data['c'])
	data['c'] = data['c'][size-30:size]
	return talib.WMA(data['c'], timeperiod=30)

