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
		print ("--[6]--Compra executada, via simulacao.. \n")
		db.insertBuyOrder(data)
		t.sleep(60)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True):
		acc_config = db.getConfigAcc(bot_config['user_id'])
		acc_balance = getBalance(user_id= bot_config['user_id'], bot_config= bot_config)
		##CALCULANDO QUANTIDADE BASEADO NO BALANCO DISPONIVEL DE BTC OU USDT
		amount = float(acc_balance)*float(bot_config['order_value'])/float(price_now)
		##VERIFICANDO SE A QUANTIDADE CALCULADA PARA COMPRA E MAIOR QUE A ORDEM MINIMA
		#if(check_min_order(bot_config['min_order'], amount, bot_config['currency']) == 0):
		#print ("--[6]--Ordem minima nao atingida para compra.. \n")
		#return
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
		##LANCANDO ORDEM DE COMPRA NA EXCHANGE
		order_buy = bittrex.buy_limit(market=bot_config['currency'], quantity=amount, rate=price_now)
		if(order_buy['success'] == False or order_buy == None):
			return ##QUITANDO
		#####################################
		##CARREGANDO DADOS
		UUID = order_buy['result']['uuid']
		USER_ID = bot_config['user_id']
		t.sleep(10)
		##CHECKAR SE A ORDEM FOI EXECUTADA
		order_status  = None
		while(order_status == None):
			order_status  = getOrder(uuid= UUID, user_id=  USER_ID)['result']

		if(order_status['IsOpen'] == True):
			cancel_order(uuid= UUID, user_id= USER_ID)
			return  ##QUITANDO
		
		#####################################
		##TRANSFERINDO A QUANTIDADE COMPRADA PARA O DICIONARIO DATA PARA INSERIR NO BANCO DE DADOS
		data['qnt'] = getOrder(uuid= UUID, user_id= USER_ID)['result']['Quantity']
		data['buy_uuid'] = UUID
		db.insertBuyOrder(data)
		print ("--[6]--Compra executada, modo real. \n")
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
		print ("--[11]--Venda executada, via simulacao.. \n")
		t.sleep(60)
	if(bot_config['active'] == 1 and checkConnApi(bot_config= bot_config) == True and trans['selled'] == 0):
		acc_config = db.getConfigAcc(bot_config['user_id'])
		bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
		order_sell = bittrex.sell_limit(market=bot_config['currency'], quantity=trans['quantity'], rate=price_now*1.1)
		if(order_sell['success'] == False or order_sell == None):
			return
		#####################################
		##CARREGANDO DADOS
		UUID = order_sell['result']['uuid']
		USER_ID = bot_config['user_id']
		t.sleep(10)
		##CHECKAR SE A ORDEM FOI EXECUTADA
		order_status  = None
		while(order_status == None):
			order_status  = getOrder(uuid= UUID, user_id=  USER_ID)['result']

		if(order_status['IsOpen'] == True):
			cancel_order(uuid= UUID, user_id= USER_ID)
			return  ##QUITANDO
		#####################################
		##COMITANDO A ORDEM DE VENDA NO BANCO DE DADOS
		data['sell_uuid'] = UUID
		db.commitSellOrder(data)
		print ("--[11]--Venda executada, bot ativo.. \n")
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

	
def cancel_order(uuid, user_id):
	acc_config = db.getConfigAcc(user_id)
	bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')
	order_cancel = None
	while(order_cancel == None):
		order_cancel = bittrex.cancel(uuid)