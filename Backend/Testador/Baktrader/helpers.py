# coding=utf-8
import datetime as datetime
import numpy as np
import pytz
import sys
import os
import csv
import json


class Helpers:
    """Helper functions

    Returns:
        All functions to help in development (use anyway)
    """
    # Time on my timezone

    def time_now(self):
        """time now 
        Returns:
            [data] -- returns a atual data in sao paulo 
        """
        brasil = pytz.timezone('America/Sao_Paulo')
        ct = datetime.datetime.now(tz=brasil)
        return ct.strftime("%Y-%m-%d") #%H:%M:%S")

    # convert timestamp to date
    def tstampToData(self, timestamp):
        """convert timestamp to data

        Arguments:
            timestamp {[timestamp]}
        """
        data = datetime.datetime.fromtimestamp(
            int(timestamp)/1000.0
        ).strftime("%Y-%m-%d")# %H:%M:%S")
        return data

    def writeOutput(self, bot_id, data):
        try:
            file = open('/home/binance/logs'+str(bot_id)+'-output.txt', 'a+')
            file.write('['+str(self.time_now())+'] ' + data + "\n")
        except:
            return

    def progress(self, count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

    def saveDatabase(self, lopen, lhigh, llow, lclose, lvol, closetime, coin, period, start, end):
        thefile = open('databases/' + str(coin) + '-' + str(period) + '-' +
                       str(start) + '-' + str(end)+'.csv', 'w')
        thefile.write("Date,Open,High,Low,Close,Adj  Close,Volume \n")
        for item in range(0, len(lopen)):
            thefile.write(
                str(closetime[item]) + ',' + str(lopen[item]) +
                ',' + str(lhigh[item]) + ','
                + str(llow[item]) + ',' + str(lclose[item]) + ',' + str(lclose[item]) +','+ str(lvol[item]) + '\n')

    def logcsv(self,string):
        thefile = open('/home/gabs/Backend/Backend/Testador/Baktrader/logs/log.csv', 'a')
        thefile.write(str(string) + '\n')