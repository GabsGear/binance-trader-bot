from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
import data
import fisher as fs

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
        self.high = self.datas[0].high
        self.date = self.datas[0].datetime

        # Indicators
        self.rsi_lag = bt.indicators.LaguerreRSI(self.datas[0])
        self.highest = bt.indicators.Highest(self.high, period=2)
        #self.aud = bt.indicators.AroonUpDownOscillator(self.datas[0])
        #self.across = bt.indicators.CrossOver(self.aud.aroonup, self.aud.aroondown)
        #self.pct = bt.indicators.PercentChange(self.datas[0].high, period=2)
        #self.ichimoku = bt.indicators.Ichimoku(self.datas[0])
        #self.vortex = bt.indicators.Vortex(self.datas[0])
        #self.ko = fs.KlingerOsc(self.datas[0])
        self.m1 = bt.indicators.ExponentialSmoothing(self.datas[0], period=56)
        self.m2 = bt.indicators.ExponentialSmoothing(self.datas[0], period=9)
        self.cross = bt.indicators.CrossOver(self.m2, self.m1)
        #self.bb = bt.indicators.BollingerBands(self.datas[0], devfactor=2)
        #self.vcross = bt.indicators.CrossOver(self.vortex.vi_plus, self.vortex.vi_minus)
        

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.win = self.lose = 0
        self.count = 0
        self.fix_profit = 0
        self.trades = [self.win, self.lose]


    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        #self.writeOutput("%s, %s" % (dt, txt))

    def start(self):
        self.trades = 0

    def notify_order(self, order):
        if order.status == order.Completed:
            # If a stop loss or take profit is triggered:
            if 'name' in order.info:
               self.log('h')
               #self.log("%.8f, %.8F, %.8f" %(self.price_buy, self.price_sell, self.perc(self.price_buy, self.price_sell) ))
            else:
                if (order.isbuy() and self.fix_profit == 1):
                    # Initialize our take profit and stop loss orders :
                    stop_loss = order.executed.price * (1.0 - 0.02)
                    take_profit = order.executed.price * (1.0 + 0.01)
                    
                    stop_order = self.sell(exectype=bt.Order.StopLimit, price=stop_loss)
                    stop_order.addinfo(name="STOP")
 
                    #OCO : One cancels the Other =&gt; The execution of one instantaneously cancels the other
                    takeprofit_order = self.sell(exectype=bt.Order.Limit, price=take_profit, oco=stop_order)
                    takeprofit_order.addinfo(name="PROFIT")
                    self.buyprice = order.executed.price
            self.order = None

    def next(self):
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        #print(self.pct[0])
        #blue = self.ichimoku.lines.senkou_span_a[0]
        #yellow = self.ichimoku.lines.senkou_span_b[0]
        #green = self.ichimoku.lines.kijun_sen[0]

        BUY_SIGNAL = self.cross > 0
        SELL_SIGNAL = self.cross < 0

        if self.order:
            return

        if not self.position:
            if(BUY_SIGNAL):
                self.price_buy = self.close[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            if(SELL_SIGNAL and self.fix_profit == 0):
                self.price_sell = self.close[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()



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
                print("cash:%.8f"%cash)
                print("valor:%.8f"%data.close[0])
                amount = math.floor(cash/data.close[0])*0.9
                self.p.stake = amount
                print("quantia:%.8f"%amount)
                return self.p.stake
            # Sell situation
            if not position.size:
                return 0  # do not sell if nothing is open

            return self.p.stake