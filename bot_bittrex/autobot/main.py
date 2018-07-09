import sys
import Bot as _BOT
import db as _DATABASE
import time
import Exchange as _EXCHANGE

def main():
	#Bittrex = _BITTREX.Bittrex() # Instace of class Bittrex
	params = {
			'id': 21,
			'user_id': 21,
			'exchange': 'bittrex',
			'strategy': 0,
			'pid': 0,
			'status': 0,
		}
	Bot = _BOT.Bot(params) # Instace of class Bot
	#balance = _EXCHANGE.Exchange({'exchange':'binance'}).balance()
	#User = Bittrex.user # Instace of class Bot
	while(True):
		Bot.buy_routine()
		Bot.sell_routine()
		time.sleep(30)

	

main()