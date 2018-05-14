# coding=utf-8
# pylint: disable=E1101
# pylint: disable=W0612
import binance_
import helpers
import botconfig
import numpy as np
<<<<<<< HEAD
import talib
=======
import talib as tb
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144

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

    def getDataDecision(self, bot_config):
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
<<<<<<< HEAD

class statics():
=======
    
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
    def perc(self, buy, sell):
        x = sell*100/buy
        if x < 100:
            return float(-1*(100-x))
        if x > 100:
            return float(x-100)
        return float(0)

<<<<<<< HEAD
    def getRSI(self, data):
        size = len(data['c'])
        data = np.array(data['c'], dtype=float)
        rsi = talib.RSI(data, 20)
        if(rsi[size-1] > 0.0):
            return rsi[size-1]
        else:
            return self.getRSISmall(data)

    def getRSISmall(self, data):
        size = len(data['c'])
        data['c']= np.array(data['c'], dtype=float)
        for c in data['c']:
            c = c*100
        rsi = talib.RSI(data['c'], 20)
        return rsi[size-1]

class StrategiesBase(statics):
=======
    # def getRSI(self, data):
    #     size = len(data['c'])
    #     data['c'] = np.array(data['c'], dtype=float)
    #     rsi = tb.RSI(data['c'], 20)
    #     if(rsi[size-1] > 0.0):
    #         return rsi[size-1]
    #     else:
    #         return tb.getRSISmall(data)

    # def getRSISmall(self, data):
    #     size = len(data['c'])
    #     data['c']= np.array(data['c'], dtype=float)
    #     for c in data['c']:
    #         c = c*100
    #     rsi = tb.RSI(data['c'], 20)
    #     return rsi[size-1]
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144

    """Strategies class
        The classe constructor set binance candlestick detals and start all strategies
    
    Returns:
        [string] -- this functions analyze the data and search a buy or sell oportunity
    """    
    def startTurtle(self, bot_config, data):
        price_now = str(data['price_now'])
        hp = helpers.Helpers()

<<<<<<< HEAD
        log = ('price now = ' + str(price_now))
        hp.writeOutput(bot_config['id'], log)

        tomax = data['h']
        size = len(data['h'])
        tomax = tomax[len(tomax) - 2 : len(tomax)]
        tomin = data['l']
        tomin = tomin[len(tomin)-20:len(tomin)] 
        last_l = data['l'][size-1:size]

        if(len(tomin) > 0):
            minn = min(tomin)
            maxx = max(tomax)
            log =  ('Buy at ' + str(minn))
            hp.writeOutput(bot_config['id'], log)
            if(last_l[0] <= minn):
                log = ('sinal buy')
                hp.writeOutput(bot_config['id'], log)
=======
    def startTurtle(self, bot_config):
        data = super().getDataDecision(bot_config)
        price_now = binance_.Binance_opr()
        price_now = price_now.getPriceNow(bot_config['currency'])

        print('price now = ' + str(price_now))
        tomax = self.getLhigh()
        tomax = tomax[len(tomax) - 3 : len(tomax) - 1]
        tomin = self.getLlow()
        if(len(tomin) > 0):
            minn = min(tomin)
            maxx = max(tomax)
            print (' Buy at ' + str(minn))
            print(' .  ')
            if(data["price_now"] <= minn):
                print('sinal buy')
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
                return 'buy'
            if(data["price_now"] >= maxx):
                log = ('sinal sell')
                hp.writeOutput(bot_config['id'], log)
                return 'sell'
        return 'none'  

<<<<<<< HEAD
    def startPivotUp(self, bot_config, data):
        lclose = data['c']
        lopen = data['o']
        lhigh = data['h']
        llow = data['l']
        
=======
    def startPivotUp(self, bot_config):
        lclose, lopen, lhigh, llow = self.getLclose(), self.getLopen(), self.getLhigh(), self.getLlow()
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
        size = len(lclose)
        pivot = {
            'c': lclose[size - 2],
            'o': lopen[size - 2]
        }

        maxHigh = max(lhigh)
        maxLow = max(llow)
        var = super().perc(pivot['o'], pivot['c'])

<<<<<<< HEAD
        pivotUp = var > 2.0 and pivot['c'] > maxHigh 
=======
        pivotUp = var > 3.0 and pivot['c'] > maxHigh 
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
        pivotDown = var < -1.5 and pivot['c'] < maxLow

        if(pivotUp):
            return 'buy'

        if pivotDown:
                return 'sell'
        return 'none'

<<<<<<< HEAD
    def startInside(self, bot_config, data):
        high, close= data['h'], data['c']
=======
    def startInside(self, bot_config):
        data = super().getDataDecision(bot_config)
        high, close= self.getLhigh(), self.getLclose()
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
        flag = False
        size = len(close) - 1

        if (high[size - 1] < high[size - 2]) and (close[size - 1] >= close[size - 2]):
<<<<<<< HEAD
            price_now = float(data['price_now'])
            if price_now > float(high[size]):
=======
            price_now = binance_.Binance_opr()
            price_now = price_now.getPriceNow(bot_config['currency'])
            if price_now > high[size]:
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
                flag = True

        if (flag):
            flag = False
            return 'buy'
                    
        if int(data['open_orders']) > 0 and float(data['price_now']) >= float(data['trans']['buy_value']) * 1.05:
            return 'sell'        
        return 'none'

<<<<<<< HEAD
    def startDoubleUp(self, bot_config, data):
        close = data['c']
        vol   = data['v']
=======
    def startDoubleUp(self, bot_config):
        data = super().getDataDecision(bot_config)
        close = self.getLclose()
        vol   = self.getLvol()
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
        flag = False
        if(len(close) > 0):
            if (close[len(close) - 2] > close[len(close) - 1]) and (vol[len(vol) - 2] >= vol[len(vol) - 1]):
                flag = True
        
            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.02:
                return 'sell'
        return 'none'

<<<<<<< HEAD
    def startFollowBTC(self, bot_config, data):
=======
    def startFollowBTC(self, bot_config):
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
        """
            Search pivot up on btc 
        """
        dt = binance_.Binance_opr()
        lopen, lhigh, llow, lclose, lvol, closetime = dt.getBTCCandles(bot_config['period'])

        size = len(lclose)
        pivot = {
            'c': lclose[size - 2],
            'o': lopen[size - 2]
        }
        maxHigh = max(lhigh)
        maxLow = max(llow)
        var = super().perc(pivot['o'], pivot['c'])
<<<<<<< HEAD

        pivotUp = var > 3.0 and pivot['c'] > maxHigh 
        pivotDown = var < -1.5 and pivot['c'] < maxLow
        if pivotUp:
            return 'buy'
        if pivotDown:
                return 'sell'
        return 'none'

    def startRSIMax(self, bot_config, data):
        high = data['h']
        size = len(high)
        tomax = high[size-3:size-1]
        maxx = max(tomax)
        rsi = super().getRSI(data)
        hp = helpers.Helpers()
        log = ('---Estrategia RSI -- RSI = ' + str(rsi))
        hp.writeOutput(bot_config['id'], log)
        

        if(bot_config['period'] == 'day'):
            if(rsi < 30.0):
                return 'buy'
        if(bot_config['period'] == 'hour'):
            if(rsi < 35.0):
                return 'buy'    
        if(bot_config['period'] == 'thirtyMin'):
            if(rsi < 40.0):
                return 'buy'    
        return 'none' 
        
    def startBreackChannel(self, bot_config, data):
        size = len(data['h'])
        tomin = data['l'][size-20:size] 
        tomax = data['h'][size-2:size] 
        last_l = data['l'][size-1:size]
        last_h = data['h'][size-1:size]

        if(len(tomin) > 0):
            #print "maior que 0"
            minn = min(tomin) 
            maxx = max(tomax) 
            hp = helpers.Helpers()
            #log = ('--- Estrategia Breack Channel MIN = ' + str(minn) + ' MAX = ' + str(maxx))
            #hp.writeOutput(bot_config['id'], log)
            
            if(last_l[0] <= minn):
                hp.writeOutput(bot_config['id'], "indicou compra no break.")
                return 'buy'

            if(last_h[0]  >= maxx):
                hp.writeOutput(bot_config['id'], "indicou venda no break.")
                return 'sell'
        return 'none' 

    def startBollingerBand(self, bot_config, data):
        lclose = data['c']
        llow = data['l']
        lhigh = data['h']
        interval = 20 #numero de candles
        nDesvios = 2 #numero de desvios padrao
        size = len(lclose)

        close = lclose[size - interval: size]
        mean = np.mean(close)
        desvio = np.std(close)

        upperBand = mean + (desvio * nDesvios)
        lowerBand = mean - (desvio * nDesvios)
        
        if(llow[size-1] <= lowerBand):
=======

        pivotUp = var > 3.0 and pivot['c'] > maxHigh 
        pivotDown = var < -1.5 and pivot['c'] < maxLow
        
        if pivotUp:
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
            return 'buy'
        if pivotDown:
                return 'sell'
        return 'none'

<<<<<<< HEAD
        if(lhigh[size-1] >= upperBand):
            return 'sell'
        
        return 'none'

        
=======
    # def startRSIMax(self, bot_config):
    #     data = self.getDataDecision(bot_config)
    #     high = self.getLhigh()
    #     size = len(high)
    #     tomax = high[size-3:size-1]
    #     maxx = max(tomax)
    #     rsi = super().getRSI(data)

    #     if(rsi < 30):
    #         return 'buy'
    #     if(data['price_now'] >= maxx):
    #         return 'sell'
    #     return 'none'
	
 
>>>>>>> 16a0b954ffb031d38ffc5bb59ef366fd3aab1144
