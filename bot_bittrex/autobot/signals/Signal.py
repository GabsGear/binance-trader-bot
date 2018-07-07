import pandas as pd
from datetime import datetime
from datetime import timedelta
import MySQLdb as mysql
import os
import sys

class Signal():
	
	def __init__(self, path=None, market=None, currency=None, strategy=None, signal=None, timeframe=None):
		self.market = market
		self.currency = currency
		self.strategy = strategy
		self.signal = signal
		self.timeframe = timeframe
		self.path = path

	# Get instance connection with database
	def get_socket(self):
		db = mysql.connect(host="127.0.0.1", user="root", passwd="", db="protrader")
		cursor = db.cursor()
		return db, cursor

	def insert(self):
		db, cursor = self.get_socket()
		query = ("INSERT INTO signals (market, currency, strategy, signalto, date) VALUES (%s, %s, %s, %s, %s)")
		cursor.execute(query, (self.market, self.currency, self.strategy, self.signal, self.time_now()))
		db.commit()
		cursor.close()
	
	def new(self):
		db, cursor = self.get_socket()
		query = ("SELECT * FROM signals WHERE currency=%s ORDER BY id desc")
		cursor.execute(query, (self.currency,))
		signal = cursor.fetchone()
		count  = cursor.rowcount
		cursor.close()
		if(count > 0):
			date_utc = datetime.utcnow()
			elapsed = date_utc-signal[5]
			if(self.timeframe == 'hour'):
				minutes = 120
			else:
				minutes = 60

			print(elapsed)
			if(elapsed < timedelta(minutes=minutes)):
				print("JA TEM SINAL")
				return False
		print("NAO TEM SINAL")
		return True
	
	def time_now(self):
		return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

