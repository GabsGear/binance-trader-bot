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
	cursor.execute(query, (data['bot_id'], data['valor'], data['qnt'], 0.0, 0, str(time_now()), '-', data['buy_uuid'], ''))
	db.commit()
	cursor.close()

def commitSellOrder(data):
	db, cursor = getConn()
	trans = getBuyOrder(data['bot_id'])
	query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s) WHERE id=(%s)")
	value = float(data['sell_value'])
	cursor.execute(query, (value, "1", str(time_now()), data['sell_uuid'], trans['id'] ))
	db.commit()
	cursor.close()


def getBuyOrder(bot_id):
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
			'buy_uuid': trans[8],
			'sell_uuid': trans[9],
		}
	else:
		obj = False
	cursor.close()
	return obj
	#except:
	#print("ERRO: getBuyOrders.")

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
				'api_secret': data[5],
				'api_key': data[6],
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
				'strategy_sell': data[5],
				'percentage': data[6],
				'pid': data[7],
				'active': data[8],
				'max_order': data[9],
				'order_value': float(data[10]),
				'period': data[11],
				'stoploss': data[12]
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
	ct = datetime.datetime.now(tz=brasil)
	return ct.strftime("%d/%m/%y-%X")