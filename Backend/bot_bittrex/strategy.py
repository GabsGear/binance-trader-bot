import numpy as np
import talib as tb
import bittrex_func
import db
import statistics


def getDataDecision(bot_config):
	#try:
	candles = bittrex_func.getCandleList(bot_config['currency'], bot_config['period'])
	price_now = bittrex_func.getTicker(bot_config['currency'])
	data = {
	'price_now': price_now,
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
	last_l = data['l'][size-2:size-1]

	tomin = data['l'][size-21:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20

	if(len(tomin) > 0):
		if(last_l[0] <= min(tomin)):
			return 'buy'


	return 'none'

def break_channel(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	tomin = data['l'][size-21:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
	tomax = data['h'][size-3:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
	last_l = data['l'][size-2:size-1]
	last_h = data['h'][size-2:size-1]

	if(len(tomin) > 0):
		#print "maior que 0"
		minn = min(tomin) ## CALCULO O MINIMO DESSES 20 CANDLES
		maxx = max(tomax) ## CALCULO O MINIMO DESSES 20 CANDLES
		print("--RESISTENCIA:"+str(maxx)+"|HIGH:"+str(last_h))
		print("--SUPORTE:"+str(minn)+"|LOW:"+str(last_l))
		if(last_l[0] <= minn):
			return 'buy'

		if(last_h[0] >= maxx):
			return 'sell'

	return 'none'


def inside_bar(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	flag = False

	high = np.array(data['h'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
	low = np.array(data['l'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

	if(len(high) > 0):
		if (high[1] < high[0]) and (low[1] >= low[0] and data['price_now'] > high[0]):
			return 'buy'

	return 'none'


def double_up(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	flag = False

	vol   = np.array(data['v'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
	close = np.array(data['c'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

	if(len(close) > 0):
		if (close[1] > close[0]) and (vol[1] >= vol[0]):
			return 'buy'

	return 'none'


##ESTRATeGIA PIVO DE ALTA
##VALOR NO BANCO: 2
def pivot_up(bot_config):
	data = getDataDecision(bot_config)
	size = len(data['c'])
	##REUNINDO DADOS SOBRE O CANDIDATO A PIVO
	if(size > 0):
		pivot = {
			'c': data['c'][size-2],
			'o': data['o'][size-2],
		}
		## PERCENTUAL
		var = perc(pivot['o'], pivot['c'])
		##STATMENT PARA SE ADEQUAR AO PIVO
		if(var > 2.0):
			return 'buy'

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
	rsi = statistics.getRSI(data)
	
	if(bot_config['period'] == 'day'):
		if(rsi < 30.0):
			return 'buy'
	if(bot_config['period'] == 'hour'):
		if(rsi < 30.0):
			return 'buy'	
	if(bot_config['period'] == 'thirtyMin'):
		if(rsi < 30.0):
			return 'buy'	
	return 'none'
	

def map(bot_config):
	map = {
		0: contra_turtle(bot_config), #CONTRA TURTLE
		1: inside_bar(bot_config), #INSIDE BAR
		2: double_up(bot_config), #DOUBLLE UP
		#3:pivot_up(bot_config), #PIVOT UP
		4: rsi_max(bot_config), #RSI RESISTANCE
		6: break_channel(bot_config), #BREAK CHANNEL
	}
	#print map
	return map



def writeOutput(bot_id, data):
	file = open('/home/bittrex/logs/'+str(bot_id)+'.txt', 'a+')
	file.write(data + "\n")