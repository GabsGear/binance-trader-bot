# coding=utf-8
# pylint: disable=W0612
import binance_
import strategies
import botconfig
import time

class Functions():
    def buyOrder(self, bot_config, data_decision, pos):
        bn = binance_.Binance_opr()
        price_now = data_decision['o'] 
        price_now = price_now[pos+1]

        data = self.createBuyData(bot_config, data_decision, price_now)
        print('Estrategia ' + str(bot_config['strategy_buy']) + ' Signal = ' + str(
            self.selectBuyStrategy(data, bot_config, data_decision, pos)) + ' Candle ' + str(pos))

        if (self.selectBuyStrategy(data, bot_config, data_decision, pos) == 'buy'):
            bn.createBuyOrder(data, bot_config, data_decision, price_now)
        return

    def createBuyData(self, bot_config, data_decision, price_now):      
        data = {
            'bot_id': bot_config['id'],
            'valor': price_now,
            'qnt': (float(bot_config['wallet'])*bot_config['order_value']/price_now),
            'buy_uuid': '',
        }
        return data

    def orderBuyStatus(self, bot_config, data_decision):
        db = botconfig.Db()
        open_order, trans = db.getBuyOrders(bot_config['id'])
        if (open_order and not bot_config['active']):
            return 1
        return 0

    def selectBuyStrategy(self, data, bot_config, data_decision, pos):
        st = strategies.StrategiesBase()
        if(bot_config['strategy_buy'] == 0):
            # CONTRA TURTLE
            return st.startTurtle(bot_config, data_decision, pos)
        elif (bot_config['strategy_buy'] == 1):
            return st.startInside(bot_config, data_decision, pos)  # INSIDE BAR
        elif(bot_config['strategy_buy'] == 2):
            # DOUBLLE UP
            return st.startDoubleUp(bot_config, data_decision, pos)
        elif(bot_config['strategy_buy'] == 3):
            return st.startPivotUp(bot_config, data_decision, pos)  # PIVOT UP
        elif(bot_config['strategy_buy'] == 4):
            return st.startRSIMax(bot_config, data_decision, pos)  # RSI
        elif(bot_config['strategy_buy'] == 5):
            return st.startFollowBTC(bot_config, data_decision, pos)  # BTC
        elif(bot_config['strategy_buy'] == 6):
            # breack channel
            return st.startBreackChannel(bot_config, data_decision, pos)
        elif(bot_config['strategy_buy'] == 7):
            return st.startBollingerBand(bot_config, data_decision, pos)

# ----------------------------------------sell
    def sellOrder(self, bot_config, data_decision, pos):
        bn = binance_.Binance_opr()
        fixProfit = self.getFixProfit(bot_config, data_decision)
        stoploss = self.getStopLoss(bot_config, data_decision)
        st = strategies.StrategiesBase()

        price_now = data_decision['o'] 
        price_now = price_now[pos+1]      
        
        data = self.getSellData(bot_config, data_decision, pos)
        if(price_now <= stoploss):
            print('stop loss')
            bn.createSellOrder(data, bot_config, data_decision, price_now)
            return

        elif(bot_config['strategy_buy'] == 6):
            if(st.startBreackChannel(bot_config, data_decision, pos) == 'sell'):
                print('Sell')
                bn.createSellOrder(data, bot_config, data_decision, price_now)
                return

        elif(price_now >= fixProfit and bot_config['strategy_buy'] != 6):
            bn.createSellOrder(data, bot_config, data_decision, price_now)
            return

    def orderSellStatus(self, bot_config, data_decision):
        db = botconfig.Db()
        open_order, trans = db.getBuyOrders(bot_config['id'])
        if(not open_order and not bot_config['active']):
            return 1
        # NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
        elif(not bot_config['active'] and not open_order):
            return 1
        elif not (trans):
            return 1
        # NAO VENDER EM QUANTO ORDEM DE COMPRA ABERTA
        return 0

    def getSellData(self, bot_config, data_decision, pos):
        bn = binance_.Binance_opr()
        price_now = data_decision['o'] 
        price_now = price_now[pos+1]
        data = {
            'bot_id': bot_config['id'],
            'sell_value': price_now,
        }
        return data

    def getFixProfit(self, bot_config, data_decision):
        db = botconfig.Db()
        open_order, trans = db.getBuyOrders(bot_config['id'])
        return float(trans['buy_value']+trans['buy_value']*bot_config['percentage'])

    def getStopLoss(self, bot_config, data_decision):
        db = botconfig.Db()
        open_order, trans = db.getBuyOrders(bot_config['id'])
        return float(trans['buy_value']*(1-float(bot_config['stoploss'])))

class Routines(Functions):
    def startBuyRoutine(self, bot_config, data_decision, pos):
        if(super().orderBuyStatus(bot_config, data_decision)):
            print('Algo comprado')
            return
        super().buyOrder(bot_config, data_decision, pos)

    def startSellRoutine(self, bot_config, data_decision, pos):
        if (super().orderSellStatus(bot_config, data_decision)):
            print('Nada comprado')
            return
        print('tentando vender')
        super().sellOrder(bot_config, data_decision, pos)
