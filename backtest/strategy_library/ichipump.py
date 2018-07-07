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
        #self.pgo = bt.indicators.PGO(self.datas[0])
        self.ichimoku = bt.indicators.Ichimoku(self.datas[0])
        #self.rmi = bt.indicators.RelativeMomentumIndex()
        self.ppo = bt.indicators.PercentagePriceOscillator(self.datas[0])
        self.vortex = bt.indicators.Vortex(self.datas[0])
        self.admx = bt.indicators.AverageDirectionalMovementIndexRating(self.datas[0])
        self.red = self.ichimoku.lines.tenkan_sen
        self.green = self.ichimoku.lines.kijun_sen
        self.ao = bt.indicators.AwesomeOscillator(self.datas[0])
        #self.bb = bt.indicators.BollingerBandsPct(self.datas[0])
        #self.ct = bt.indicators.CointN(self.datas[0])
        #self.cross = bt.indicators.CrossOver(self.red, self.green)
        self.dpp = bt.indicators.PivotPoint(self.data1)
        #self.dpp.plotinfo.plot = False  # deactivate plotting
        self.dpp.plotinfo.plotmaster = self.data0
        
        #print(self.ichimoku.lines.chikou_span[len(size-1)])
        #self.pp = bt.indicators.PercentagePriceOscillator(self.datas[0])
        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.win = self.lose = 0
        self.trades = [self.win, self.lose]

    def perc(self, buy, sell):
        x = sell*100/buy
        if x < 100:
            x = float(-1*(100-x))
        elif x > 100:
            x = float(x-100)
        else:
            x = float(0)
        if(x < 0):
            return x*-1
        return x

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
                self.log("%s: REF : %s / %s / BUY AT : %.8f / SELL AT: %.8F  " %
                         (order.info['name'], order.ref,
                          self.data.num2date(order.executed.dt).date().isoformat(), self.price_at_signal,
                          order.executed.price ))
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

        yellow = self.ichimoku.lines.senkou_span_b[0]
        blue = self.ichimoku.lines.senkou_span_a[0]
        red = self.ichimoku.lines.tenkan_sen[0]
        green = self.ichimoku.lines.kijun_sen[0]
        
        C = self.datas[0].close[0]
        L = self.datas[0].low[0]
        # Parametros ADMX
        ADX = self.admx.adx[0]
        ADXR = self.admx.adxr[0]
        # Parametros VORTEX
        PLUS = self.vortex.vi_plus[0]
        MINUS = self.vortex.vi_minus[0]
        # Calculando Rate Changes
        RATE_ADX = self.perc(ADX, ADXR)
        RATE_VOR = self.perc(PLUS, MINUS)

        #print("RATE ADX: %.8f"% RATE_ADX)
        #print("RATE VOR: %.8f"% RATE_VOR)
        #print(self.p[1])
        # Sinal de compra
        BUY = C > yellow and C > blue and L > yellow and L > blue and RATE_VOR > 15 and blue > yellow
        # Sinal de venda
        SELL = C < yellow and C < blue

        ############ ROTINA ###########
        if self.order:
            return

        if not self.position:
            # Not yet ... we MIGHT BUY if ...
            if(BUY):
                day = str(self.data.num2date(self.date[0]).date().isoformat())
                #if(day in DATES):
                # BUY, BUY, BUY!!! (with default parameters)
                self.log('BUY CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            if(SELL):
                self.log('SELL CREATE, %.8f' % (self.dataclose[0]))
                self.price_at_signal = self.dataclose[0]
                # Keep track of the created order to avoid a 2nd order
                takeprofit_order = self.sell()
                takeprofit_order.addinfo(name="PROFIT")

    def writeOutput(self, msg):
        x = datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\outputs\output.txt''')
        file = open(x, 'a+')
        file.write('[+] ' + msg + "\n")
        file.close()


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