import db

		
class Order():
	def __init__(self, bot_id=None, buy_value=None, amount=None, pair=None, buy_uuid=None):
		pair = pair.split("-")
		self.bot_id = bot_id
		self.buy_value = buy_value
		self.amount = amount
		self.status = 0
		self.market = pair[0]
		self.currency = pair[1]
		self.buy_uuid = buy_uuid

	def execute_order_buy(self):
		db.insertBuyOrder(self)
		return
	
	def execute_order_sell(self):
		db.commitSellOrder(self)
		return
	
		
