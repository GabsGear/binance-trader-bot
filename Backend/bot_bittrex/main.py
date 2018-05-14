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
	#acc_config = db.getConfigAcc(bot_config['user_id'])
	bittrex_func.loadAPI(bot_config)
	db.setPID(bot_id)
	#bittrex = bittrex_lib.Bittrex(acc_config['bit_api_key'], acc_config['bit_api_secret'], api_version='v1.1')	
	#print bittrex.get_balances()
	while(bot_config['active'] != 2):
		routine(bot_id)

def routine(bot_id):
	t.sleep(30)
	print ("--[1]--Iniciando Rotina... \n")
	bot_config = db.getConfigBot(bot_id)
	tryBuy(bot_config) ##VERIFICANDO ESTRATEGIA DE COMPRA
	trySell(bot_config) ##VERIFICANDO ESTRATEGIA DE VENDA

def tryBuy(bot_config):
	##CARREGANDO DADOS DE DECISAO
	price_now = bittrex_func.getTicker(bot_config['currency'])
	trans = db.getOrder(bot_config['id'])
	#############
	print ("--[2]--Checkando se posso comprar... \n")
	if(orderBuyStatus(bot_config) == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return
	print ("--[4]--Checagem de compra concluida, agora posso receber sinais de compra.. \n")
	
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
	print ("--[7]--Checkando se posso vender... \n")
	if(orderSellStatus(bot_config) == 1): #VERIFICANDO PENDENCIA DE ORDENS
		return
	print ("--[9]--Checagem de venda conluida... \n")
	###################################
	#DADOS SQL PARA INSERCAO
	data = {
		'bot_id': bot_config['id'],
		'sell_value': price_now,
		'sell_uuid': '',
	}
	## STOPLOSS
	###################################
	checkSell(data, bot_config, trans, price_now)
	###################################

def checkBuy(data, bot_config, price_now):
	for i in range(0, 7): #0 a 4
		if(bot_config['strategy_buy'] == i):
			print ("--[5]--Recebendo sinais de compra.. \n")
			if(strategy.map(bot_config)[i] == 'buy'):
				print ("--[5]--Tentando comprar.. \n")
				bittrex_func.buyLimit(data, bot_config, price_now)

def checkSell(data, bot_config, trans, price_now):
	fix_profit = trans['buy_value']+(trans['buy_value']*bot_config['percentage'])
	stoploss = trans['buy_value']*(1-float(bot_config['stoploss']))
	
	print ("--[9]--Stoploss calculado ... \n")
	if(price_now <= stoploss):
		bittrex_func.sellLimit(data, bot_config, price_now, trans)
		t.sleep(1800)
		return
	print ("--[9]--Nao atingi o stop entao posso receber sinais de venda ... \n")
	##VENDENDO VIA MEDIA MOVEL ID 101 SO TEM PRA ESTRATEGIA BREAK CHANNEL
	if(bot_config['strategy_buy'] == 6 and strategy.map(bot_config)[6] == 'sell'):
		bittrex_func.sellLimit(data, bot_config, price_now, trans)
		return
	if(price_now >= fix_profit and bot_config['strategy_buy'] != 6):
		bittrex_func.sellLimit(data, bot_config, price_now, trans)
		return 


##VERIFICA SE PODE COMPRAR, 
def orderBuyStatus(bot_config):
	trans = db.getOrder(bot_config['id'])
	num_order = db.getOpenOrders(bot_config['id'])

	##ORDEM DE COMPRA JA ABERTA
	##BOT EM MODO SIMULACAO
	if(num_order > 0  and bot_config['active'] == 0):
		print ("--[3]--Temos uma ordem aberta de compra e o bot esta em simulacao... \n")
		return 1 #ORDEM JA ABERTA DE VENDA

	##BOT ATIVO
	##ORDEM DE COMPRA NUM_ORDER === SELLED = 0, entao nao tem nenhuma venda para verificar
	if(num_order > 0  and bot_config['active'] == 1): 
		print ("--[3]--Temos uma ordem aberta de compra e o bot esta ativo... \n")
		return 1

	return 0
	#########################


#VERIFICANDO SE PODE VENDER BASEADO NOS STATUS DA ORDEN DE COMPRA
def orderSellStatus(bot_config):
	trans = db.getOrder(bot_config['id'])
	num_order = db.getOpenOrders(bot_config['id'])
	if(num_order == 0 and bot_config['active'] == 0):
		print ("--[8]--Bot simulando e nao a nenhuma ordem aberta pra vender... \n")
		return 1 #NAO HA NADA PARA VENDER
	
	if(trans == False): #NAO HA ORDEM PARA VERIFICAR
		print ("--[8]--Nenhuma ordem foi aberta... \n")
		return 1
	
	if(trans['selled'] == 1 and trans != False):
		print ("--[8]--Ordem ja foi vendida.. \n")
		return 1

	return 0
	#########################



main()