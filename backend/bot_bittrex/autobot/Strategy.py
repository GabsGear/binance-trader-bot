import Bittrex as _BITTREX

class Strategy():
	def __init__(self, bot_id, pair):
		Bittrex = _BITTREX.Bittrex(bot_id)
		O, H, C, L = Bittrex.getCandleList(pair) # Size fixed in 100
		self.pair  = pair
		self.timeframe = Bittrex.bot.timeframe
		self.open  = O
		self.high  = H
		self.close = C
		self.low   = L
		#self.price = Bittrex.getTicker(pair)


	def contra_turtle(self):
		last_l = self.low[99]
		tomin = self.low[100-20::] # Slice the last 20 stocks

		print("[+] PAIR: %s"% (self.pair))
		print("[+] TIMEFRAME: %s"% (self.timeframe))
		print("[+] LAST LOW: %.8f"% (last_l))
		print("[+] SUPORTE: %.8f"% (min(tomin)))
		
		if(last_l <= min(tomin)):
			return 'buy'
		else:
			return 'none'
