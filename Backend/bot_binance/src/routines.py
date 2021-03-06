# coding=utf-8
# pylint: disable=W0612
import binance_
import strategies
import helpers
import botconfig
import time

class Functions():
    def buyOrder(self, bot_config, data_decision):
        """ this function start is responsable to check a possible buy order
            first analyze all last orders and check if haven't a pendent order for buy or sell
        Arguments:
            bot_config {[dict]} -- bot setup
        """
        bn = binance_.Binance_opr()
        data = self.createBuyData(bot_config, data_decision) 
        print(self.selectBuyStrategy(data, bot_config, data_decision))  
        if (self.selectBuyStrategy(data, bot_config, data_decision) == 'buy'):
            bn.createBuyOrder(data, bot_config, data_decision)
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

    def checkLastOrders(self, bot_config, data_decision, uuid, client): 
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
            order = bn.getOrder(bot_config, data_decision, uuid, client)
            if (order['status'] != 'NEW'):
                return True   
        return False 

    def orderBuyStatus(self, bot_config, data_decision):
        """the principal method to check the last orders
        
        Arguments:
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
        
        Returns:
            [bool] -- this method return 0 when everything is ok and you want to buy
        """
        if (data_decision['open_orders'] and not bot_config['active']):
            return 1
        elif (data_decision['open_orders'] and bot_config['active']):
            return 1         
        return 0

    def selectBuyStrategy(self, data, bot_config, data_decision): 
        """select strategy
        
        Arguments:
            data {[type]} -- data to create a buy order
            bot_config {[dict]} -- bot setup
            data_decision {[dict]} -- transactions detals
        """
        print('Selecionando estrategia numero ' + str(bot_config['strategy_buy']))
        st = strategies.StrategiesBase()
        if(bot_config['strategy_buy'] == 0):
            return st.startTurtle(bot_config, data_decision) #CONTRA TURTLE
        elif (bot_config['strategy_buy'] == 1):
            return st.startInside(bot_config, data_decision) #INSIDE BAR
        elif(bot_config['strategy_buy'] == 2):        
            return st.startDoubleUp(bot_config, data_decision) #DOUBLLE UP
        elif(bot_config['strategy_buy'] == 3):   
            return st.startPivotUp(bot_config, data_decision) #PIVOT UP
        elif(bot_config['strategy_buy'] == 4):   
            return st.startRSIMax(bot_config, data_decision) #RSI
        elif(bot_config['strategy_buy'] == 5):   
            return st.startFollowBTC(bot_config, data_decision) #BTC
        elif(bot_config['strategy_buy'] == 6):  
            return st.startBreackChannel(bot_config, data_decision) #breack channel
        elif(bot_config['strategy_buy'] == 7):   
            return st.startBollingerBand(bot_config, data_decision)

    def sellOrder(self, bot_config, data_decision):
        bn = binance_.Binance_opr()
        hp = helpers.Helpers()
        fixProfit = self.getFixProfit(bot_config, data_decision)
        stoploss = self.getStopLoss(bot_config, data_decision)
        st = strategies.StrategiesBase()
        
        data = self.getSellData(bot_config, data_decision)
        if(data_decision['price_now'] <= stoploss):
            bn.createSellOrder(data, bot_config, data_decision)
            return
           
        elif(bot_config['strategy_buy'] == 6):
            if(st.startBreackChannel(bot_config, data_decision) == 'sell'):
                bn.createSellOrder(data, bot_config, data_decision)
                return  

        elif(data_decision['price_now'] >= fixProfit and bot_config['strategy_buy'] != 6):
            bn.createSellOrder(data, bot_config, data_decision)  
            return

    def orderSellStatus(self, bot_config, data_decision):
        if(not data_decision['open_orders'] and not bot_config['active']):
            return 1 
        elif(not bot_config['active'] and not data_decision['open_orders']):
            return 1
        elif not (data_decision['trans']):
            return 1
        elif(bot_config['active'] and not data_decision['open_orders']): 
        return 0

    def getSellData(self, bot_config, data_decision):
        data = {
            'bot_id': bot_config['id'],
            'sell_value': data_decision['price_now'],
            'sell_uuid': '',
        }
        return data

    def getFixProfit(self, bot_config, data_decision):
        return float(data_decision['trans']['buy_value']+data_decision['trans']['buy_value']*bot_config['percentage'])

    def getStopLoss(self, bot_config, data_decision):
        return float(data_decision['trans']['buy_value']*(1-float(bot_config['stoploss'])))
    
class Routines(Functions):
    def get_config(self, bot_config):
        bn = binance_.Binance_opr()
        lopen, lhigh, llow, lclose, lvol, closetime = bn.getCandles(str(bot_config['currency']), bot_config['period'])
        st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
        data_decision = st.getDataDecision(bot_config)
        return data_decision
        
    def startBuyRoutine(self, bot_config):
        data_decision = self.get_config(bot_config)
        st = strategies.StrategiesBase()
        if(st.btcPercentage() == 0):
            return
        if(super().orderBuyStatus(bot_config, data_decision)):
            return  
        super().buyOrder(bot_config, data_decision)

    def startSellRoutine(self, bot_config):
        data_decision = self.get_config(bot_config)
        if (super().orderSellStatus(bot_config, data_decision)):
            return
        super().sellOrder(bot_config, data_decision)

