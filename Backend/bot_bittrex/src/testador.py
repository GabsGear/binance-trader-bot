import bittrex_lib
import numpy as np

candles = bittrex_lib().Bittrex()



class TestStrategy:
    def test(self,market, time):
        candles = bittrex_func.getCandleList(market, time)
        print (candles)
        print (self.inside_bar(candles))


    def contra_turtle(self, data):
        size = len(data['c'])

        tomin = data['l'][size-21:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
        tomax = data['h'][size-3:size-1]  ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 2

        if(len(tomin) > 0):
            #print "maior que 0"
            minn = min(tomin) ## CALCULO O MINIMO DESSES 20 CANDLES
            maxx = max(tomax) ## CALCULO O MAXIMO DESSES 2 CANDLES
            if(data['price_now'] <= minn):
                #print "LANCEI COMPRA"
                return 'buy'
            if(data['price_now'] >= maxx):
                #print "LANCEI VENDA"
                return 'sell'

        return 'none'

    def inside_bar(self, data):
        size = len(data['c'])
        flag = False

        high = np.array(data['h'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
        low = np.array(data['l'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
        close = np.array(data['c'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

        if(len(high) > 0):
            if (high[1] < high[0]) and (close[1] >= close[0]):
                if data['price_now'] > high[0]:
                    flag = True

        
            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.05:
                return 'sell'

        return 'none'

    def double_up(self, data):
        data
        size = len(data['c'])
        flag = False

        vol   = np.array(data['v'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4
        close = np.array(data['c'][size-3:size-1]) ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 4

        if(len(close) > 0):
            if (close[1] > close[0]) and (vol[1] >= vol[0]):
                flag = True

        
            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.02:
                return 'sell'

        return 'none'

    def pivot_up(self, data):
        data = data
        size = len(data['c'])
        flag = False

        close = data['c'][size-20:size-1] ##CORTO O VETOR DE CANDLES E DEIXO ELES COM TAMANHO 20
        pivot = max(close)

        if(len(close) > 0):
            if (data['price_now'] > pivot):
                flag = True

            if (flag):
                return 'buy'
            
            if data['open_orders'] > 0 and data['price_now'] >= data['trans']['buy_value'] * 1.03:
                return 'sell'

        return 'none'



TestStrategy.test("none","DGDBTC", "ONEDAY")

print ('sadasd')




