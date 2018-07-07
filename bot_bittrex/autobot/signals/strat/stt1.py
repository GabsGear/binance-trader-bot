from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
import backtrader as bt
from Signal import Signal as _SIGNAL

# Import the backtrader platform
import backtrader as bt


# Create a Stratey
class Strategy(bt.Strategy):

    params = (
        ('period', 21),
        ('pair', None),
        ('date', None)
    )

    def __init__(self):
        self.ao = bt.indicators.AroonOsc(self.datas[0])
        self.hig = bt.indicators.Highest(self.datas[0].high, period=2)
        self.date = self.datas[0].datetime


    def next(self):
        #print(self.ao[0])
        date = str(self.data.num2date(self.date[0]).date().isoformat())
        hour = str(self.data.num2date(self.date[0]).time().isoformat())
        if(str(self.p.date) == date+' '+hour):
            pair = str(self.p.pair).split("/")
            if(self.ao[0] <= -75.0):
                params = {
                    'market': pair[1],
                    'currency': pair[0],
                    'strategy': 0,
                    'signal': 0,
                    'timeframe': '1h',
                }
                Signal = _SIGNAL(params)
                if(Signal.new()):
                    Signal.insert()
                    print("Date:%s, AO:%.2f"% (self.p.date, self.ao[0]))
        
            




