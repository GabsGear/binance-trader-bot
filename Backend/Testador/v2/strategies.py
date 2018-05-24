# coding=utf-8
# pylint: disable=E1101
# pylint: disable=W0612
import binance_
import helpers
import botconfig
import numpy as np
import talib

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

    def getDataDecision(self, bot_config, pos):
        data = {
            'o': self.getLopen(),
            'h': self.getLhigh(), 
            'l': self.getLlow(), 
            'c': self.getLclose(), 
            'v': self.getLvol(),
            't': self.getCloseTime(),
        }
        return data

class statics():
    def perc(self, buy, sell):
        x = sell*100/buy
        if x < 100:
            return float(-1*(100-x))
        if x > 100:
            return float(x-100)
        return float(0)

    def getRSI(self, data, pos):
        size = pos
        close = data['c']
        close = close[0 : size]
        close= np.array(close, dtype=float)
        rsi = talib.RSI(close, 20)
        if(rsi[size-1] > 0.0):
            return rsi[size-1]
        else:
            return self.getRSISmall(data, pos)

    def getRSISmall(self, data, pos):
        size = pos
        close = data['c']
        close = close[0 : size]
        close= np.array(close, dtype=float)
        for c in close:
            c = c*100
        rsi = talib.RSI(close, 20)
        return rsi[size-1]

    def getMean(self, coin, bot_config):
        lclose=self.getCandles(coin, bot_config['period'])
        lclose=np.array(lclose).astype(np.float)
        lclose=lclose[len(lclose)-30:len(lclose)]
        return lclose.mean()


class StrategiesBase(statics):

    def startTurtle(self, bot_config, data, pos):
        high = data['h']
        tomax = data['h']
        tomax = tomax[pos - 2 : pos]
        tomin = data['l']
        tomin = tomin[pos-20: pos] 
        open = data['o']
        price_now = open[pos + 1]
        if(len(tomin) > 0):
            minn = min(tomin)
            maxx = max(tomax)
            if(price_now <= minn):
                return 'buy'
            if(price_now >= maxx):
                return 'sell'
        return 'none'  

    def startPivotUp(self, bot_config, data, pos):
        lclose = data['c']
        lopen = data['o']
        lhigh = data['h']
        llow = data['l']
        
        size = pos
        pivot = {
            'c': lclose[size - 2],
            'o': lopen[size - 2]
        }

        maxHigh = max(lhigh)
        maxLow = max(llow)
        var = super().perc(pivot['o'], pivot['c'])

        pivotUp = var > 2.0 and pivot['c'] > maxHigh 
        pivotDown = var < -1.5 and pivot['c'] < maxLow

        if(pivotUp):
            return 'buy'

        if pivotDown:
                return 'sell'
        return 'none'

    def startInside(self, bot_config, data, pos):
        high, close= data['h'], data['c']
        open = data['o']
        flag = False
        size = pos
        price_now = open[pos+1]
        if (high[size - 1] < high[size - 2]) and (close[size - 1] >= close[size - 2]):
            if price_now > float(high[size]):
                flag = True

        if (flag):
            flag = False
            return 'buy'
                    
        if int(data['open_orders']) > 0 and float(price_now) >= float(data['trans']['buy_value']) * 1.05:
            return 'sell'        
        return 'none'

    def startDoubleUp(self, bot_config, data, pos):
        close = data['c']
        vol   = data['v']
        open = data['o']
        price_now = data[pos+1]
        flag = False
        if(len(close) > 0):
            if (close[len(close) - 2] > close[len(close) - 1]) and (vol[len(vol) - 2] >= vol[len(vol) - 1]):
                flag = True
        
            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and float(price_now) >= data['trans']['buy_value'] * 1.02:
                return 'sell'
        return 'none'

    def startFollowBTC(self, bot_config, data, pos):
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

        pivotUp = var > 3.0 and pivot['c'] > maxHigh 
        pivotDown = var < -1.5 and pivot['c'] < maxLow
        if pivotUp:
            return 'buy'
        if pivotDown:
                return 'sell'
        return 'none'

    def startRSIMax(self, bot_config, data, pos):
        high = data['h']
        tomax = high[pos-3:pos-1]
        maxx = max(tomax)
        print('calculando rsi')
        rsi = super().getRSI(data, pos)

        print('rsi = ' + str(rsi))
        if(bot_config['period'] == 'day'):
            if(rsi <= 30.0):
                return 'buy'  
        if(bot_config['period'] == 'thirtyMin'):
            if(rsi >= 60.0):
                return 'sell'    
        return 'none' 
        
    def startBreackChannel(self, bot_config, data, pos):
        tomin = data['l'][pos-20:pos] 
        tomax = data['h'][pos-2:pos] 
        last_l = data['l'][pos-1:pos]
        last_h = data['h'][pos-1:pos]

        if(len(tomin) > 0):
            #print "maior que 0"
            minn = min(tomin) 
            maxx = max(tomax) 
            hp = helpers.Helpers()
            #log = ('--- Estrategia Breack Channel MIN = ' + str(minn) + ' MAX = ' + str(maxx))
            #hp.writeOutput(bot_config['id'], log)
            
            if(last_l[0] <= minn):
                return 'buy'

            if(last_h[0]  >= maxx):
                return 'sell'
        return 'none'   

    def startBollingerBand(self, bot_config, data, pos):
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
            return 'buy'

        if(lhigh[size-1] >= upperBand):
            return 'sell'
        
        return 'none'

        