import bittrex_lib
import db

def loadAPI(bot_config):
	global bittrex
	global bittrex_v1
	acc_config = db.getConfigAcc(bot_config['user_id'])
	if(bot_config['active'] == 1):
		bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v2.0')
		bittrex_v1 = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v1.1')
	else:
		bittrex = bittrex_lib.Bittrex('', '', api_version='v2.0')
		bittrex_v1 = bittrex_lib.Bittrex('', '', api_version='v1.1')

def getCandles(market, time):
	bittrex = bittrex_lib.Bittrex('', '', api_version='v2.0')
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

def checkConnApi(bot_config):
	acc_config = db.getConfigAcc(bot_config['user_id'])
	bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v2.0')
	result = bittrex.get_balance('BTC')['success']
	if(result == False):
		print("Falha na conexao...")
		return 
	return result

##MARKET API
def getOrderHistory(market):
	return bittrex.get_order_history(market)

def getOrder(uuid, user_id):
	acc_config = db.getConfigAcc(user_id)
	bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v2.0')
	return bittrex.get_order(uuid)

def getBalance(user_id, bot_config):
	acc_config = db.getConfigAcc(user_id)
	bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v2.0')
	v = bot_config['currency'].split('-')
	if(v[0] == 'USDT'):
		return bittrex.get_balance('USDT')['result']['Available']
	return bittrex.get_balance('BTC')['result']['Available']

def buyLimit(data, bot_config, price_now):
	#print data
	if(bot_config['active'] == 0):
		db.insertBuyOrder(data)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True):
		print "tentei compra"
		acc_config = db.getConfigAcc(bot_config['user_id'])
		acc_balance = getBalance(user_id= bot_config['user_id'], bot_config= bot_config)
		ammount = float(acc_balance)*float(bot_config['order_value'])/float(price_now)
		bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v1.1')
		orderBuy = bittrex.buy_limit(market=bot_config['currency'], quantity=ammount, rate=0.00000040)
		print orderBuy
		if(orderBuy == None):
			print "sou novo"
		if(orderBuy['success'] == False):
			print orderBuy
			return
		##print getOrder(uuid= orderBuy['result']['uuid'], user_id= bot_config['user_id'])
		data['qnt'] = getOrder(uuid= orderBuy['result']['uuid'], user_id= bot_config['user_id'])['result']['Quantity']
		data['buy_uuid'] = orderBuy['result']['uuid']
		db.insertBuyOrder(data)

def sellLimit(data, bot_config, price_now, trans):
	#print data
	if(bot_config['active'] == 0):
		db.commitSellOrder(data)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True and trans['selled'] == 0):
		print("to tentando vender")
		acc_config = db.getConfigAcc(bot_config['user_id'])
		bittrex = bittrex_lib.Bittrex(acc_config['api_key'], acc_config['api_secret'], api_version='v1.1')
		orderSell = bittrex.sell_limit(market=bot_config['currency'], quantity=trans['quantity'], rate=price_now)
		print orderSell
		if(orderSell == None):
			print "sou novo"
		if(orderSell['success'] == False):
			print orderSell
			return
		data['sell_uuid'] = orderSell['result']['uuid']
		db.commitSellOrder(data)