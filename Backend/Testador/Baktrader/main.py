from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import strat as st
#import breackChannel as bc
import strat as st
import backtrader as bt
import binance_ as bn
import helpers as hp


def main():
    # cd = bn.Binance_opr()
    # h = hp.Helpers()
    # lopen, lhigh, llow, lclose, lvol, closetime = cd.getCandles(
    #     'ETHBTC', 'hour')

    # h.saveDatabase(lopen, lhigh, llow, lclose, lvol,
    #             closetime, 'ETHBTC','hour' , '1', '2')

    cerebro = bt.Cerebro()

    cerebro.addstrategy(st.TestStrategy)
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.SQN, _name='sqn')

    datapath = os.path.join(
        '/home/gabs/Backend/Backend/Testador/Baktrader/databases/LTCBTC-hour-Jul, 2017-May, 2018.csv')

    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2017, 7, 3),
        todate=datetime.datetime(2018, 5, 17),
        decimals=8,
        adjclose=True,
        reverse=False)

    cerebro.adddata(data)
    cerebro.broker.setcash(1.0)

    print('Starting Portfolio Value: %.8f' % cerebro.broker.getvalue())

    res = cerebro.run()
    print('Final Portfolio Value: %.8f' % cerebro.broker.getvalue())
    print('trades: ', res[0].analyzers.sqn.get_analysis())
    print('drawdown: ', res[0].analyzers.drawdown.get_analysis())

    cerebro.plot()


main()
