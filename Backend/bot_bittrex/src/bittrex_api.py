import bittrex
import db

def loadAPI(bot_config):
	global bittrex
	global bittrex_v1
	acc_config = db.getConfigAcc(bot_config['user_id'])
	if(bot_config['active'] == 1):
		bittrex = bittrex.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v2.0')
		bittrex_v1 = bittrex.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v1.1')
	else:
		bittrex = bittrex.Bittrex('', '', api_version='v2.0')
		bittrex_v1 = bittrex.Bittrex('', '', api_version='v1.1')

def getCandles(market, time):
	return bittrex.get_candles(market, time)['result']

def getCandleList(market, time): 
	candles = getCandles(market, time)
	###################
	o, h, l, c, v, t = [], [], [], [], [], []
	####################
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

def getTicker(market):
	data =  bittrex_v1.get_ticker(market)['result']
	return data

def getMarketCurrency():
	return bittrex_v1.get_markets()['result']

def checkConnApi():
	result = bittrex.get_balance('apiC')['success']
	if(result == False):
		print("Falha na conexao...")
		return 
	return result

##MARKET API
def getOrderHistory(market):
	return bittrex.get_order_history(market)

def getOrder(uuid):
	return bittrex.get_order(uuid)

def getBalance():
	return bittrex.get_balance('apiC')

def buyLimit(market, quantity, rate):
	return bittrex_v1.buy_limit(market, quantity, rate)

def sellLimit(market, quantity, rate):
	return bittrex_v1.sell_limit(market, quantity, rate)