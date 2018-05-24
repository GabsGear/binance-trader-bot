from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt

class breakChannel(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas.close
        self.datalow = self.datas.low
        self.datahigh = self.datas.high
        # To keep track of pending orders
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.8f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.8f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def next(self):
        # Simply log the closing price of the series from the reference
        #self.log('Close, %.8f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:
            size = len(self.dataclose)
            tomin = self.datalow[size-21:size-1]
            tomax = self.datahigh[size-3:size-1]
            last_l = self.datalow[size-2:size-1]
            last_h = self.datahigh[size-2:size-1]
                
            minn = min(tomin) 
            maxx = max(tomax) 

            # Not yet ... we MIGHT BUY if ...
            if(last_l[0] <= minn):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.8f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()

        else:

            # Already in the market ... we might sell
            if(last_h[0] >= maxx):
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.8f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
