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

global COUNT

COUNT = 0


# Create a Stratey
class Strategy(bt.Strategy):

    params = (
        ('period', 21),
        #('signal', None)
    )

    def __init__(self):
        self.vortex = bt.indicators.Vortex(self.datas[0])
        self.plus = self.vortex.vi_plus


    def next(self):
        self.test = self.vortex.vi_plus.lines[0].get(0, 2)
        
            




