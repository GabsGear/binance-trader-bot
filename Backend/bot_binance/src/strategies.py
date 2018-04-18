# coding=utf-8
import binance_
import helpers
import botconfig
import numpy as np

class Desicion():
    """Data decision class
    this class get last transactions details from database, price now and adictional infos
    
    Returns:
        [dict] -- This functions returns transactions detals from database
    """
    __lopen = __lhigh = __llow = __lclose = __lvol = __closetime = " "
    
    def __init__(self, lopen, lhigh, llow, lclose, lvol, closetime):
        self.__lopen = (lopen) 
        self.__lhigh = (lhigh) 
        self.__llow = (llow) 
        self.__lclose = (lclose) 
        self.__lvol = (lvol) 
        self.__closetime = (closetime)

    #Getters
    def getLopen(self):
        return self.__lopen
    
    def getLhigh(self):
        return self.__lhigh      
    
    def getLlow(self):
        return self.__llow

    def getLclose(self):
        return self.__lclose

    def getLvol(self):
        return self.__lvol      
    
    def getCloseTime(self):
        return self.__closetime  

    def getDataDesicion(self, bot_config):
        db = botconfig.Db()
        bn = binance_.Binance_opr()
        price_now = bn.getPriceNow(bot_config['currency'])
        open_order, trans = db.getBuyOrders(bot_config['id'])
        data = {
            'price_now': price_now,
            'open_orders': open_order,
            'trans':trans,
            'o': self.getLopen(),
            'h': self.getLhigh(), 
            'l': self.getLlow(), 
            'c': self.getLclose(), 
            'v': self.getLvol(),
            't': self.getCloseTime(),
        }
        return data
    
class StrategiesBase(Desicion):
    """Strategies class
        The classe constructor set binance candlestick detals and start all strategies
    
    Returns:
        [string] -- this functions analyze the data and search a buy or sell oportunity
    """
    __lopen = __lhigh = __llow = __lclose = __lvol = " "
    
    def __init__(self, lopen, lhigh, llow, lclose, lvol):
        self.__lopen = (lopen) 
        self.__lhigh = (lhigh) 
        self.__llow = (llow) 
        self.__lclose = (lclose) 
        self.__lvol = (lvol) 

    def getLopen(self):
        return self.__lopen
    
    def getLhigh(self):
        return self.__lhigh      
    
    def getLlow(self):
        return self.__llow

    def getLclose(self):
        return self.__lclose

    def getLvol(self):
        return self.__lvol       

    def startTurtle(self, bot_config):
        data = super().getDataDesicion(bot_config)
        price_now = binance_.Binance_opr()
        price_now = price_now.getPriceNow(bot_config['currency'])


        print('price now = ' + str(price_now))
        high = self.getLhigh()
        high = high[len(high) - 2 : len(high)]
        tomin = self.getLlow()

        if(len(tomin) > 0):
            minn = min(high)
            maxx = max(high)
            print ('Buy at ' + str(minn))
            print(' .  ')
            if(data["price_now"] <= minn):
                print('sinal buy')
                return 'buy'
            if(data["price_now"] >= maxx):
                print('sinal sell')
                return 'sell'
        print('sinal none')
        return 'none'  

    def startPivot_up(self, bot_config):
        data = super().getDataDesicion(bot_config)
        flag = False
        close = self.getLclose() 
        pivot = max(close)

        if(len(close) > 0):
            if (data['price_now'] > pivot):
                flag = True

            if (flag):
                return 'buy'

            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.03:
                return 'sell'
        return 'none'

    def startInside(self, bot_config):
        data = super().getDataDesicion(bot_config)
        high, low = self.getLhigh(), self.getLlow()
        flag = False
        size = len(high) - 1

        if (high[size] < high[size - 1]) and (low[size] > low[size - 1]):
            price_now = binance_.Binance_opr()
            price_now = price_now.getPriceNow(bot_config['currency'])
            if price_now > high[size - 1]:
                flag = True

        if (flag):
            flag = False
            return 'buy'
                    
        if int(data['open_orders']) > 0 and float(data['price_now']) >= float(data['trans']['buy_value']) * 1.05:
            return 'sell'        
        return 'none'

    def startDoubleUp(self, bot_config):
        data = super().getDataDesicion(bot_config)
        close = self.getLclose()
        flag = False
        vol   = self.getLvol()
        if(len(close) > 0):
            if (close[1] > close[0]) and (vol[1] >= vol[0]):
                flag = True
        
            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.02:
                return 'sell'
        return 'none'