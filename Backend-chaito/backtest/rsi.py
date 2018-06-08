from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
# Import the backtrader platform
import backtrader as bt

# Create a Stratey
class Strategy(bt.Strategy):
    params = (
        ('period',14),
    )
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.period)
        self.order = None
        self.buyprice = None

        self.win = self.lose = 0
        self.trades = [self.win, self.lose]


    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        #print("[+]"+str(dt)+"[+]"+str(txt))
        print("[+]"+str(dt)+"[+]"+str(txt))

    def start(self):
        self.trades = 0

    def notify_order(self, order):
        if order.status == order.Completed:
            if 'name' in order.info:
                self.log("%s: REF : %s / %s / PRICE : %.8f /" %
                         (order.info['name'], order.ref,
                          self.data.num2date(order.executed.dt).date().isoformat(),
                          order.executed.price))
            else:
                if order.isbuy():
                    stop_loss = order.executed.price * (1.0 - 0.5)
                    take_profit = order.executed.price * (1.0 + 0.2)
 
                    stop_order = self.sell(exectype=bt.Order.StopLimit,
                                           price=stop_loss)
                    stop_order.addinfo(name="STOP")
                    takeprofit_order = self.sell(exectype=bt.Order.Limit,
                                                 price=take_profit,
                                                 oco=stop_order)
                    takeprofit_order.addinfo(name="PROFIT")

                    self.log("SignalPrice : %.8f Buy: %.8f, Stop: %.8f, Profit : %.8f, Cost: %.8f"
                             % (self.price_at_signal,
                                order.executed.price,
                                stop_loss,
                                take_profit,
                                order.executed.value))
                    self.buyprice = order.executed.price
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

        else:
            self.lose += 1
            self.trades = self.win, self.lose
            self.log('LOSS TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))


    def next(self):
        if self.order:
            return
        if not self.position:
            if(self.rsi[0] < 30.0):
                self.log('BUY CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                self.order = self.buy()

    def writeOutput(self, msg):
        datapath=('/home/gabs/Backend/Backend/Testador/Baktrader/logs/log.csv')
        file = open(datapath, 'a+')
        file.write('[+] ' + msg + "\n")
        file.close()
