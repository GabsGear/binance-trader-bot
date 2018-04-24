import MySQLdb as mysql
import os
import datetime
import pytz

def getConn():
	db = mysql.connect(host="127.0.0.1", user="root", passwd="libano252528", db="protrader")
	cursor = db.cursor()
	return db, cursor


def insertBuyOrder(data):
	#print data
	db, cursor = getConn()
	query = ("INSERT INTO transactions (bot_id, buy_value, quantity, sell_value, selled, date_open, date_close, buy_uuid, sell_uuid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
	cursor.execute(query, (data['bot_id'], data['valor'], data['qnt'], 0.0, 0, time_now(), '', data['buy_uuid'], ''))
	db.commit()
	cursor.close()

def commitSellOrder(data):
	db, cursor = getConn()
	trans = getBuyOrder(data['bot_id'])
	query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s) WHERE id=(%s)")
	value = float(data['sell_value'])
	cursor.execute(query, (value, "1", time_now(), data['sell_uuid'], trans['id'] ))
	db.commit()
	cursor.close()


def getOrder(bot_id):
	#try:
	db, cursor = getConn()
	query = ("SELECT * FROM transactions WHERE bot_id = %s order by id desc")
	cursor.execute(query, (bot_id, ))
	trans = cursor.fetchone()
	db.commit()
	#print(trans)
	if(cursor.rowcount > 0):
		obj = {
			'id': trans[0],
			'bot_id': trans[1],
			'buy_value': trans[2],
			'quantity': trans[3],
			'sell_value': trans[4],
			'selled': trans[5],
			'date_open': trans[6],
			'date_close': trans[7],
			'buy_uuid': trans[8],
			'sell_uuid': trans[9],
		}
	else:
		obj = False
	cursor.close()
	return obj
	#except:
	#print("ERRO: getBuyOrders.")

def delete_trans(id):
	db, cursor = getConn()
	query = ("DELETE FROM transactions WHERE id = %s")
	cursor.execute(query, (id,))
	db.commit()
	cursor.close()

def update_trans(id):
	db, cursor = getConn()
	query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s) WHERE id=(%s)")
	cursor.execute(query, (0, '0', '', '', id))
	db.commit()
	cursor.close()

def getOpenOrders(bot_id):
	db, cursor = getConn()
	query = ("SELECT * FROM transactions WHERE bot_id = %s and selled = %s")
	cursor.execute(query, (bot_id, 0))
	trans = cursor.fetchone()
	db.commit()
	count = cursor.rowcount
	cursor.close()
	return count


def getConfigAcc(user_id):
	try:
		db, cursor = getConn()
		query = ("SELECT * FROM users WHERE id = %s")
		cursor.execute(query, (user_id))
		data = cursor.fetchone()
		db.commit()
		cursor.close()
		obj = {
				'id': data[0],
				'name': data[1],
				'email': data[2],
				'bit_api_secret': data[5],
				'bit_api_key': data[6],
		       }
		
		return obj
	except:
		print("ERRO: getConfigAcc.")

def getConfigBot(bot_id):
	try:
		db, cursor = getConn()
		query = ("SELECT * FROM bot WHERE id = %s")
		cursor.execute(query, (bot_id,))
		data = cursor.fetchone()
		db.commit()
		cursor.close()
		obj = {
				'id': data[0],
				'user_id': data[1],
				'exchange': data[2],
				'currency': data[3],
				'strategy_buy': data[4],
				'percentage': float(data[5]),
				'pid': data[6],
				'active': data[7],
				'order_value': float(data[8]),
				'period': data[9],
				'stoploss': data[10]
		       }
		return obj
	except:
		print("ERRO: getConfigBot.")

def setPID(bot_id):
	try:
		db, cursor = getConn()
		pid = os.getpid()
		query = ("UPDATE bot SET pid=(%s) WHERE id=(%s)")
		cursor.execute(query, (pid, bot_id))
		db.commit()
		cursor.close()
	except:
		print("ERRO: setPID.")

def time_now():
	brasil = pytz.timezone('America/Sao_Paulo')
	return datetime.datetime.now(tz=brasil).strftime('%Y-%m-%d %H:%M:%S')