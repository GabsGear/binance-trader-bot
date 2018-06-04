import Bittrex as _BITTREX
import db
import Strategy as _STRATEGY
import Order as _ORDER
import Lib as _LIB


		
class Bot():
	def __init__(self, id = None, user_id = None, strategy = None, profit = None, pid = None, status = None, stoploss = None):
		self.id = id
		self.user_id = user_id
		self.pairs = ['BTC-ADA', 'BTC-XLM', 'BTC-TRX', 'BTC-GNT', 'BTC-WAVES', 'BTC-DGB', 'BTC-XEM', 
		'BTC-EMC2', 'BTC-STORJ', 'BTC-OMG', 'BTC-LTC', 'BTC-XEM', 'BTC-ETH', 'BTC-NEO', 'BTC-BTG', 'BTC-DASH'
		'BTC-LSK', 'BTC-NXT', 'BTC-GNT', 'BTC-POLY', 'BTC-STEEM', 'BTC-ETC', 'BTC-ZRX', 'BTC-RLC', 'BTC-CVC'
		'BTC-ZEN', 'BTC-QTUM', 'BTC-ZEN', 'BTC-BURST', 'BTC-STRAT']
		self.strategy = strategy
		self.profit = profit
		self.pid = pid
		self.status = status
		self.stoploss = stoploss
		

	def check_buy(self):
		Bittrex = _BITTREX.Bittrex(self.id)
		
		# Not free to make new buy orders exit from routine
		#if(self.free_buy() == 0):
		#return

		for pair in self.pairs:
			Strategy  = _STRATEGY.Strategy(self.id, pair)
			if(Strategy.contra_turtle() == 'buy'):
				pair = pair.split("-")
				# CHECK IF EXIST OPEN ORDER FOR PAIR:MARKET-CURRENCY
				count_order = db.getPendentOrder(self.id, pair[0], pair[1])
				if(count_order == 0):
					price_now = Bittrex.getTicker(pair[0]+'-'+pair[1])
					amount = float(1)/float(price_now)
					Order = _ORDER.Order(bot_id=self.id, market=pair[0], currency=pair[1], buy_value=price_now, sell_value=None, amount=amount, status=0)
					Order.execute_buy()
				else:
					print ("[+] OPEN ORDER FOR PAIR  %s-%s... \n" % (pair[0], pair[1]))

	def check_sell(self):
		Bittrex = _BITTREX.Bittrex(self.id)
		Orders = db.getOrders(self.id)
		for Order in Orders:
			price_now = Bittrex.getTicker(Order.market+"-"+Order.currency)
			fix_profit = Order.buy_value + (Order.buy_value * self.profit)
			stoploss = Order.buy_value * (1 - self.stoploss)
			print("[+] ORDEM:%d, MARKET:%s, CURRENCY:%s, BUY:%.8f, SELL:%.8f, STOP:%.8f"% (Order.id, Order.market, Order.currency, Order.buy_value, fix_profit, stoploss))
			if(price_now >= fix_profit):
				Order.sell_value = price_now
				Order.status = 1
				Order.execute_sell()
				print ("[+] Venda via lucro fixo ... \n")
				return

	# CHECAGEM PARA LIBERACAO DE COMPRA
	# 0: LIVRE | 1: IMPEDIDO
	def free_buy(self):
		Order = db.getOrder(self.id)
		#num_order = db.getOpenOrders(self.id)
		print("checando")
		##ORDEM DE COMPRA JA ABERTA
		##BOT EM MODO SIMULACAO
		if(Order.status == 0):
			print ("[+] Temos uma ordem aberta de compra... \n")
			return 0 #ORDEM JA ABERTA DE VENDA
		else:
			return 1

	def free_sell(self):
		trans = db.getOrder(self.id)
		num_order = db.getOpenOrders(self.id)

		if(num_order == 0 and self.status == 0):
			print ("[+] Bot simulando e nao a nenhuma ordem aberta pra vender... \n")
			return 1 #NAO HA NADA PARA VENDER
		
		if(trans == False): #NAO HA ORDEM PARA VERIFICAR
			print ("[+] Nenhuma ordem foi aberta... \n")
			return 1
		
		if(trans['selled'] == 1 and trans != False):
			print ("[+] Ordem ja foi vendida.. \n")
			return 1

		return 0
		#########################
	
	def sell_routine(self, pair):
		#############
		print ("[+] Checkando se posso vender... \n")
		
		if(self.free_sell() == 1): #VERIFICANDO PENDENCIA DE ORDENS
			return

		trans = db.getOrder(self.id)

		if(trans['pair'] == None):
			return

		price_now = bittrex_func.getTicker(trans['pair'])

		###################################
		Order = Order(bot_id=self.id, buy_value=price_now, amount=trans['amount'], pair=trans['pair'], buy_uuid=None)
		self.checkSell(Order)
		###################################