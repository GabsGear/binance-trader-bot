# coding=utf-8
# API Key:
# baYMJ0rCsQEplo9ROTkejMCUhMqKeGHNCs2LnBvTUA7rF0GmzNDmQexCG2zHqAWk
# Secret Key:  To ensure safety, API Secret Key will only be displayed at the time of being created. And if the key is lost, you should delete the API and set up a new one.
# Iq7l85XHXxGEwHClejleZG4OAVTTzpQmhgJiSPwjbcMvJWRoodm7FeFVKEhBzuut
import binance_
import strategies
import helpers
import botconfig
import time

class Functions():
    def buyOrder(self, bot_config):
        """ this function start is responsable to check a possible buy order
            first analyze all last orders and check if haven't a pendent order for buy or sell
        Arguments:
            bot_config {[dict]} -- bot setup
        """
        bn = binance_.Binance_opr()
        
        lopen, lhigh, llow, lclose, lvol, closetime = bn.getCandles(str(bot_config['currency']), bot_config['period'])
        st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
        data_decision = st.getDataDesicion(bot_config)
        
        if(self.orderBuyStatus(bot_config, data_decision)):
            return

        data = self.createBuyData(bot_config, data_decision)   
        self.selectBuyStrategy(data, bot_config, data_decision)
        return

    def createBuyData(self, bot_config, data_decision):  
        """create buy data to insert in database
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
        
        Returns:
            [dict] -- data for database
        """
        data = {
            'bot_id': bot_config['id'],
            'valor': data_decision['price_now'],
            'qnt': float(bot_config['order_value'])/float(data_decision['price_now']),
            'buy_uuid': '',
        }
        return data


    def checkLastOrders(self, bot_config, data_decision, uuid): 
        """check the last order and verify the negociation status
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
            uuid {[string]} -- id from binance 
        
        Returns:
            [bool] -- return true if the last order is filled
        """
        if (bot_config['active']):
            bn = binance_.Binance_opr()
            order = bn.getOrder(bot_config, data_decision, uuid)
            if (order['status'] == 'FILLED'):
                return True   
        return False 

    def printDL(self):
        print('-----------------------------------------------')

    def orderBuyStatus(self, bot_config, data_decision):
        """the principal method to check the last orders
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
        
        Returns:
            [bool] -- this method return 0 when everything is ok and you want to buy
        """
        print('2- Verificando pendencias de ordens')
        if (data_decision['open_orders'] and not bot_config['active']):
            print ('Err Bot desativado com ordem aberta')
            self.printDL()
            return 1
        elif (data_decision['open_orders'] and bot_config['active']):
            print('Err Bot ativo com ordem de venda aberta')
            print(str(data_decision['open_orders']) + ' Ordens abertas')
            self.printDL()
            return 1 
        elif(bot_config['active'] and data_decision['trans']):
            if not (self.checkLastOrders(bot_config, data_decision, data_decision['buy_uuid'])): 
                print('Err Selled nao possibilita compra')
                self.printDL()  
                return 1            
        return 0

    def selectBuyStrategy(self, data, bot_config, data_decision): 
        """select strategy
        
        Arguments:
            data {[type]} -- data to create a buy order
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
        """
        print('5- Selecionando minha estrategia de compra')
        bn = binance_.Binance_opr()
        for i in range(0, 3):
            print('PROCURANDO O SINAL')
            if(bot_config['strategy_buy'] == i):
                if(self.mapStrategy(bot_config)[i] == 'buy'):
                    bn.createBuyOrder(data, bot_config, data_decision)

    def sellOrder(self, bot_config):
        bn = binance_.Binance_opr()
        lopen, lhigh, llow, lclose, lvol, closetime = bn.getCandles(str(bot_config['currency']), bot_config['period'])
        st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
        data_decision = st.getDataDesicion(bot_config)

        if (self.orderSellStatus(bot_config, data_decision)):
            self.printDL()
            return
        else:
            stoploss = self.getStopLoss(bot_config, data_decision)
            fixProfit = self.getFixProfit(bot_config, data_decision)
            data = self.getSellData(bot_config, data_decision)
            if(data_decision['price_now'] <= stoploss):
                print('4.5 - Venda por stopLoss')
                bn.createSellOrder(data, bot_config, data_decision)
                return
            self.selectSellStrategy(data, bot_config, data_decision, fixProfit)
        return

    def orderSellStatus(self, bot_config, data_decision):
        if(not data_decision['open_orders'] and not bot_config['active']):
            return 1 
        
        elif not (data_decision['trans']):
            return 1

        elif(bot_config['active'] and data_decision['open_orders']): ##NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
            return 1
            
        elif(not bot_config['active'] and data_decision['open_orders']): ##NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
            return 1

        elif(bot_config['active'] and data_decision['trans']):
            if not (self.checkLastOrders(bot_config, data_decision, data_decision['buy_uuid'])): 
                return 1      
        return 0

    def getSellData(self, bot_config, data_decision):
        data = {
            'bot_id': bot_config['id'],
            'sell_value': data_decision['price_now'],
            'sell_uuid': '',
        }
        return data

    def getFixProfit(self, bot_config, data_decision):
        return data_decision['trans']['buy_value']+data_decision['trans']['buy_value']*bot_config['percentage']

    def getStopLoss(self, bot_config, data_decision):
        return data_decision['trans']['buy_value']*(1-float(bot_config['stoploss']))
    
    #seleciona a estrategia
    def selectSellStrategy(self, data, bot_config, data_decision, fixProfit): 
        bn = binance_.Binance_opr()

        if(bot_config['strategy_sell'] and data_decision['price_now'] >= fixProfit):
            bn.createSellOrder(data, bot_config, data_decision)   
        else:
            for i in range(0, 3):
                if(bot_config['strategy_buy'] == i):
                    if(self.mapStrategy(bot_config)[i] == 'sell'): #teste
                        bn.createSellOrder(data, bot_config, data_decision)   

    def mapStrategy(self, bot_config): 
        """map the strategies
        
        Arguments:
            bot_config {[dict]} -- bot setup
        
        Returns:
            [type] -- return a map with all strategies
        """
        bn = binance_.Binance_opr()
        lopen, lhigh, llow, lclose, lvol, closetime = bn.getCandles(str(bot_config['currency']), bot_config['period'])
        st = strategies.StrategiesBase(lopen, lhigh, llow, lclose, lvol)
        map = {
            0: st.startTurtle(bot_config), #CONTRA TURTLE
            1: st.startInside(bot_config), #INSIDE BAR
            2: st.startDoubleUp(bot_config), #DOUBLLE UP
            3: st.startPivot_up(bot_config), #PIVOT UP
        }
        return map

class Routines(Functions):
    def startBuyRoutine(self, bot_config):
        print('1- Iniciando rotina de compra')
        super().buyOrder(bot_config)
    def startSellRoutine(self, bot_config):
        print('1- Iniciando rotina de venda') 
        super().sellOrder(bot_config)

