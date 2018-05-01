
from binance.enums import *
from binance.websockets import BinanceSocketManager
from binance.client import Client

client = Client("","")
bm = BinanceSocketManager(client)

#CALLBACK
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

def process_m_message(msg):
    print("stream: {} data: {}".format(msg['stream'], msg['data']))
# pass a list of stream names

conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_30MINUTE)
bm.start()