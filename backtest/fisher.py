import backtrader as bt
import math
import pandas as pd
import statsmodels.api as sm

__all__ = ['Fisher']

class Fisher(bt.Indicator):

    lines = ('Fx',)
    params = (('period', 20),)

    _alpha = 0.33
    _alphaFish = 0.5

    def __init__(self):

        self._scaledPrev = 0
        self._FxPrev = 0

        self._h = bt.indicators.Highest(self.data, period=self.p.period)
        self._l = bt.indicators.Lowest(self.data, period=self.p.period)

        super(Fisher, self).__init__()

    def next(self):

        d = self.data[0]

        h = self._h[0]
        l = self._l[0]

        Fx = self.l.Fx

        scaled = 2 * ((d - l) / (h - l) - .5)
        scaled = self._alpha * scaled + (1-self._alpha) * (self._scaledPrev if len(Fx) > 1 else scaled)

        if scaled > 0.9999:
            scaled = 0.9999
        elif scaled < -0.9999:
            scaled = -0.9999

        self._scaledPrev = scaled

        Fx[0] = math.log((1 + scaled) / (1 - scaled))
        self._FxPrev = Fx[0] = self._alphaFish * Fx[0] + (1-self._alphaFish) * (self._FxPrev if len(Fx) > 1 else Fx[0])



class KlingerOsc(bt.Indicator):
 
    lines = ('sig','kvo')
 
    params = (('kvoFast',34),('kvoSlow',55),('sigPeriod',13))
 
    def __init__(self):
        self.plotinfo.plotyhlines = [0]
        self.addminperiod(55)
 
        self.data.hlc3 = (self.data.high + self.data.low + self.data.close) / 3
        # This works - Note indexing should be () rather than []
        # See: https://www.backtrader.com/docu/concepts.html#lines-delayed-indexing
        self.data.sv = bt.If((self.data.hlc3(0) - self.data.hlc3(-1)) / self.data.hlc3(-1) >=0, self.data.volume, -self.data.volume)
        self.lines.kvo = bt.indicators.EMA(self.data.sv, period=self.p.kvoFast) - bt.indicators.EMA(self.data.sv, period=self.p.kvoSlow)
        self.lines.sig = bt.indicators.EMA(self.lines.kvo, period=self.p.sigPeriod)