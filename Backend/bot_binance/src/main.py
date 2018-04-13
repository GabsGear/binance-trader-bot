# coding=utf-8
import binance_
import strategies
import helpers
import botconfig
import sys
import routines
import time

def main():

    db = botconfig.Db()
    bot_id = sys.argv[1]
    global bot_config
    bot_config = db.getConfigBot(bot_id)
    print ("Started")
    db.setPID(bot_id)
    while(True):
        routine(bot_id)
        time.sleep(10)

def routine(bot_id):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    routine.startBuyRoutine(bot_config)
    routine.startSellRoutine(bot_config)


main()
