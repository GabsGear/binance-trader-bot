# coding=utf-8
# pylint: disable=W0612
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
    # base de dados da simulacao
    lopen, lhigh, llow, lclose, lvol, closetime = cd.getCandles(
        str(bot_config['currency']), bot_config['period'])
    pos = 20
    st = strategies.Desicion(lopen, lhigh, llow, lclose, lvol, closetime)
    saveDatabase(lopen, lhigh, llow, lclose, lvol, closetime)
    data_decision = st.getDataDecision(bot_config, pos)

    while(pos != (len(lopen) -1)):
        routine(bot_id, data_decision, pos)
        pos += 1
        time.sleep(1/10)
    print('Analise completa')


def saveDatabase(lopen, lhigh, llow, lclose, lvol, closetime):
    thefile = open('test.txt', 'w')
    thefile.write("Data; Volume; Open,High;Low;close \n")
    for item in range(0, len(lopen)):
        thefile.write(
            str(closetime[item]) + '; ' + str(lvol[item]) + '; ' + str(lopen[item]) + '; ' 
            + str(lhigh[item]) + '; ' + str(llow[item]) + '; ' + str(lclose[item]) + '\n')

def routine(bot_id, data_decision, pos):
    db = botconfig.Db()
    routine = routines.Routines()
    bot_config = db.getConfigBot(bot_id)
    routine.startBuyRoutine(bot_config, data_decision, pos)
    routine.startSellRoutine(bot_config, data_decision, pos)

main()
