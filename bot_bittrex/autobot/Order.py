import db as _DATABASE

		
class Order():
	def __init__(self, params=None):
		self.id = params['id']
		self.bot_id = params['bot_id']
		self.market = params['market']
		self.currency = params['currency']
		self.buy_value = params['buy_value']
		self.sell_value = params['sell_value']
		self.amount = params['amount']
		self.status = params['status']

	def execute_buy(self):
		Database = _DATABASE.Database()
		print("[+4+] Abrindo uma ordem para o par: %s-%s"% (self.market, self.currency))
		Database.open_order(self)
		return
	
	def execute_sell(self):
		Database = _DATABASE.Database()
		print("[+4+] Fechando uma ordem para o par: %s-%s"% (self.market, self.currency))
		Database.close_order(self)
		return
	
		
