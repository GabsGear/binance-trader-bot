import db as _DATABASE

		
class Order():
	def __init__(self, id=None, bot_id=None, market=None, currency=None, buy_value=None, sell_value=None, amount=None, status=None):
		self.id = id
		self.bot_id = bot_id
		self.market = market
		self.currency = currency
		self.buy_value = buy_value
		self.sell_value = sell_value
		self.amount = amount
		self.status = status

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
	
		
