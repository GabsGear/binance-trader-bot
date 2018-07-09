import ccxt as _CCXT
		
class Exchange():
	def __init__(self, params=None):
		self.exchange = params['exchange']

	def price(self, pair):
		_BINANCE = _CCXT.binance()
		return _BINANCE.fetch_ticker(pair)['bid']

	def balance(self):
		TOTAL = 0
		_BINANCE = _CCXT.binance({
			'apiKey': 'oW51DLGVhwvAycmmIx1TDiryL7gBfeNgH37gx9K0FGXzlCson0ZL3WGfP2lZ4gCj',
    		'secret': 'vWPZRjZR5hLufvHgckwab8RNYRb6zd9Fws4HtxwmX5I3lUiiknOjiXDKy41lU8Po',
		})
		balance = _BINANCE.fetch_balance()['total']
		for value in balance:
			price = self.price("XRP/BTC")
			#print(value)
			#TOTAL = TOTAL * (value*price)

		print(balance)

	