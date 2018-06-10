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

    while(bot_config['active'] != 2):
        bn = binance_.Binance_opr()
        lopen, lhigh, llow, lclose, lvol, closetime = bn.getCandles(str(bot_config['currency']), bot_config['period'])
        st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
        data_decision = st.getDataDecision(bot_config)
        routine(bot_id, data_decision)
        time.sleep(1)

def routine(bot_id, data_decision):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    print('--Rotina de compra bot ' + str(bot_id))
    routine.startBuyRoutine(bot_config, data_decision)
    print('--Rotina de venda bot ' + str(bot_id))
    routine.startSellRoutine(bot_config, data_decision)

main()
