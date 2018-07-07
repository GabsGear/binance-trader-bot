from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
import data

# Import the backtrader platform
import backtrader as bt

# Create a Stratey
class Strategy(bt.Strategy):

    params = (
        ('period',21),
    )
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.close = self.datas[0].close
        self.low = self.datas[0].low
        self.high = self.datas[0].datetime
        self.date = self.datas[0].datetime

        # Indicators
        self.rsi_lag = bt.indicators.LaguerreRSI(self.datas[0])
        self.highest = bt.indicators.Highest(self.high, period=2)

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.win = self.lose = 0
        self.count = 0
        self.trades = [self.win, self.lose]


    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        self.writeOutput("%s, %s" % (dt, txt))

    def start(self):
        self.trades = 0

    def notify_order(self, order):
        if order.status == order.Completed:
            self.order = None


    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        #self.log('OPERATION PROFIT, GROSS %.8f, NET %.8f' %(trade.pnl, trade.pnlcomm))
        if trade.pnl > 0:
            self.win += 1
            self.trades = self.win, self.lose

            #self.log('WIN TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            #self.log('################################')
        else:
            self.lose += 1
            self.trades = self.win, self.lose
            #self.log('LOSS TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            #self.log('################################')

    def next(self):
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        BUY_SIGNAL = self.rsi_lag[0] <= 0.01
        SELL_SIGNAL = self.close[0] >= self.high[0] 

        if self.order:
            return

        if not self.position:
            if(BUY_SIGNAL):
                self.price_buy = self.close[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            if(SELL_SIGNAL):
                self.price_sell = self.close[0]
                # Keep track of the created order to avoid a 2nd order
                takeprofit_order = self.sell()
                takeprofit_order.addinfo(name="PROFIT")




    def writeOutput(self, msg):
        path = r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\outputs'''
        x = datapath=(path+'\\'+str(sys.argv[1])+"-"+str(sys.argv[2])+".csv")
        file = open(x, 'a+')
        file.write(msg + "\n")
        file.close()
    
    def perc(self, buy, sell):
        x = sell*100/buy
        if x < 100:
            return float(-1*(100-x))
        if x > 100:
            return float(x-100)
        return float(0)


class Quantity(bt.Sizer):
        params = (('stake', 1),)
        def _getsizing(self, comminfo, cash, data, isbuy):
            position = self.broker.getposition(data)
            #print(position)
            if(isbuy):
                amount = math.floor(cash/data.close[0])*0.9
                self.p.stake = amount
                return self.p.stake
            # Sell situation
            if not position.size:
                return 0  # do not sell if nothing is open

            return self.p.stake