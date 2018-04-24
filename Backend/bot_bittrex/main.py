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
	
	while(bot_config['active'] != 2):
		routine(bot_id)

def routine(bot_id):
	bot_config = db.getConfigBot(bot_id)
	tryBuy(bot_config) ##VERIFICANDO ESTRATEGIA DE COMPRA
	trySell(bot_config) ##VERIFICANDO ESTRATEGIA DE VENDA

def tryBuy(bot_config):
	##CARREGANDO DADOS DE DECISAO
	price_now = bittrex_func.getTicker(bot_config['currency'])
	trans = db.getOrder(bot_config['id'])
	#############
	if(orderBuyStatus(bot_config) == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return
	
	####################################
	#DADOS PARA INSERCAO SQL
	data = {
		'bot_id': bot_config['id'],
		'valor': price_now,
		'qnt': float(bot_config['order_value'])/float(price_now),
		'buy_uuid': '',
	}
	####################################
	checkBuy(data, bot_config, price_now)
	#######################################


def trySell(bot_config):
	##CARREGANDO DADOS DE DECISAO
	price_now = bittrex_func.getTicker(bot_config['currency'])
	trans = db.getOrder(bot_config['id'])
	#############
	if(orderSellStatus(bot_config) == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return
	
	stoploss = trans['buy_value']*(1-float(bot_config['stoploss']))
	###################################
	#DADOS SQL PARA INSERCAO
	data = {
		'bot_id': bot_config['id'],
		'sell_value': price_now,
		'sell_uuid': '',
	}
	## STOPLOSS
	if(price_now <= stoploss):
		bittrex_func.sellLimit(data, bot_config, price_now, trans)
		return
	###################################
	checkSell(data, bot_config, trans, price_now)
	###################################



def checkBuy(data, bot_config, price_now):
	for i in range(0, 5): #0 a 4
		if(bot_config['strategy_buy'] == i):
			#print "MOEDA:"+str(bot_config['currency'])+"\SINAL COMPRA:"+str(mapStrategy()[i])
			if(strategy.map(bot_config)[i] == 'buy'):
				bittrex_func.buyLimit(data, bot_config, price_now)

def checkSell(data, bot_config, trans, price_now):
	fix_profit = trans['buy_value']+(trans['buy_value']*bot_config['percentage'])
	if(price_now >= fix_profit):
		bittrex_func.sellLimit(data, bot_config, price_now, trans)


##VERIFICA SE PODE COMPRAR, 
def orderBuyStatus(bot_config):
	trans = db.getOrder(bot_config['id'])
	num_order = db.getOpenOrders(bot_config['id'])

	##ORDEM DE COMPRA JA ABERTA
	##BOT EM MODO SIMULACAO
	if(num_order > 0  and bot_config['active'] == 0):
		##print str(bot_config['currency'])+"ordem de compra ja aberta"
		return 1 #ORDEM JA ABERTA DE VENDA

	##BOT ATIVO
	##ORDEM DE COMPRA NUM_ORDER === SELLED = 0, entao nao tem nenhuma venda para verificar
	if(num_order > 0  and bot_config['active'] == 1): 
		##print "Output: Trans Selled = 0 | Bot Active = 1."
		return 1


	##BOT ATIVO = 1
	##TRANS != False - existe transacao no banco de dados
	##SELLED = 1 - a transacao ja esta com selled = 1
	##VERIFICANDO SE A ORDEM DE VENDA ESTA ABERTA AINDA NA EXCHANGE SE TIVER VAI EXCLUIR APOS 5 MIN
	if(bot_config['active'] == 1 and trans != False and trans['selled'] == 1):
		##print str(bot_config['currency'])+" BOT ATIVO E COM NENHUMA ORDEM DE VENDA ABERTA"
		order  = bittrex_func.getOrder(trans['sell_uuid'], bot_config['user_id'])['result']
		status = bittrex_func.getOrder(trans['sell_uuid'], bot_config['user_id'])['success']
		##print order
		if(order['IsOpen'] == True):
			bittrex_func.cancel_order(bot_config['id'], trans['sell_uuid'], trans['date_open'], bot_config['user_id'], 'sell')
			##print("ORDEM DE VENDA AINDA ABERTA")
			return 1 #ORDEM JA ABERTA DE VENDA
	return 0
	#########################


#VERIFICANDO SE PODE VENDER BASEADO NOS STATUS DA ORDEN DE COMPRA
def orderSellStatus(bot_config):
	trans = db.getOrder(bot_config['id'])
	num_order = db.getOpenOrders(bot_config['id'])
	if(num_order == 0 and bot_config['active'] == 0):
		#print str(bot_config['currency'])+"nao ha nada para vender"
		return 1 #NAO HA NADA PARA VENDER
	
	if(trans == False): #NAO HA ORDEM PARA VERIFICAR
		return 1


	##BOT ATIVO = 1
	##TRANS != False - existe transacao no banco de dados
	##SELLED = 0 - a transacao ja esta com selled = 1
	##VERIFICANDO SE A ORDEM DE COMPRA ESTA ABERTA AINDA NA EXCHANGE SE TIVER VAI EXCLUIR APOS 5 MIN
	if(bot_config['active'] == 1 and num_order > 0): ##NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
		print str(bot_config['currency'])+" BOT ATIVO E COM UMA ORDEM DE COMPRA ABERTA"
		order  = bittrex_func.getOrder(trans['buy_uuid'], bot_config['user_id'])['result']
		status = bittrex_func.getOrder(trans['buy_uuid'], bot_config['user_id'])['success']
		if(order['IsOpen'] == True):
			print("ORDEM DE COMPRA AINDA ABERTA...")
			bittrex_func.cancel_order(bot_config['id'], trans['buy_uuid'], trans['date_open'], bot_config['user_id'], 'buy')
			return 1 #NAO HA NADA PARA VENDER
	return 0
	#########################



main()