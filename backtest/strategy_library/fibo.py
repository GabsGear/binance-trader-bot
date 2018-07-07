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
        self.pp = pp = bt.indicators.PivotPoint(self.data1)
        pp.plotinfo.plot = False  # deactivate plotting
        pp1 = pp()  # couple the entire indicators
        self.buysignal = self.data0.close < pp1.s2
        self.sellsignal = self.data0.close > pp1.lines.p
        bt.indicators.PrettyGoodOscillator(self.datas[0])
        #self.fpp = bt.studies.FibonacciPivotPoiont(self.data1)

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
                self.log("%s: REF : %s / %s / PRICE : %.8f /" %
                         (order.info['name'], order.ref,
                          self.data.num2date(order.executed.dt).date().isoformat(),
                          order.executed.price))
                #self.order = None
            else:
                if order.isbuy():
                    # Initialize our take profit and stop loss orders :
                    stop_loss = order.executed.price * (1.0 - 0.5)
                    take_profit = order.executed.price * (1.0 + 0.012)
 
                    stop_order = self.sell(exectype=bt.Order.StopLimit,
                                           price=stop_loss)
                    stop_order.addinfo(name="STOP")
 
                    #OCO : One cancels the Other =&gt; The execution of one instantaneously cancels the other
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
            if(self.buysignal):
                self.log('BUY CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        '''else:
            if(self.sellsignal):
                self.log('SELL CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()'''


    def writeOutput(self, msg):
        x = datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\outputs\output.txt''')
        file = open(x, 'a+')
        file.write('[+] ' + msg + "\n")
        file.close()




class Quantity(bt.Sizer):
        params = (('stake', 1),)
        def _getsizing(self, comminfo, cash, data, isbuy):
            position = self.broker.getposition(data)
            if(isbuy):
                amount = math.floor(cash/data.close[0])*0.9
                self.p.stake = amount
                return self.p.stake
            # Sell situation
            if not position.size:
                return 0  # do not sell if nothing is open

            return self.p.stake