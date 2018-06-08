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
        ('period',21),
    )
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.period)
        # MACD Indicator
        self.macd = bt.indicators.MACD(self.datas[0], period_me1=12, period_me2=26, period_signal=9)
        self.sma = bt.indicators.SMA(self.datas[0], period=50)
        # Cross of macd.macd and macd.signal
        self.mcross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
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
            if 'name' in order.info:
                self.log("%s: REF : %s / %s / PRICE : %.8f /" %
                         (order.info['name'], order.ref,
                          self.data.num2date(order.executed.dt).date().isoformat(),
                          order.executed.price))
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
        # Simply log the closing price of the series from the reference
        #self.log('Close, %.8f' % self.dataclose[0])
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        #self.log('MACD | LINE:%.8f | SIGNAL: %.8f'% (self.macd.lines.macd[0], self.macd.lines.signal[0]))
        # Check if we are in the market
        if not self.position:
            # Not yet ... we MIGHT BUY if ...
            if(self.rsi[0] < 30.0):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            if(self.dataclose[0] > self.sma[0]):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('SELL CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
                self.order.addinfo(name="PROFIT")



    def writeOutput(self, msg):
        x = datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backend\backtest\data\output.txt''')
        file = open(x, 'a+')
        file.write('[+] ' + msg + "\n")
        file.close()




class Quantity(bt.Sizer):
        params = (('stake', 1),)
        def _getsizing(self, comminfo, cash, data, isbuy):
            position = self.broker.getposition(data)
            print(position)
            if(isbuy):
                #buy_price = float(self.strategy.buyprice)
                #print("Preco comprado:"+str(self.strategy.buyprice))
                #print(str(self.strategy.order))
                amount = math.floor(cash/data.close[0])
                self.p.stake = amount
                #print("valor que quero comprar:")
                #print(self.p.stake*data.close[0])
                #print("valor que tenho:")
                #print(cash)
                return self.p.stake
            # Sell situation
            if not position.size:
                return 0  # do not sell if nothing is open

            return self.p.stake