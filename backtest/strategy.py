import backtrader as bt

class Strategy(bt.Strategy):

    def __init__(self):
        super(Strategy, self).__init__()
        self.order = None
        self.rsi = bt.indicators.RSI(self.data.close, period=14)

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))


    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                     
    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        print(self.position)
        if self.order:
            return

        if self.rsi[0] < 50:
            #print('%s: BUY  CREATED' % dtstr)
            self.order = self.buy(exectype=bt.Order.Market)
            
        if self.rsi[0] > 62:
            #print('%s: SELL CREATED' % dtstr)
            self.order = self.sell(exectype=bt.Order.Close)
            #print("---ORDEM-VENDA----------------------------</br>")
            #print(self.order_sell)
