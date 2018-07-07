import Bittrex as _BITTREX
#import Strategy as _STRATEGY
import sys
import Bot as _BOT
import db as _DATABASE
import time

def main():
	#Bittrex = _BITTREX.Bittrex() # Instace of class Bittrex
	Bot = _BOT.Bot(id =21, user_id=21, pid =None, status=0) # Instace of class Bot
	#User = Bittrex.user # Instace of class Bot
	while(True):
		Bot.buy_routine()
		Bot.sell_routine()
		time.sleep(30)

	

main()