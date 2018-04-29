import numpy as np
import matplotlib.pyplot as plt
import binance_
import pandas as pd
import matplotlib.patches as mpaches
#%matplotlib inline

def bband():
    dt = binance_.Binance_opr()
    lopen, lhigh, llow, lclose, lvol, closetime = dt.getCandles('XVGBTC', 'hour')

    interval = 20 #numero de candles
    nDesvios = 2
    size = len(lclose)

    close = lclose[size - interval: size]
    closetime = closetime[size - interval: size]
    mean = np.mean(close)
    desvio = np.std(close)

    upper = mean + (desvio * nDesvios)
    lower = mean - (desvio * nDesvios)

    print('Mean')
    print(mean)
    print('Upper')
    print(upper)
    print('Lower')
    print(lower)


    """
        Fechou fora, fechou dentro, estrategia para operar na tendencia de alta
        Voce entra quando um candle fecha fora de uma das bandas e o seguinte fecha dentro
    """


bband()