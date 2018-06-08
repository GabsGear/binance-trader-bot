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
	tryBuy(bot_config) ##VERIFICANDO ESTRATEGIA DE COMPRA
	trySell(bot_config) ##VERIFICANDO ESTRATEGIA DE VENDA

def tryBuy(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	#############
	if(checkOrderStatus(bot_config, data_decision, 'buy') == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return
	
	print "passo aqui"
	####################################
	#DADOS PARA INSERCAO SQL
	data = {
		'bot_id': bot_config['id'],
		'valor': data_decision['price_now'],
		'qnt': float(bot_config['order_value'])/float(data_decision['price_now']),
		'buy_uuid': '',
	}
	####################################
	checkBuy(data, bot_config, data_decision)
	#######################################

def trySell(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	#############
	if(checkOrderStatus(bot_config, data_decision, 'sell') == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return

	stoploss = data_decision['trans']['buy_value']*(1-float(bot_config['stoploss']))
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
	checkSell(data, bot_config, data_decision)
	###################################

def mapStrategy():
	map = {
		0: strategy.contra_turtle(bot_config), #CONTRA TURTLE
		1: strategy.inside_bar(bot_config), #INSIDE BAR
		2: strategy.double_up(bot_config), #DOUBLLE UP
		3: strategy.pivot_up(bot_config), #PIVOT UP
		4: strategy.rsi_max(bot_config), #RSI RESISTANCE
	}
	print map
	return map



def checkBuy(data, bot_config, data_decision):
	for i in range(0, 4):
		if(bot_config['strategy_buy'] == i):
			print "achei minha estrategia de compra"+str(i)
			if(mapStrategy()[i] == 'buy'):
				bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

def checkSell(data, bot_config, data_decision):
	fix_profit = data_decision['trans']['buy_value']+data_decision['trans']['buy_value']*bot_config['percentage']
	for i in range(0, 4):
		if(bot_config['strategy_sell'] == i):
			print "achei minha estrategia de venda"+str(i)
			if(mapStrategy()[i] == 'sell' and bot_config['strategy_sell'] == 0):
				bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])
			if(bot_config['strategy_sell'] == 1 and data_decision['price_now'] >= fix_profit):
				bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

def checkOrderStatus(bot_config, data_decision, order_type):
	if(bot_config['active'] == 1 and data_decision['open_orders'] == 1):
		if(order_type == 'buy'):
			order = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['result']
			status = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['success']
		else:
			order = bittrex_func.getOrder(data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['result']
			status = bittrex_func.getOrder(data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['success']
		########################
		if(status == False):
			print("Erro na requisicao de ordem de"+str(order_type)+str(order))
		else:
			if(order['IsOpen'] == True):
				print("ORDEM DE"+str(order_type)+"AINDA ABERTA...")
				return 1 ## SAIR DA FUNCAO TRY
	if(data_decision['open_orders'] == 0 and order_type == 'sell'):
		return 1 ## SAIR DA FUNCAO TRY
	####################
	print "nenhuma ordem aberta so dale"
	return 0 ## FICAR NA FUNCAO TRY



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