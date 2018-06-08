# coding=utf-8
# pylint: disable=W0612
import MySQLdb as mysql
import os
import datetime
import pytz
import helpers


class Db:
    def getConn(self):
        try:
            db = mysql.connect(host="localhost", user="root",
                               passwd="gabsghell", db="protrade")
            #db = mysql.connect(host="127.0.0.1", user="root", passwd="Gv9KP70E316v", db="protrader")
            cursor = db.cursor()
            return db, cursor
        except:
            print('Erro, getCOnn()')

    def insertBuyOrder(self, data):
        dt = helpers.Helpers()
        db, cursor = self.getConn()
        query = ("INSERT INTO transactions (bot_id, buy_value, quantity, sell_value, selled, date_open, buy_uuid, sell_uuid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (data['bot_id'], data['valor'], data['qnt'],
                               0.0, 0, dt.time_now(), str(data['buy_uuid']), ''))
        db.commit()
        cursor.close()

    def commitSellOrder(self, data, bot_config):
        dt = helpers.Helpers()
        db, cursor = self.getConn()
        row, trans = self.getBuyOrders(data['bot_id'])
        query = ("UPDATE transactions SET sell_value=(%s), selled=(%s), date_close=(%s), sell_uuid=(%s), taxa=(%s) , profit=(%s)  WHERE id=(%s)")
        value = float(data['sell_value'])
        profit = float(data['profit'])
        taxa = float(data['taxa'])
        cursor.execute(query, (value, "1", dt.time_now(),
                               data['sell_uuid'], taxa, profit, trans['id']))
        db.commit()

        query = ("UPDATE bot SET credits = (%s) WHERE id=(%s)")
        credits = str(data['credits'])
        print(credits)
        print(bot_config['id'])
        cursor.execute(query, (credits, bot_config['id']))
        print('a')
        db.commit()
        cursor.close()

    def getBuyOrders(self, bot_id):
        try:
            db, cursor = self.getConn()
            query = ("SELECT * FROM transactions WHERE bot_id = %s and selled = %s")
            cursor.execute(query, (bot_id, 0))
            trans = cursor.fetchone()
            db.commit()
            cursor.close()
            if(cursor.rowcount > 0):
                obj = {
                    'result': True,
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
                return False, False
            count = cursor.rowcount
            return count, obj
        except:
            print("ERRO: getBuyOrders.")

    def getConfigAcc(self, user_id):
        # try:
        db, cursor = self.getConn()
        query = ("SELECT * FROM users WHERE id = %s")
        cursor.execute(query, (user_id,))
        data = cursor.fetchone()
        db.commit()
        cursor.close()
        obj = {
            'id': data[0],
            'name': data[1],
            'email': data[2],
            'api_secret': data[9],
            'api_key': data[8],
        }
        return obj
        # except:
        #    print("ERRO: getConfigAcc.")

    def getConfigBot(self, bot_id):
        try:
            db, cursor = self.getConn()
            query = ("SELECT * FROM bot WHERE id = %s")
            cursor.execute(query, (bot_id,))
            data = cursor.fetchone()
            currency = self.convert(data[3])
            db.commit()
            cursor.close()
            obj = {
                'id': data[0],
                'user_id': data[1],
                'exchange': data[2],
                'currency': currency,
                'strategy_buy': data[4],
                'percentage': data[5],
                'pid': data[6],
                'active': data[7],
                'order_value': float(data[8]),
                'period': data[9],
                'stoploss': data[10],
                'min_order': data[11],
                'credits': data[12]
            }
            return obj
        except:
            print('Erro, getCOnfigBot()')

    def convert(self, string):
        try:
            converted = string.split('-')
            converted = converted[1] + converted[0]
            return converted
        except:
            return string

    def setPID(self, bot_id):
        try:
            db, cursor = self.getConn()
            pid = os.getpid()
            query = ("UPDATE bot SET pid=(%s) WHERE id=(%s)")
            cursor.execute(query, (pid, bot_id))
            db.commit()
            cursor.close()
        except:
            print("ERRO: setPID.")