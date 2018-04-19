#dict = {'nome':'null', 'key':'null', 'secret':'null'}
#dict['nome'] = ('gabriel_')
#dict['key'] = ('q4r6zw4CXMGynsdQhRgzcs1PuOBfT1uCCwBG2op0fue7Qr33XvH23Cn0W5SMgWGU') 
#dict['secret'] = ('8PVopsBzr0piU66t3dEiPoxTuZUfVCemWdkjI5zN9OhEZcyPxgeO4UaAD1jM0zG0')
# coding=utf-8
import numpy as np
from binance.client import Client 
from binance.enums import ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC, SIDE_BUY, SIDE_SELL
import botconfig
from datetime import datetime
import numpy as np
import requests
import helpers
import botconfig
import sys
import json
import routines
import time

class ApiData:
    def checkLogin(self, idt, key):
        client = Client(idt, key)
        status = client.get_system_status()
        if (status['msg'] == 'normal'):
            print ("Logado em simulacao\n")
        else:
            sys.exit(0)

login = ApiData()
client = Client("","")
login.checkLogin("","")

def loginAPI(bot_config):
    db = botconfig.Db()
    print("logando na  api")
    acc_config = db.getConfigAcc(str(bot_config['user_id']))
    client = Client(str(acc_config['api_key']), str(acc_config['api_secret']))
    status = client.get_system_status()
    if (status['msg'] == 'normal'):
        print ("Login Ok")
        return client
    else:
        sys.exit(0)

class Binance_opr(ApiData):
    def getCandles(self, coin, period):
        """This function returns a candlestick list in a especific time interval
        
        Arguments:
            coin {[string]} -- Coin in binance format
            period {[interval]} -- Candlestic interval
        
        Returns:
            [list] -- CandleList
        """
        '''
            API TURNS MODEL
            1499040000000,      // Open time
            "0.01634790",       // Open
            "0.80000000",       // High
            "0.01575800",       // Low
            "0.01577100",       // Close
            "148976.11427815",  // Volume
            1499644799999,      // Close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "17928899.62484339" // Ignore
        '''
        if(period == 'Day'):
            candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_1DAY)
            candles = candles[len(candles)-20:len(candles)-1]
        elif(period == 'hour'):
            candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_1HOUR)
            candles = candles[len(candles)-20:len(candles)-1]                  
        elif(period == 'thirtyMin'):
            candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_30MINUTE)
            candles = candles[len(candles)-20:len(candles)-1]
        elif(period == 'fiveMin'):
            candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_5MINUTE)
            candles = candles[len(candles)-20:len(candles)-1]
        elif(period == 'oneMin'):
            candles = client.get_klines(symbol= coin, interval=Client.KLINE_INTERVAL_1MINUTE)
            candles = candles[len(candles)-20:len(candles)-1]
        #map
        opentime = []
        lopen = []
        lhigh = []
        llow = []
        lclose = []
        lvol = []
        closetime = []

        for candle in candles:
            opentime.append(candle[0])
            lopen.append(candle[1])
            lhigh.append(candle[2])
            llow.append(candle[3])
            lclose.append(candle[4])
            lvol.append(candle[5])
            closetime.append(candle[6])
        
        lopen = np.array(lclose).astype(np.float)
        lhigh = np.array(lhigh).astype(np.float)
        llow = np.array(llow).astype(np.float)
        lclose = np.array(lclose).astype(np.float)
        lvol = np.array(lvol).astype(np.float)
        return lopen, lhigh, llow, lclose, lvol, closetime      

    def getMean(self, coin, bot_config):
        """Mean in 30 candles
        
        Arguments:
            coin {[string]} -- currency in binance format
        
        Returns:
            [type] -- this function returns a mean of 30 candles
        """
        lclose = self.getCandles(coin, bot_config['period'])
       	lclose = np.array(lclose).astype(np.float)
        lclose = lclose[len(lclose)-30:len(lclose)]
        return lclose.mean()
    
    def getPriceNow(self, coin):
        """Price now
        
        Arguments:
            coin {[string]} -- currency in binance format
        
        Returns:
            [float] -- this function returns the atual currency price
        """
        r = requests.get("https://www.binance.com/api/v3/ticker/price?symbol=" + coin)
        r = r.content
        jsonResponse = json.loads(r.decode('utf-8'))
        return float(jsonResponse['price'])

    def getOrder(self, bot_config, data_decision, orderID, client):
        """get order
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- decision dict
            orderID {[string]} -- order id from binance
        
        Returns:
            [dict] -- this function returns a especific order
        """
        try:    
            order = client.get_order(symbol=bot_config['currency'], orderId=orderID)#(str(bot_config['currency'])), orderId=orderID)
            return order
        except:
            print("erro ao abrir ordem")

    def getOpenOrders(self, bot_config, data_decision, client):
        """get open orders
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- decision dict
        
        Returns:
            [bool] -- this function returns true if have a open order in a currency
        """
        orders = client.get_open_orders(symbol=bot_config['currency'])
        if not orders:
            return True   
        return False

    def getClientBalance(self, client):
        """get client balance from binance wallet
        
        Returns:
            [float] -- returns free BTC from botwork
        """
        balance = client.get_asset_balance(asset='BTC')
        print (balance)
        return balance['free']
         
    def getPrecision(self, coin):
        data = client.get_symbol_info(coin)
        return data['filters'][1]['minQty']

    def createBuyOrder(self, data, bot_config, data_decision):
        """
            AQUI A MAGICA ACONTECE 
        """
        check = routines.Routines()
        if not (check.orderBuyStatus(bot_config, data_decision)):
            db = botconfig.Db()
            if not (bot_config['active']):
                print('Inserindo simulada')
                db.insertBuyOrder(data)
            else: 
                client = loginAPI(bot_config)
                status = client.get_system_status()
                price = "%.8f" % (data_decision['price_now'])
                print(price)

                if(bot_config['active'] == 1 and status['msg'] == 'normal'):
                    ammount = float(self.getClientBalance(client))*bot_config['order_value']/float(data_decision['price_now'])
                    precision = float(self.getPrecision(bot_config['currency']))
                    if (precision == 1):
                        ammount = int(ammount) 
                    elif (precision == 0.01):
                        ammount = "%.2f" % ammount
                    else: 
                        ammount = "%.3f" % ammount

                    print('Quantidade')
                    print(ammount)            
                    #try:
                    order = client.create_order(symbol=bot_config['currency'],side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC, quantity=ammount, price= str(price))
                    time.sleep(300)
                    #except:
                    #return 
                    print (order)    
                    orderID = order['orderId']
                    orders = self.getOrder(bot_config, data_decision, orderID, client)
                    if(float(orders['executedQty']) == 0 ):
                        print('Timeout excedido, ordem cancelada')
                        client.cancel_order(symbol=bot_config['currency'], orderId=orderID)
                        return
                    else:
                        data['qnt'] = orders['executedQty']
                        data['qnt'] = ammount
                        data['buy_uuid'] = orderID
                        db.insertBuyOrder(data)

    def createSellOrder(self, data, bot_config, data_decision):
        """This function start a sell order
        
        Arguments:
            data {[dict]} -- data from insert in database 
            bot_config {[dict]} -- bot setup from database
            data_decision {[dict]} -- transactions detals
        """
        print ('entrou na funcao de venda')
        db = botconfig.Db()
        if not (bot_config['active']):
            print('inserindo os dados de venda no bd')  
            db.commitSellOrder(data)
        else:
            client = loginAPI(bot_config)
            status = client.get_system_status()
            if(bot_config['active'] and status['msg'] == 'normal'):
                print('Pronto pra criar ordem de venda')
                price = "%.8f" % data_decision['price_now']
                #try:
                order = client.create_order(symbol=bot_config['currency'],side=SIDE_SELL,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC, quantity=data_decision['trans']['quantity'], price=str(price))
                time.sleep(300)
                #except:
                #print('erro criando a ordem de venda')
                #    return
                orderID = order['orderId']
                orders = self.getOrder(bot_config, data_decision, orderID, client)
                if(float(orders['executedQty']) == 0 ):
                        print('Timeout excedido, ordem cancelada')
                        client.cancel_order(symbol=bot_config['currency'], orderId=orderID)
                        return
                print ('ORDEM DE VENDA ID ' + str(order['orderId']))
                data['sell_uuid'] = order['orderId']
                db.commitSellOrder(data)