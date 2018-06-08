from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
import backtrader as bt
import rsi as stt

def execBT():
	cerebro = bt.Cerebro()
	cerebro.addstrategy(stt.Strategy)
	cerebro.addsizer(bt.sizers.SizerFix, stake=40)

	cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="mySharpe", riskfreerate=0.001)
	cerebro.addanalyzer(bt.analyzers.DrawDown, _name="myDrawDown")
	cerebro.addanalyzer(bt.analyzers.SQN, _name="SQN")

	datapath=('/home/gabs/Backend/Backend/Testador/Baktrader/databases/LTCBTC-hour-Jul, 2017-May, 2018.csv')

	data = bt.feeds.YahooFinanceCSVData(
	dataname=datapath,
	fromdate=datetime.datetime(2017, 7, 18),
	todate=datetime.datetime(2018, 5, 17),
	decimals=8,
	adjclose=True,
	buffered= True,
	reverse=False)
	data = cerebro.adddata(data)
	cerebro.broker.setcash(1.0)
	cerebro.broker.setcommission(commission=0.002)
	print('Starting Portfolio Value: %.8f' % cerebro.broker.getvalue())
	
	backtest = cerebro.run()

	print('Final Portfolio Value: %.8f' % cerebro.broker.getvalue())
	perc = cerebro.broker.getvalue()*100-100
	print("Porcentagem de lucro: %.2f"% perc)
	print('SQN Ratio :', backtest[0].analyzers.SQN.get_analysis().sqn)
	print('QNT Trades :', backtest[0].analyzers.SQN.get_analysis().trades)
	cerebro.plot(style='candlestick', barup='green', bardown='red')