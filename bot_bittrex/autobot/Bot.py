import db as _DATABASE
import Order as _ORDER
import Exchange as _EXCHANGE
from datetime import datetime
from datetime import timedelta


		
class Bot():
	def __init__(self, params=None):
		self.id = params['id']
		self.user_id = params['user_id']
		self.exchange = params['exchange']
		self.strategy = params['strategy']
		self.pid = params['pid']
		self.status = params['status']

		

	def buy_routine(self):
		# 1 - LOAD SIGNALS
		SIGNALS = self.load_signals()
		#PROCESSAR SINAIS
		for signal in SIGNALS:
			# 2 - CHECK BUY
			if(self.free_buy(signal['market'], signal['currency']) == 1):
				PAIR = signal['currency']+'/'+signal['market']
				PRICE_NOW = _EXCHANGE.Exchange({'exchange':'binance'}).price(PAIR)
				AMOUNT = float(1)/float(PRICE_NOW)
				params = {
					'bot_id': self.id,
					'market': signal['market'],
					'currency': signal['currency'],
					'buy_value': PRICE_NOW,
					'sell_value': None,
					'amount': AMOUNT,
					'status': 0,
				}
				Order = _ORDER.Order(params)
				Order.execute_buy()
	
	def load_signals(self):
		Database = _DATABASE.Database()
		print("[+1+] Carregando sinais...")
		SIGNALS = Database.get_signals(self.strategy)
		print("[+2+] Sinais carregados com sucesso...")
		print("--------Signal Book---------------- \n")
		print(SIGNALS)
		print("--------------------------------- \n")
		return SIGNALS
	
	def load_orders(self):
		Database = _DATABASE.Database()
		print("[+1+] Carregando ordens...")
		ORDERS = Database.get_open_orders(self.id)
		print("[+2+] Ordens carregados com sucesso...")
		print("--------Ordens Abertas---------------- \n")
		for Order in ORDERS:
			PAIR = Order.currency+'/'+Order.market
			print("[+] ORDEM:%d, STATUS:%s, MARKET:%s, CURRENCY:%s, PRICE_BUY:%.8f, PRICE_TO_SELL:%.8f"% (Order.id, Order.status, Order.market, Order.currency, Order.buy_value, self.get_profit(PAIR, Order.buy_value, 0.01)[1]))
		print("--------------------------------- \n")
		return ORDERS

	

	def sell_routine(self):
		ORDERS = self.load_orders()
		for Order in ORDERS:
			## FREE TO SELL ORDER
			if(self.free_sell == 0):
				PAIR = Order.currency+'/'+Order.market
				if(self.get_profit(PAIR, Order.buy_value, 0.01)[0]):
					Order.sell_value = self.get_profit(PAIR, Order.buy_value, 0.01)[1]
					Order.status = 1
					Order.execute_sell()
					print ("[+] Venda via lucro fixo ... \n")

	# Get profit of transaction True or False
	def get_profit(self, pair, buy_value, profit):
		PRICE_NOW = _EXCHANGE.Exchange({'exchange':'binance'}).price(pair)
		PROFIT = buy_value + (buy_value * profit) # 1% profit
		return [PRICE_NOW >= PROFIT, PROFIT]


	# CHECAGEM PARA LIBERACAO DE VENDA
	# 0: LIVRE | 1: IMPEDIDO
	def free_buy(self, market, currency):
		Database = _DATABASE.Database()
		print("[+3+] Checando se o sinal ja foi utilizado...")
		'''if(self.status == 1):
			if(market == 'USDT'):
				balance = Bittrex.getBalance(market)
			else:
				balance = Bittrex.getBalance(market)
				balance = balance*7700 # BTC PRICE
			
			# 1-STEP: CHECK IF BALANCE AVAILABLE IS SMALLER 30, RETURN 0 IF TRUE
			if(balance < 30): # MIN 30 DOLARES
				print ("[+] Ordem minima nao atingida... \n")
				return 0'''

		# 2-STEP: CHECK IF EXIST OPEN ORDER FOR PAIR, RETURN 0 IF TRUE
		count_order = Database.get_order_pair(self.id, market, currency)
		if(count_order > 0):
			print ("[+] Temos uma ordem aberta de compra aberta para o par: %s-%s... \n"% (market, currency))
			return 0
			
		return 1


	# CHECAGEM PARA LIBERACAO DE COMPRA
	# 0: LIVRE | 1: IMPEDIDO
	def free_sell(self):
		# SEM NENHUMA REGRA DEFINIDA AINDA
		return 0
		#########################