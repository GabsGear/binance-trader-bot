# coding=utf-8
import datetime as datetime
import numpy as np
import pytz
import sys
import binance_

class Helpers:
    """Helper functions
    
    Returns:
        All functions to help in development (use anyway)
    """
    #Time on my timezone  
    def time_now(self):
        """time now 
        
        Returns:
            [data] -- returns a atual data in sao paulo 
        """
        brasil = pytz.timezone('America/Sao_Paulo')
        ct = datetime.datetime.now(tz=brasil)
        return ct.strftime("%d/%m/%y-%X")
    
    #convert timestamp to date
    def tstampToData(self, timestamp):
        """convert timestamp to data
        
        Arguments:
            timestamp {[timestamp]}
        """
        return(
            datetime.datetime.fromtimestamp(
                int(timestamp)/1000.0
            ).strftime('%Y-%m-%d %H:%M:%S')
        )

