from talib import MA_Type
import sys
import json
import io
import numpy as np
from talib.abstract import *
import talib as tb
import time as t
import datetime
import urllib2
import signal
import pytz
import strategy
import db
import bittrex_func
import bittrex_lib


def main():
	bot_id = sys.argv[1]
	global bot_config
	bot_config = db.getConfigBot(bot_id)
	print("STARTED...")

	bittrex_func.loadAPI(bot_config)
	db.setPID(bot_id)

	while(True):
		routine(bot_id)

def routine(bot_id):
	bot_config = db.getConfigBot(bot_id)
	buyOrder(bot_config) ##VERIFICANDO ESTRATEGIA DE COMPRA
	sellOrder(bot_config) ##VERIFICANDO ESTRATEGIA DE VENDA

def buyOrder(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	##DADOS PARA INSERCAO NA TABELA
	if(data_decision['open_orders'] == 1):
		return

	if(bot_config['active'] == 1 and data_decision['open_orders'] == 1):
		order = bittrex_func.getOrder(uuid= data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['result']
		status = bittrex_func.getOrder(uuid= data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['success']
		if(status == False):
			print order
			print("Erro na requisicao de ordem de venda.")
		else:
			if(order['IsOpen'] == True):
				print("ORDEM DE VENDA AINDA ABERTA")
				return

	####################################
	#DADOS PARA INSERCAO SQL
	data = {
		'bot_id': bot_config['id'],
		'valor': data_decision['price_now'],
		'qnt': float(bot_config['order_value'])/float(data_decision['price_now']),
		'buy_uuid': '',
	}
	####################################
	if(bot_config['strategy_buy'] == 0 and strategy.contra_turtle(bot_config) == 'buy'):
		bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

	if(bot_config['strategy_buy'] == 1 and strategy.inside_bar(bot_config) == 'buy'):
		bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

	if(bot_config['strategy_buy'] == 2 and strategy.double_up(bot_config) == 'buy'):
		bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

	if(bot_config['strategy_buy'] == 3 and strategy.pivot_up(bot_config) == 'buy'):
		bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

	if(bot_config['strategy_buy'] == 4 and strategy.rsi_max(bot_config) == 'buy'):
		bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

	#######################################

def sellOrder(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	#################################################
	##VERIFICANDO SE EXISTE ORDEM ABERTA
	if(data_decision['open_orders'] == 0):
		return

	if(bot_config['active'] == 1 and data_decision['open_orders'] == 1): ##NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
		order = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['result']
		status = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['success']
		if(status == False):
			print("Erro na requisicao de ordem de compra.")
		else:
			if(order['IsOpen'] == True):
				print("ORDEM DE COMPRA AINDA ABERTA...")
				return

	stoploss = data_decision['trans']['buy_value']*(1-float(bot_config['stoploss']))
	fix_profit = data_decision['trans']['buy_value']+data_decision['trans']['buy_value']*bot_config['percentage']
	###################################
	#DADOS SQL PARA INSERCAO
	data = {
		'bot_id': bot_config['id'],
		'sell_value': data_decision['price_now'],
		'sell_uuid': '',
	}
	## STOPLOSS
	if(data_decision['price_now'] <= stoploss):
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])
	###################################

	##SELECIONANDO E VERIFICANDO ESTRATEGIA
	if(bot_config['strategy_sell'] == 0 and bot_config['strategy_buy'] == 0 and strategy.contra_turtle(bot_config) == 'sell'): ## VENDA VIA CONTRA TT
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

	if(bot_config['strategy_sell'] == 0 and bot_config['strategy_buy'] == 1 and strategy.inside_bar(bot_config) == 'sell'): ## VENDA VIA INSIDE BAR
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

	if(bot_config['strategy_sell'] == 0 and bot_config['strategy_buy'] == 2 and strategy.double_up(bot_config) == 'sell'): ## VENDA VIA DOUBLE UP
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

	if(bot_config['strategy_sell'] == 0 and bot_config['strategy_buy'] == 3 and strategy.pivot_up(bot_config) == 'sell'): ## VENDA VIA DOUBLE UP
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])
	
	if(bot_config['strategy_sell'] == 0 and bot_config['strategy_buy'] == 4 and strategy.rsi_max(bot_config) == 'sell'): ## VENDA VIA DOUBLE UP
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

	if(bot_config['strategy_sell'] == 1 and data_decision['price_now'] >= fix_profit): ## VENDA VIA PRECO FIXO
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])


def perc(buy, sell):
	x = sell*100/buy
	if x < 100:
		return -1*(100-x)
	if x > 100:
		return x-100
	return 0


## AUXILIARES

def writeOutput(bot_id, data):
	file = open('/home/logs/'+str(bot_id)+'-output.txt', 'a+')
	file.write('['+str(time_now())+'] '+data+"\n")




main()