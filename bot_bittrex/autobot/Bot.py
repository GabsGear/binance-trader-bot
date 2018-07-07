import Bittrex as _BITTREX
import db as _DATABASE
import Strategy as _STRATEGY
import Order as _ORDER
import Lib as _LIB
from datetime import datetime
from datetime import timedelta


		
class Bot():
	def __init__(self, id = None, user_id = None, pid = None, status = None):
		self.id = id
		self.user_id = user_id
		self.pid = pid
		self.status = status
		

	def buy_routine(self):
		Bittrex  = _BITTREX.Bittrex()
		Database = _DATABASE.Database()
		Database.filter_signals()
		print("[+1+] Carregando sinais...")
		SIGNALS = Database.get_signals()
		print("[+2+] Sinais carregados com sucesso...")
		print("--------Signal Book---------------- \n")
		print(SIGNALS)
		print("--------------------------------- \n")
		for signal in SIGNALS:
			if(self.free_buy(signal['market'], signal['currency']) == 1):
				PAIR = signal['market']+'-'+signal['currency']
				PRICE_NOW = Bittrex.getTicker(PAIR)
				AMOUNT = float(1)/float(PRICE_NOW)
				Order = _ORDER.Order(bot_id=self.id, market=signal['market'], currency=signal['currency'], buy_value=PRICE_NOW, sell_value=None, amount=AMOUNT, status=0)
				Order.execute_buy()
	

	def sell_routine(self):
		Bittrex = _BITTREX.Bittrex()
		Database = _DATABASE.Database()
		Orders = Database.get_open_orders(self.id)
		print(Orders)
		for Order in Orders:
			#print("[+] Status da ordem e %s"% Order.status)
			if(self.free_sell == 0):
				price_now = Bittrex.getTicker(Order.market+"-"+Order.currency)
				fix_profit = Order.buy_value + (Order.buy_value * 0.01) # 1% profit
				print("[+] ORDEM:%d, MARKET:%s, CURRENCY:%s, PRICE:%.8f, SELL:%.8f"% (Order.id, Order.market, Order.currency, Order.buy_value, fix_profit))
				#if(price_now >= fix_profit):
				Order.sell_value = price_now
				Order.status = 1
				#Order.execute_sell()
				print ("[+] Venda via lucro fixo ... \n")
				return


	# CHECAGEM PARA LIBERACAO DE VENDA
	# 0: LIVRE | 1: IMPEDIDO
	def free_buy(self, market, currency):
		Bittrex = _BITTREX.Bittrex()
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
		trans = db.getOrder(self.id)
		Database = _DATABASE.Database()
		Orders = Database.get_open_orders(self.id)

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