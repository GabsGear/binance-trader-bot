import talib
import numpy



close = numpy.random.random(100)
output = talib.RSI(close)
print(output)
print('gabs')