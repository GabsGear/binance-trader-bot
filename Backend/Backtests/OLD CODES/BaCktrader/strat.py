from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import helpers 
# Import the backtrader platform
import backtrader as bt


# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RSI(self.datas[0], period=14)
        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.win = self.lose = 0
        self.trades = [self.win, self.lose]

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def notify_trade(self, trade):
        hp = helpers.Helpers()
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.8f, NET %.8f' %
                 (trade.pnl, trade.pnlcomm))
        hp.logcsv('OPERATION PROFIT, GROSS %.8f, NET %.8f' %
                 (trade.pnl, trade.pnlcomm))
        if trade.pnl > 0:
            self.win += 1
            self.trades = self.win, self.lose
            self.log('WIN TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            hp.logcsv('WIN TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))

        else:
            self.lose += 1
            self.trades = self.win, self.lose
            self.log('LOSS TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))
            hp.logcsv('LOSS TRADE   win: ' + str(self.win) + ' loss: ' + str(self.lose))

    def next(self):
        hp = helpers.Helpers()
        # Simply log the closing price of the series from the reference
        self.log('Close, %.8f' % self.dataclose[0])
        hp.logcsv('Close, %.8f' % self.dataclose[0])
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.rsi[0] <= 30:
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.8f' % self.dataclose[0])
                hp.logcsv('BUY CREATE, %.8f' % self.dataclose[0])
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()

        else:
            if self.rsi[0] >= 60:
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('SELL CREATE, %.8f' % self.dataclose[0])
                hp.logcsv('SELL CREATE, %.8f' % self.dataclose[0])
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
