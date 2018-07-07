from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import ccxt
import datetime
import backtrader as bt
import backtrader.feeds as btfeed
import Signal as _SIGNAL
import time
from strat import stt1
import pandas as pd

_BINANCE = ccxt.binance()
_BITTREX = ccxt.bittrex()

PAIRS = {
    'BTC': ['NEO', 'LTC', 'TRX', 'BNB', 'EOS', 'WAVES', 'SC', 'XRP', 'ETH', 'ZEN']
}

def main():
    while(True):
        for currency in PAIRS['BTC']:
            pair = str(currency+"/BTC")
            bt_prepare(pair)

def bt_prepare(pair):
    cerebro = bt.Cerebro(stdstats=False)
    _STRATEGY = stt1.Strategy

    cerebro.addstrategy(_STRATEGY)
    cerebro.addsizer(bt.sizers.SizerFix, stake=1)

    # Loading data to backtrader from exchange using CCXT
    matrix = get_candles(pair, '1h')
    candles = pd.DataFrame(matrix)
    candles[0] = candles[0].apply(to_datetimeindex)
    candles[0] = candles[0].apply(to_Timestamp)
    date = candles[0][candles.index[-1]]

    cerebro.addstrategy(_STRATEGY, date=date, pair=pair)
    cerebro.addsizer(bt.sizers.SizerFix, stake=1)

    data = data_feed(dataname=candles, nocase=False)
    cerebro.adddata(data)
    #print(_STRATEGY)
    # Run over everything
    cerebro.run()
    #cerebro.plot()



class data_feed(btfeed.PandasData):
    params = (
        ('nocase', False),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1)
    )


def to_datetimeindex(unixtimestamp):
    t = datetime.datetime.fromtimestamp(unixtimestamp / 1e3)
    return t.strftime("%Y-%m-%d %H:%M:%S")

def to_Timestamp (stringtime):
    return pd.Timestamp(stringtime)


def get_candles(pair=None, timeframe=None):
    delay = int(_BINANCE.rateLimit / 1000)
    time.sleep(delay)
    return _BINANCE.fetch_ohlcv(pair, timeframe)



main()