from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
import data

# Import the backtrader platform
import backtrader as bt
global DATES
DATES = ['2018-04-26', '2018-04-28', '2018-04-29', '2018-05-02', '2018-05-03', '2018-05-05', '2018-05-09', '2018-05-13', '2018-05-18', '2018-05-20', '2018-05-24', '2018-05-27', '2018-05-29', '2018-05-31', '2018-06-02', '2018-06-03', '2018-06-05']

# Create a Stratey
class Strategy(bt.Strategy):
    params = (
        ('period',21),
    )
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.date = self.datas[0].datetime
        #self.rsi = bt.indicators.RSI(self.datas[0], period=14)
        self.ctt = bt.indicators.Lowest(self.datas[0].low, period=20)
        self.oa = bt.indicators.AccelerationDecelerationOscillator(self.datas[0], period=10)
        self.ama = bt.indicators.AdaptiveMovingAverage(self.datas[0])
        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.win = self.lose = 0
        self.trades = [self.win, self.lose]


    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        #print("[+]"+str(dt)+"[+]"+str(txt))
        self.writeOutput("[+]"+str(dt)+"[+]"+str(txt))

    def start(self):
        self.trades = 0

    def notify_order(self, order):
        if order.status == order.Completed:
            # If a stop loss or take profit is triggered:
            if 'name' in order.info:
                self.log("%s: REF : %s / %s / BUY AT : %.8f / SELL AT: %.8F / VAR: %.8f %" %
                         (order.info['name'], order.ref,
                          self.data.num2date(order.executed.dt).date().isoformat(), self.price_at_signal,
                          order.executed.price, data.perc(self.price_at_signal, order.executed.price) )
            else:
                if order.isbuy():
                    # Initialize our take profit and stop loss orders :
                    '''stop_loss = order.executed.price * (1.0 - 0.05)
                    take_profit = order.executed.price * (1.0 + 0.03)
                    
                    stop_order = self.sell(exectype=bt.Order.StopLimit, price=stop_loss)
                    stop_order.addinfo(name="STOP")
 
                    #OCO : One cancels the Other =&gt; The execution of one instantaneously cancels the other
                    takeprofit_order = self.sell(exectype=bt.Order.Limit, price=take_profit, oco=stop_order)
                    akeprofit_order.addinfo(name="PROFIT")

                    self.log("SignalPrice : %.8f Buy: %.8f, Stop: %.8f, Profit : %.8f, Cost: %.8f"
                             % (self.price_at_signal,
                                order.executed.price,
                                stop_loss,
                                take_profit,
                                order.executed.value))
                    self.buyprice = order.executed.price
                    self.order = None''' 
            self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.8f, NET %.8f' %
                 (trade.pnl, trade.pnlcomm))
        if trade.pnl > 0:
            self.win += 1
            self.trades = self.win, self.lose

            self.log('WIN TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            self.log('################################')
        else:
            self.lose += 1
            self.trades = self.win, self.lose
            self.log('LOSS TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            self.log('################################')

    def next(self):
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        global DATES
        if self.order:
            return
        #print(self.datas[0].btc_var[0])
        # Check if we are in the market
        #print("SUPORTE:%.8f, PRICE:%.8f" % (self.ctt[0], self.datas[0].low[0]))
        print("AMA: %.8f"% self.ama[0])
        if not self.position:
            # Not yet ... we MIGHT BUY if ...
            #if(self.oa[0] > 0 and self.ama[0] < self.dataclose[0]):
            day = str(self.data.num2date(self.date[0]).date().isoformat())
            if(day in DATES):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            #if(self.oa[0] < 0)
            day = str(self.data.num2date(self.date[0]).date().isoformat())
            if(day not in DATES):
                self.log('SELL CREATE, %.8f' % (self.dataclose[0]))
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
                self.order.addinfo(name="PROFIT")

    def writeOutput(self, msg):
        x = datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\outputs\output.txt''')
        file = open(x, 'a+')
        file.write('[+] ' + msg + "\n")
        file.close()


