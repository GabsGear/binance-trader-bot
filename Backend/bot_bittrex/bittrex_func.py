import bittrex_lib
import db
import time as t
import datetime
import pytz


def loadAPI(bot_config):
	global bittrex
	global bittrex_v1
	acc_config = db.getConfigAcc(bot_config['user_id'])
	if(bot_config['active'] == 1):
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v2.0')
		bittrex_v1 = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
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
	price_now =  float(bittrex_v1.get_ticker(market)['result']['Ask'])
	if(price_now < 0.00001000):
		price_now =  float(bittrex_v1.get_ticker(market)['result']['Last'])
	return price_now

def getMarketCurrency():
	return bittrex_v1.get_markets()['result']

def checkConnApi(bot_config):
	acc_config = db.getConfigAcc(bot_config['user_id'])
	bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v2.0')
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
	bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v2.0')
	return bittrex.get_order(uuid)

def getBalance(user_id, bot_config):
	acc_config = db.getConfigAcc(user_id)
	bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v2.0')
	v = bot_config['currency'].split('-')
	if(v[0] == 'USDT'):
		return bittrex.get_balance('USDT')['result']['Available']
	return bittrex.get_balance('BTC')['result']['Available']

def buyLimit(data, bot_config, price_now):
	if(bot_config['active'] == 0):
		db.insertBuyOrder(data)
		t.sleep(60)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True):
		acc_config = db.getConfigAcc(bot_config['user_id'])
		acc_balance = getBalance(user_id= bot_config['user_id'], bot_config= bot_config)
		##CALCULANDO QUANTIDADE BASEADO NO BALANCO DISPONIVEL DE BTC OU USDT
		amount = float(acc_balance)*float(bot_config['order_value'])/float(price_now)
		##VERIFICANDO SE A QUANTIDADE CALCULADA PARA COMPRA E MAIOR QUE A ORDEM MINIMA
		if(check_min_order(bot_config['min_order'], amount, bot_config['currency']) == 0):
			return
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
		##LANCANDO ORDEM DE COMPRA NA EXCHANGE
		orderBuy = bittrex.buy_limit(market=bot_config['currency'], quantity=amount, rate=price_now)
		if(orderBuy['success'] == False or orderBuy == None):
			return
		##TRANSFERINDO A QUANTIDADE COMPRADA PARA O DICIONARIO DATA PARA INSERIR NO BANCO DE DADOS
		data['qnt'] = getOrder(uuid= orderBuy['result']['uuid'], user_id= bot_config['user_id'])['result']['Quantity']
		data['buy_uuid'] = orderBuy['result']['uuid']
		db.insertBuyOrder(data)
		t.sleep(60)

def get_market(currency):
	markets = currency.split('-')
	if(markets[0] == 'USDT'):
		return 'USDT'
	return 'BTC'

def check_min_order(min_order, amount, currency):
	if(get_market(currency) == 'USDT'):
			total_brl = amount*3.3
			if(min_order < total_brl):
				return 0 ## 0 : NAO PASSOU NA VERIFICACAO MINIMA
			else:
				return 1 ## 1 :  PASSOU NA VERIFICACAO MINIMA
	if(get_market(currency) == 'BTC'):
			total_brl = amount*9000*3.3
			if(min_order < total_brl):
				return 0 ## 0 : NAO PASSOU NA VERIFICACAO MINIMA
			else:
				return 1 ## 1 :  PASSOU NA VERIFICACAO MINIMA

def sellLimit(data, bot_config, price_now, trans):
	#print data
	if(bot_config['active'] == 0):
		db.commitSellOrder(data)
		t.sleep(60)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True and trans['selled'] == 0):
		print("to tentando vender")
		acc_config = db.getConfigAcc(bot_config['user_id'])
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
		orderSell = bittrex.sell_limit(market=bot_config['currency'], quantity=trans['quantity'], rate=price_now*1.1)
		print orderSell
		if(orderSell['success'] == False or orderSell == None):
			print orderSell
			return
		data['sell_uuid'] = orderSell['result']['uuid']
		db.commitSellOrder(data)
		t.sleep(60)


def check_delta_time(trans_time):
	brasil = pytz.timezone('America/Sao_Paulo')
	time_now = datetime.datetime.now(tz=brasil).strftime('%Y-%m-%d %H:%M:%S')
	time = datetime.datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")
	delta = str(time-trans_time)
	date = delta.split(":")
	hour = int(date[0])
	minute = int(date[1])
	if(hour > 0 or minute > 1):
		return 1
	return 0

	
def cancel_order(bot_id, uuid, date, user_id, order_type):
	time = check_delta_time(date) ##SE 0 NAO FAZ NADA / SE 1 EXCLUI
	print("verificando tempo de cancelamento...")
	if(time == 1):
		acc_config = db.getConfigAcc(user_id)
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
		bittrex.cancel(uuid)
		order = db.getOrder(bot_id)
		if(order_type == 'buy'):
			db.delete_trans(order['id'])
			print("cancelei a ordem de COMPRA e deletei do banco de dados.")
		else:
			db.update_trans(order['id'])
			print("cancelei a ordem de VENDA e atualizei a transacao.")