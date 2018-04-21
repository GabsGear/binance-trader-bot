import numpy as np
import talib as tb
import bittrex_func
import db


def contra_turtle(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])

	tomin = data['l'][size-21:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
	tomax = data['h'][size-3:size-1]  ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 2

	if(len(tomin) > 0):
		#print "maior que 0"
		minn = min(tomin) ## CALCULO O MINIMO DESSES 20 CANDLES
		maxx = max(tomax) ## CALCULO O MAXIMO DESSES 2 CANDLES
		if(data['price_now'] <= minn):
			#print "LANCEI COMPRA"
			return 'buy'
		if(data['price_now'] >= maxx):
			#print "LANCEI VENDA"
			return 'sell'
	return 'none'


def inside_bar(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	flag = False

	high = np.array(data['h'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
	close = np.array(data['c'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

	if(len(high) > 0):
		if (high[1] < high[0]) and (close[1] >= close[0]):
			if data['price_now'] > high[0]:
				flag = True
	   
		if (flag):
			return 'buy'
		
		if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.05:
			return 'sell'

	return 'none'

def double_up(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	flag = False

	vol   = np.array(data['v'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
	close = np.array(data['c'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

	if(len(close) > 0):
		if (close[len(close) - 1 ] > close[len(close)]) and (vol[len(vol) - 1] >= vol[len(vol)]):
			flag = True
	   
		if (flag):
			return 'buy'
		
		if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.02:
			return 'sell'

	return 'none'

def pivot_up(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	flag = False

	close = data['c'][size-20:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
	pivot = {
		
	}

	if(len(close) > 0):
		if (data['price_now'] > pivot):
			flag = True

		if (flag):
			return 'buy'
		
		if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.03:
			return 'sell'

	return 'none'

def getDataDecision(bot_config):
	#try:
	candles = bittrex_func.getCandleList(bot_config['currency'], bot_config['period'])
	open_orders, trans = db.getBuyOrders(bot_config['id'])
	price_now = bittrex_func.getTicker(bot_config['currency'])['Last']
	data = {
	'price_now': price_now,
	'open_orders': open_orders,
	'trans': trans,
	'o': candles['o'], 
	'h': candles['h'], 
	'l': candles['l'], 
	'c': candles['c'],
	'v': candles['v'],
	't': candles['t'], }
	return data
	#except:
	#print("ERRO: getDataDecision.")




