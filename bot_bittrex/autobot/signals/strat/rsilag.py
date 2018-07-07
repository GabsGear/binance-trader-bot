from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import math
from datetime import datetime
from datetime import timedelta

# Import the backtrader platform
import backtrader as bt


# Create a Stratey
class Strategy(bt.Strategy):

    params = (
        ('period',21),
        ('signal', None)
    )
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.close = self.datas[0].close
        self.low = self.datas[0].low
        self.high = self.datas[0].high
        self.date = self.datas[0].datetime

        self.rsi_lag = bt.indicators.LaguerreRSI(self.datas[0])
        self.highest = bt.indicators.Highest(self.high, period=2)

    def next(self):
        global COUNT

        BUY_SIGNAL = self.rsi_lag[0] <= 0.01
        SELL_SIGNAL = self.close[0] >= self.high[0]
        
        day = str(self.data.num2date(self.date[0]).date().isoformat())
        hour = str(self.data.num2date(self.date[0]).time().isoformat())
        date = str(day+" "+hour)
        utc = datetime.utcnow() - timedelta(minutes=60)
        date_utc = str(utc.strftime('%Y-%m-%d %H:00:00'))

        if(date == date_utc):
            print("[+] DATE: %s-%s | CURRENCY: %s, RSI_LAG: %.8f \n"% (self.p.signal.currency, day, hour, self.rsi_lag[0]))
