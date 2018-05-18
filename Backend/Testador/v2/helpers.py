# coding=utf-8
import datetime as datetime
import numpy as np
import pytz
import sys
import binance_
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
        return ct.strftime("%Y-%m-%d %H:%M:%S")

    # convert timestamp to date
    def tstampToData(self, timestamp):
        """convert timestamp to data

        Arguments:
            timestamp {[timestamp]}
        """
        data = datetime.datetime.fromtimestamp(
            int(timestamp)/1000.0
        ).strftime("%Y-%m-%d %H:%M:%S")
        print(data)
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

    def saveDatabase(self, lopen, lhigh, llow, lclose, lvol, closetime):
        os.remove("test2.csv")
        thefile = open('test2.csv', 'w')
        thefile.write("Data; Volume; Open;High;Low;close \n")
        for item in range(0, len(lopen)):
            thefile.write(
                str(closetime[item]) + '; ' + str(lvol[item]) + '; ' + str(lopen[item]) + '; ' 
                + str(lhigh[item]) + '; ' + str(llow[item]) + '; ' + str(lclose[item]) + '\n')


        