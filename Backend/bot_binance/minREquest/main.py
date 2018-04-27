# coding=utf-8
import binance_
import strategies
import helpers
import botconfig
import sys
import routines
import time
from binance.client import Client 

def main():

    db = botconfig.Db()
    bot_id = sys.argv[1]
    global bot_config
    bot_config = db.getConfigBot(bot_id)
    db.setPID(bot_id)
    while(bot_config['active'] == 1):
        routine(bot_id)
        time.sleep(10)

def routine(bot_id):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    print('--Rotina de compra bot ' + str(bot_id))
    routine.startBuyRoutine(bot_config)
    print('--Rotina de venda bot ' + str(bot_id))
    routine.startSellRoutine(bot_config)

main()
