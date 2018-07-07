from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import datetime
import backtrader as bt
import smothavg as stt
import backtrader.feeds as btfeed
import sys
import data as b


def main():
	cerebro = bt.Cerebro()
	cerebro.addstrategy(stt.Strategy)
	cerebro.addsizer(stt.Quantity)
	#cerebro.addsizer(bt.sizers.SizerFix, stake=1)
	
    # add analyzers
	cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="SR", riskfreerate=0.001)
	cerebro.addanalyzer(bt.analyzers.DrawDown, _name="DD")
	cerebro.addanalyzer(bt.analyzers.SQN, _name="SQN")

	datapath=(r'''C:\Users\Pichau\Documents\work\protraderbot\git\backend\backtest\candles''')

	data = dataFeed(dataname=datapath+"\\"+str(sys.argv[1])+"-"+str(sys.argv[2])+"-"+str(sys.argv[3])+".csv", timeframe=bt.TimeFrame.Minutes, compression=60)

	cerebro.adddata(data)
	#data = cerebro.resampledata(data, timeframe=bt.TimeFrame.Minutes, compression=1440)
	# Set our desired cash start
	cerebro.broker.setcash(1.0)
	# Set the commission
	cerebro.broker.setcommission(commission=0.002)
	# Print out the starting conditions
	print('Starting Portfolio Value: %.8f' % cerebro.broker.getvalue())
	init = cerebro.broker.getvalue()
	backtest = cerebro.run()
	# Print out the final result
	print('Final Portfolio Value: %.8f' % cerebro.broker.getvalue())
	perc = (cerebro.broker.getvalue()*100)-100

	msg  = "PAR/TIMEFRAME/PARAM:BTC:"+str(sys.argv[1])+"/"+str(sys.argv[2])
	print(msg)
	msg  = "Patrimonio inicial:"+str(init)
	print(msg)
	msg = "Patrimonio final:"+ str(cerebro.broker.getvalue())
	print(msg)
	msg = "Lucro (%):"+str(perc)
	print(msg)
	msg = "Quantia de trades:"+str(backtest[0].analyzers.SQN.get_analysis().trades)
	print(msg)
	msg = "SQN Ratio:"+str(backtest[0].analyzers.SQN.get_analysis())
	print(msg)
	msg = "Drowndawn:"+str(backtest[0].analyzers.DD.get_analysis())
	print(msg)
	msg = "Sharpe Ratio:"+str(backtest[0].analyzers.SR.get_analysis())
	print(msg)
	print("----------------------------")
	cerebro.plot(style='candlestick', barup='green', bardown='red')



class dataFeed(btfeed.GenericCSVData):
    params = (
        #('dtformat', '%Y-%m-%dT%H:%M:%S'),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
		('adjclose', 4),
        ('volume', 5),
        ('openinterest', -1)
    )

main()