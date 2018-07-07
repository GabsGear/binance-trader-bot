import MySQLdb as mysql
import os
from datetime import datetime
from datetime import timedelta
import datetime as dt
import pytz
import sys
import Bot as _BOT
import Order as _ORDER


class Database():

	def __init__(self):
		self.db = mysql.connect(host="127.0.0.1", user="root", passwd="", db="protrader")
		self.cursor = self.db.cursor()


	def open_order(self, Order):
		query = ("INSERT INTO transactions (bot_id, market, currency, buy_value, amount, date_open) VALUES (%s, %s, %s, %s, %s, %s)")
		self.cursor.execute(query, (Order.bot_id, Order.market, Order.currency, Order.buy_value, Order.amount, self.time_now()))
		self.db.commit()
		self.cursor.close()

	def close_order(self, Order):
		query = ("UPDATE transactions SET sell_value=(%s), status=(%s), date_close=(%s) WHERE id=(%s)")
		self.cursor.execute(query, (Order.sell_value, Order.status, self.time_now(), Order.id))
		self.db.commit()
		self.cursor.close()


	def get_open_orders(self, bot_id):
		query = ("SELECT * FROM transactions WHERE bot_id = %s AND status = %s order by id desc")
		self.cursor.execute(query, (bot_id, 0))
		Orders = []
		if(self.cursor.rowcount > 0):
			for trans in self.cursor:
				Order = _ORDER.Order(
					id = trans[0],
					bot_id = trans[1], 
					market = trans[2], 
					currency = trans[3], 
					buy_value = trans[4],
					sell_value = trans[5],
					amount = trans[6],
					status = trans[7], 
				)
				Orders.append(Order)
			return Orders	
		else:
			return None
		self.cursor.close()

	# VERIFICA SE EXISTE UMA ORDEM PENDENTE PARA O PAR SOLICITADO
	# PAIR: MARKET-CURRENCY
	def get_order_pair(self, bot_id, market, currency):
		query = ("SELECT * FROM transactions WHERE bot_id=%s AND market=%s AND currency=%s AND status=0 order by id desc")
		self.cursor.execute(query, (bot_id, market, currency))
		return self.cursor.rowcount

	def delete_trans(self, id):
		query = ("DELETE FROM transactions WHERE id = %s")
		self.cursor.execute(query, (id,))
		self.db.commit()
		self.cursor.close()

	def update_trans(self, id):
		query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s) WHERE id=(%s)")
		cursor.execute(query, (0, '0', '', '', id))
		db.commit()
		cursor.close()

	def getOpenOrders(self, bot_id):
		query = ("SELECT * FROM transactions WHERE bot_id = %s and selled = %s")
		self.cursor.execute(query, (bot_id, 0))
		trans = self.cursor.fetchone()
		self.db.commit()
		count = self.cursor.rowcount
		self.cursor.close()
		return count


	def getConfigAcc(self, user_id):
		try:
			query = ("SELECT * FROM users WHERE id = %s")
			self.cursor.execute(query, (user_id,))
			data = self.cursor.fetchone()
			self.db.commit()
			self.cursor.close()
			obj = {
					'id': data[0],
					'key': data[5],
					'secret': data[6],
					'credits': data[9],
				}
			return obj
		except:
			print("[+] getConfigAcc Function. Error : " + str(sys.exc_info()))
			sys.exit()

	def getInstanceBot(self, bot_id):
		query = ("SELECT * FROM bot WHERE id = %s")
		self.cursor.execute(query, (bot_id,))
		data = self.cursor.fetchone()
		self.db.commit()
		self.cursor.close()
		Bot = _BOT.Bot(
			id = data[0], 
			user_id = data[1],
			strategy = data[3],
			profit = data[4],
			pid = data[5],
			status = data[6],
			stoploss = data[7]
		)
		return Bot

	def get_signals(self):
		SIGNALS = []
		query = ("SELECT * FROM signals")
		self.cursor.execute(query, )
		for sig in self.cursor:
			signal = {
				'id': sig[0],
				'market': sig[1],
				'currency': sig[2],
				'strategy': sig[3],
				'signalto': sig[4],
				'date': sig[5],
			}
			SIGNALS.append(signal)
		return SIGNALS
	
	def filter_signals(self):
		SIGNALS = self.get_signals()
		for sig in SIGNALS:
			date_utc = datetime.utcnow()
			elapsed = date_utc-sig['date']
			#print("UTC NOW: %s"% date_utc)
			#print("ESSE SINAL PASSOU: %s"% elapsed)
			if(elapsed > timedelta(minutes= 30)):
				#print(elapsed)
				#print(sig['id'])
				query = ("DELETE FROM signals WHERE id = %s")
				self.cursor.execute(query, (sig['id'], ))
				self.db.commit()


	def time_now(self):
		brasil = pytz.timezone('America/Sao_Paulo')
		return dt.datetime.now(tz=brasil).strftime('%Y-%m-%d %H:%M:%S')
