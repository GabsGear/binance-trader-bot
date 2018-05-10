import binance_
import helpers
import talib 
import numpy as np

class ContraTurtle():

    # recebe os candles no construtor  
    __lopen = __lhigh = __llow = __lclose = __lvol = " "

    def __init__(self, lopen, lhigh, llow, lclose, lvol):
        self.__lopen = (lopen) 
        self.__lhigh = (lhigh) 
        self.__llow = (llow) 
        self.__lclose = (lclose) 
        self.__lvol = (lvol) 

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

    def startTurtle(self, coin, futureLow, futureHigh, lastOperation):

        #price_now = binance_.Binance_opr()
        #price_now = price_now.getPriceNow(coin)
        close = self.getLclose()
        
        minn = min(close)
        maxx = max(close)

        #obj.writeOutput('id 12312312312312', 'PRECO:'+str(price_now)+'|ALVO COMPRA:'+str(minn))
        #obj.writeOutput('botConf[id]', 'PRECO:'+str(price_now)+'|ALVO VENDA:'+str(max))
        obj = helpers.Helpers()
        sLoss = obj.isStopLoss(lastOperation, minn, futureLow)

        if futureLow < minn and lastOperation[0] == 0: #lastoperation[lastbuy, lastSell]
            return 0 #buy
        #stopLoss
        elif sLoss:
            return 3
        elif futureHigh >= maxx and lastOperation[1] == 0: 
            return 1 #sell
        return 2 #none
            
class insideBar():
        # recebe os candles no construtor
    
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



    def startInside(self, coin, futureLow, futureHigh, percent, lastOperation):
        high, low = self.getLhigh(), self.getLlow()
        obj = helpers.Helpers()

        flag = False
        time = 0
        size = len(high) - 1

        obj = helpers.Helpers()
        sLoss = obj.isStopLoss(lastOperation, low[size], futureLow)

        if (high[size] < high[size - 1]) and (low[size] > low[size - 1]):
            #price_now = binance_.Binance_opr()
            #price_now = price_now.getPriceNow(coin)
            if futureLow > high[size - 1]:
                flag = True

  
        if (flag) and lastOperation[0] == 0:
            #print (time)
            obj.tstampToData(time)
            flag = False
            return 0 #buy
            
        if lastOperation[1] == 0 and futureHigh >= lastOperation[0] * percent:
            return 1 #sell
        elif sLoss:
            return 3
        else:
            return 2

class double_up():
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

    def startDOubleUp(self, coin, futureLow, futureHigh, percent, lastOperation):
        high, close = self.getLhigh(), self.getLclose() 
        flag = False

        obj = helpers.Helpers()
        sLoss = obj.isStopLoss(lastOperation, high[0], futureLow)

        if(len(high) > 0):
            if (high[1] < high[0]) and (close[1] >= close[0]):
                if futureLow > high[0]:
                    flag = True
   
            if (flag) and lastOperation[0] == 0:
                return 0
            
            elif sLoss:
                return 3
            
            if lastOperation[1] == 0 and futureHigh >= lastOperation[0] * percent:
                return 1

        return 2


class pivotUp():

    # recebe os candles no construtor  
    __lopen = __lhigh = __llow = __lclose = __lvol = " "

    def __init__(self, lopen, lhigh, llow, lclose, lvol):
        self.__lopen = (lopen) 
        self.__lhigh = (lhigh) 
        self.__llow = (llow) 
        self.__lclose = (lclose) 
        self.__lvol = (lvol) 

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

    def startPivot(self, coin, futureLow, futureHigh, lastOperation):
        flag = False
        obj = helpers.Helpers()
        close = self.getLclose() ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
        pivot = max(close)
        sLoss = obj.isStopLoss(lastOperation, close[0], futureLow)

        if(len(close) > 0):
            if (futureLow > pivot):
                flag = True

            if (flag) and lastOperation[0] == 0:
                return 0
            
            elif sLoss:
                return 3

            if lastOperation[1] == 0 and futureHigh >= lastOperation[0] * 1.03:
                return 1

        return 2


