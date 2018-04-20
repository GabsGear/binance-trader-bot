import numpy as np
import talib as tb
import bittrex_func
import db
import statistics


def getDataDecision(bot_config):
	#try:
	candles = bittrex_func.getCandleList(bot_config['currency'], bot_config['period'])
	trans = db.getBuyOrder(bot_config['id'])
	open_orders = db.getOpenOrders(bot_config['id'])
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
	low = np.array(data['l'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
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
		if (close[1] > close[0]) and (vol[1] >= vol[0]):
			flag = True

	   
		if (flag):
			return 'buy'
		
		if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.02:
			return 'sell'

	return 'none'

def pivot_up(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	##REUNINDO DADOS SOBRE O CANDIDATO A PIVO
	pivot = {
		'c': data['c'][size-2],
		'o': data['o'][size-2],
	}
	##RETIRANDO A MAXIMA DOS 20 CANDLES ATRAS DO PIVO
	max_h = max(data['h'][size-22:size-2])
	min_l = max(data['l'][size-22:size-2])
	## PERCENTUAL
	var = perc(pivot['o'], pivot['c'])
	##STATMENT PARA SE ADEQUAR AO PIVO
	pivot_up = var > 3.0 and pivot['c'] > max_h 
	pivot_do = var < -1.5 and pivot['c'] < min_l

	if(pivot_up):
		return 'buy'
		
	if(pivot_do):
		return 'sell'

	return 'none'

def perc(buy, sell):
	x = sell*100/buy
	if x < 100:
		return float(-1*(100-x))
	if x > 100:
		return float(x-100)
	return float(0)


def rsi_max(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['h'])

	tomax = data['h'][size-3:size-1]

	maxx = max(tomax)
	rsi = statistics.getRSI(data)

	if(rsi < 30.0):
		return 'buy'
		
	if(data['price_now'] >= maxx):
		return 'sell'

	return 'none'
	

def donchain_rsi(bot_config):
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
