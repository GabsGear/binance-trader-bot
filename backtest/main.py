from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import datetime
import backtrader as bt
import contraturtle as stt
import backtrader.feeds as btfeed
import sys
import data as b


def main():
	cerebro = bt.Cerebro()
	cerebro.addstrategy(stt.Strategy)
	cerebro.addsizer(stt.Quantity)
	#cerebro.addsizer(bt.sizers.SizerFix, stake=20000)
    # add analyzers
	cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="mySharpe", riskfreerate=0.001)
	cerebro.addanalyzer(bt.analyzers.DrawDown, _name="myDrawDown")
	cerebro.addanalyzer(bt.analyzers.SQN, _name="SQN")

	datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles''')

	data = dataFeed(dataname=datapath+"\\"+str(sys.argv[1])+"-"+str(sys.argv[2])+".csv", timeframe=bt.TimeFrame.Minutes, compression=60)

	cerebro.adddata(data)
	#data = cerebro.resampledata(data, timeframe=bt.TimeFrame.Minutes, compression=1440)
	# Set our desired cash start
	cerebro.broker.setcash(1.0)
	# Set the commission
	cerebro.broker.setcommission(commission=0.002)
	# Print out the starting conditions
	#print('Starting Portfolio Value: %.8f' % cerebro.broker.getvalue())
	backtest = cerebro.run()
	# Print out the final result
	#print('Final Portfolio Value: %.8f' % cerebro.broker.getvalue())
	perc = cerebro.broker.getvalue()*100-100
	#cerebro.plot(style='candlestick', barup='green', bardown='red')
	'''msg  = "PAR/TIMEFRAME/PARAM:NO-BTC:"+str(sys.argv[1])+"/"+str(sys.argv[2])
	b.write(msg)
	msg  = "Patrimonio inicial: 1 BTC"
	b.write(msg)
	msg = "Patrimonio final:"+ str(cerebro.broker.getvalue())
	b.write(msg)
	msg = "Lucro (%):"+str(perc)
	b.write(msg)
	msg = "Quantia de trades:"+str(backtest[0].analyzers.SQN.get_analysis().trades)
	b.write(msg)
	b.write("----------------------------")'''



class dataFeed(btfeed.GenericCSVData):
    params = (
        #('dtformat', '%Y-%m-%dT%H:%M:%S'),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1)
    )

main()