import db

		
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
		db.insertBuyOrder(self)
		return
	
	def execute_sell(self):
		db.commitSellOrder(self)
		return
	
		
