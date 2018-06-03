import MySQLdb as mysql
import os
import datetime
import pytz
import sys
import Bot as _BOT

def getConn():
	db = mysql.connect(host="127.0.0.1", user="root", passwd="libano252528", db="protrader")
	cursor = db.cursor()
	return db, cursor


def insertBuyOrder(Order):
	db, cursor = getConn()
	query = ("INSERT INTO transactions (bot_id, market, currency, buy_value, amount) VALUES (%s, %s, %s, %s, %s)")
	cursor.execute(query, (Order.bot_id, Order.market, Order.currency, Order.buy_value, Order.amount))
	db.commit()
	cursor.close()

def commitSellOrder(data):
	db, cursor = getConn()
	trans = getOrder(data['bot_id'])
	query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s) WHERE id=(%s)")
	value = float(data['sell_value'])
	cursor.execute(query, (value, "1", time_now(), data['sell_uuid'], trans['id'] ))
	db.commit()
	cursor.close()


def getOrder(bot_id):
	try:
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
				'pair': trans[11],
			}
		else:
			obj = False
		cursor.close()
		return obj
	except:
		print("[+] getOrder Function. Error : " + str(sys.exc_info()))
		sys.exit()

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
				'key': data[5],
				'secret': data[6],
				'credits': data[9],
		       }
		return obj
	except:
		print("[+] getConfigAcc Function. Error : " + str(sys.exc_info()))
		sys.exit()

def getInstanceBot(bot_id):
	db, cursor = getConn()
	query = ("SELECT * FROM bot WHERE id = %s")
	cursor.execute(query, (bot_id,))
	data = cursor.fetchone()
	db.commit()
	cursor.close()
	Bot = _BOT.Bot(
		bot_id = data[0], 
		user_id = data[1],
		exchange = data[2],
		pid = data[3],
		strategy = data[4],
		profit = data[5],
		status=data[6],
		timeframe = data[7],
		stoploss = data[8]
	)
	return Bot

def setPID(bot_id):
	try:
		db, cursor = getConn()
		pid = os.getpid()
		query = ("UPDATE bot SET pid=(%s) WHERE id=(%s)")
		cursor.execute(query, (pid, bot_id))
		db.commit()
		cursor.close()
	except:
		print("[+] setPID Function. Error : " + str(sys.exc_info()))
		sys.exit()

def time_now():
	brasil = pytz.timezone('America/Sao_Paulo')
	return datetime.datetime.now(tz=brasil).strftime('%Y-%m-%d %H:%M:%S')