# coding=utf-8
# pylint: disable=W0612
import binance_
import strategies
import helpers
import botconfig
import sys
import routines
import time
import os 
from binance.client import Client


def main():
    cd = binance_.Binance_opr()
    db = botconfig.Db()
    bot_id = sys.argv[1]
    global bot_config
    bot_config = db.getConfigBot(bot_id)
    db.setPID(bot_id)
    obj = helpers.Helpers()
    # base de dados da simulacao
    lopen, lhigh, llow, lclose, lvol, closetime = cd.getCandles(
        str(bot_config['currency']), bot_config['period'])
    pos = 24
    st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
    obj.saveDatabase(lopen, lhigh, llow, lclose, lvol, closetime)
    data_decision = st.getDataDecision(bot_config, pos)
    size = len(lopen) - 1
    while(pos != (size)):
        obj.progress(pos, size-1, status=' Analisando estrategia || candle  ' +
                    str(pos) + ' de ' + str(size))
        bot_config = db.getConfigBot(bot_id)
        routine(bot_id, data_decision, pos)
        pos += 1
    print('Analise completa')


def routine(bot_id, data_decision, pos):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    routine.startBuyRoutine(bot_config, data_decision, pos)
    routine.startSellRoutine(bot_config, data_decision, pos)


main()
