import Bittrex as _BITTREX
import Strategy as _STRATEGY
import sys

def main():
	bot_id = sys.argv[1]
	Bittrex = _BITTREX.Bittrex(21) # Instace of class Bittrex
	Bot = Bittrex.bot # Instace of class Bot
	User = Bittrex.user # Instace of class Bot
	
	while(True):
		Bot.check_buy()

	

main()