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
	
	if(bot_config['active'] == 2):
		print("BOT PARADO!")
		
	while(bot_config['active'] != 2):
		t.sleep(10)
		routine(bot_id)

def routine(bot_id):
	bot_config = db.getConfigBot(bot_id)
	tryBuy(bot_config) ##VERIFICANDO ESTRATEGIA DE COMPRA
	trySell(bot_config) ##VERIFICANDO ESTRATEGIA DE VENDA

def tryBuy(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	#############
	if(orderBuyStatus(bot_config, data_decision) == 1): #VERIFICANDO PENDENCIA DE ORDENS
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
	checkBuy(data, bot_config, data_decision)
	#######################################

def trySell(bot_config):
	##CARREGANDO DADOS DE DECISAO
	data_decision = strategy.getDataDecision(bot_config)
	#############
	if(orderSellStatus(bot_config, data_decision) == 1): #VERIFICANDO PENDENCIA DE ORDENS
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
		return
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
	#print map
	return map



def checkBuy(data, bot_config, data_decision):
	for i in range(0, 5): #0 a 4
		if(bot_config['strategy_buy'] == i):
			#print "MOEDA:"+str(bot_config['currency'])+"\SINAL COMPRA:"+str(mapStrategy()[i])
			if(mapStrategy()[i] == 'buy'):
				bittrex_func.buyLimit(data, bot_config, data_decision['price_now'])

def checkSell(data, bot_config, data_decision):
	fix_profit = data_decision['trans']['buy_value']+data_decision['trans']['buy_value']*bot_config['percentage']
	if(data_decision['price_now'] >= fix_profit):
		bittrex_func.sellLimit(data, bot_config, data_decision['price_now'], data_decision['trans'])

def orderBuyStatus(bot_config, data_decision):
	#print "ordens aberta"+str(data_decision['open_orders'])
	if(data_decision['open_orders'] == 1 and bot_config['active'] == 0):
		#print str(bot_config['currency'])+"ordem de compra ja aberta"
		return 1 #ORDEM JA ABERTA DE VENDA
	#BOT ATIVO E COM UMA ORDEM DE VENDA PENDENTE
	if(data_decision['open_orders'] == 1 and bot_config['active'] == 1): ##SE BOT ATIVO, E ORDEM DE COMPRA ABERTA AINDA NAO HA VENDA PARA VERIFICAR
		return 1

	if(bot_config['active'] == 1 and data_decision['trans'] != False and data_decision['trans']['selled'] == 1):
		print str(bot_config['currency'])+" BOT ATIVO E COM NENHUMA ORDEM DE VENDA ABERTA"
		order = bittrex_func.getOrder(uuid= data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['result']
		status = bittrex_func.getOrder(uuid= data_decision['trans']['sell_uuid'], user_id= bot_config['user_id'])['success']
		print order
		if(status == False):
			print order
			print("Erro getordersell.")
		else:
			if(order['IsOpen'] == True):
				print("ORDEM DE VENDA AINDA ABERTA")
				return 1 #ORDEM JA ABERTA DE VENDA
	return 0
	#########################

def orderSellStatus(bot_config, data_decision):
	if(data_decision['open_orders'] == 0 and bot_config['active'] == 0):
		#print str(bot_config['currency'])+"nao ha nada para vender"
		return 1 #NAO HA NADA PARA VENDER
	
	if(data_decision['trans'] == False): #NAO HA ORDEM PARA VERIFICAR
		return 1

	if(bot_config['active'] == 1 and data_decision['open_orders'] == 1): ##NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
		print str(bot_config['currency'])+" BOT ATIVO E COM UMA ORDEM DE COMPRA ABERTA"
		order = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['result']
		status = bittrex_func.getOrder(data_decision['trans']['buy_uuid'], user_id= bot_config['user_id'])['success']
		if(status == False):
			print("Erro getorderbuy.")
		else:
			if(order['IsOpen'] == True):
				print("ORDEM DE COMPRA AINDA ABERTA...")
				return 1 #NAO HA NADA PARA VENDER
	return 0
	#########################




## AUXILIARES
def perc(buy, sell):
	x = sell*100/buy
	if x < 100:
		return -1*(100-x)
	if x > 100:
		return x-100
	return 0

def writeOutput(bot_id, data):
	file = open('/home/logs/'+str(bot_id)+'-output.txt', 'a+')
	file.write('['+str(time_now())+'] '+data+"\n")




main()