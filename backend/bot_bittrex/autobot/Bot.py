import Bittrex as _BITTREX
import db
import Strategy as _STRATEGY
import Order as _ORDER


		
class Bot():
	def __init__(self, bot_id=None, user_id=None, exchange=None, strategy=None, profit=None, pid=None, status=None, timeframe=None, stoploss=None):
		self.id = bot_id
		self.user_id = user_id
		self.exchange = exchange
		self.pairs = ['BTC-ADA', 'BTC-XLM', 'BTC-TRX', 'BTC-GNT', 'BTC-WAVES', 'BTC-DGB', 'BTC-XEM', 
		'BTC-EMC2', 'BTC-STORJ', 'BTC-OMG', 'BTC-LTC', 'BTC-XEM', 'BTC-ETH', 'BTC-NEO', 'BTC-BTG', 'BTC-DASH'
		'BTC-LSK', 'BTC-NXT', 'BTC-GNT', 'BTC-POLY', 'BTC-STEEM', 'BTC-ETC', 'BTC-ZRX', 'BTC-RLC', 'BTC-CVC'
		'BTC-ZEN', 'BTC-QTUM', 'BTC-ZEN', 'BTC-BURST', 'BTC-STRAT']
		self.pid = pid
		self.strategy = strategy
		self.profit = profit
		self.stoploss = stoploss
		self.timeframe = timeframe
		self.status = status
		

	def check_buy(self):
		Bittrex = _BITTREX.Bittrex(self.id)
		for pair in self.pairs:
			Strategy  = _STRATEGY.Strategy(self.id, pair)
			if(Strategy.contra_turtle() == 'buy'):
			## DADOS PARA ORDEM
				price_now = Bittrex.getTicker(pair)
				amount = float(0.1)/float(price_now)
				print ("[+] Moeda  %s esta dando sinal de entrada... \n" % (pair))
				Order = _ORDER.Order(bot_id=self.id, buy_value=price_now, amount=amount, pair=pair)
				Order.execute_order_buy()
				break
	
	def checkSell(self, Order):
		trans = db.getOrder(self.id)
		price_now = Lib.getTicker(pair)
		fix_profit = trans['buy_value']+(trans['buy_value']*self.profit)
		stoploss = trans['buy_value'] * (1 - self.stoploss)
		
		if(price_now <= stoploss):
			Order.execute_order_sell()
			print ("[+] Venda via stoploss ... \n")
			return

		if(price_now >= fix_profit):
			Order.execute_order_sell()
			print ("[+] Venda via lucro fixo ... \n")
			return

	# CHECAGEM PARA LIBERACAO DE COMPRA
	# 0: LIVRE | 1: IMPEDIDO
	def free_buy(self):
		trans = db.getOrder(self.id)
		num_order = db.getOpenOrders(self.id)

		##ORDEM DE COMPRA JA ABERTA
		##BOT EM MODO SIMULACAO
		if(num_order > 0  and self.status == 0):
			print ("[+] Temos uma ordem aberta de compra... \n")
			return 1 #ORDEM JA ABERTA DE VENDA

		return 0

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