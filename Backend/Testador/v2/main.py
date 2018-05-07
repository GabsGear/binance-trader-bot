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
    cd = binance_.Binance_opr()
    db = botconfig.Db()
    bot_id = sys.argv[1]
    global bot_config
    bot_config = db.getConfigBot(bot_id)
    db.setPID(bot_id)
    obj = helpers.Helpers()

    #base de dados da simulacao
    lopen, lhigh, llow, lclose, lvol, closetime = cd.getCandles(str(bot_config['currency']), bot_config['period'])
    pos = 20    

    while(pos != len(lopen)):
        obj.progress(pos, len(lopen)-1, status=' Analisando estrategia || Candle ' + str(pos) + ' de ' + str(len(lopen)-1))
        routine(bot_id, pos)
        time.sleep(10)
        pos += 1

def routine(bot_id, pos):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    routine.startBuyRoutine(bot_config, pos)
    routine.startSellRoutine(bot_config, pos)



main()
