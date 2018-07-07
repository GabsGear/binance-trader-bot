import ccxt
import time
import statsmodels.tsa as st
from statsmodels.tsa import stattools
from statsmodels.tsa.arima_model import ARMA
import statsmodels.api as sm
import matplotlib.pyplot as plt

_BINANCE = ccxt.binance()
_BITTREX = ccxt.bittrex()


delay = int(_BINANCE.rateLimit / 1000)
time.sleep(delay)
#ohlcvs = _BINANCE.fetch_ohlcv('BTC/USDT')
ohlcvs = _BINANCE.fetch_ohlcv('BTC/USDT', timeframe = '1h')

#print(_BINANCE.fetch_ticker('BTC/USDT'))
close = []
for data in ohlcvs:
    close.append(data[1])

trans = ARMA(close, (2,0,0)).fit()

print(trans)
