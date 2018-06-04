from datetime import datetime
import backtrader as bt
import strategy as stt

def main():
	cerebro = bt.Cerebro()
	cerebro.addstrategy(stt.Strategy)
	cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
	cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
	cerebro.addanalyzer(bt.analyzers.SQN, _name='sqn')

	# **NOTE**: Read the note about the Yahoo API above. This sample is kept for
	# historical reasons. Use any other data feed.

	data = bt.feeds.YahooFinanceCSVData(dataname='data.csv')
	cerebro.adddata(data)
	# Set our desired cash start
	cerebro.broker.setcash(1000.0)
	# Set the commission
	cerebro.broker.setcommission(commission=0.0)

	res = cerebro.run()
	#print('params: ', res[0].params.n, res[0].params.m)
	print('trades: ', res[0].analyzers.sqn.get_analysis())
	#print('drawdown: ', res[0].analyzers.drawdown.get_analysis())
	cerebro.plot()
	#res.plot()

main()