# gabsghell134625apikey
# API Key:
# q4r6zw4CXMGynsdQhRgzcs1PuOBfT1uCCwBG2op0fue7Qr33XvH23Cn0W5SMgWGU
# Secret:
# 8PVopsBzr0piU66t3dEiPoxTuZUfVCemWdkjI5zN9OhEZcyPxgeO4UaAD1jM0zG0


from binance.client import Client
client = Client("", "")



# # get market depth
# depth = client.get_order_book(symbol='BNBBTC')

# # place a test market buy order, to place an actual order use the create_order function
# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=Client.SIDE_BUY,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=100)

# # get all symbol prices
# prices = client.get_all_tickers()

# # withdraw 100 ETH
# # check docs for assumptions around withdrawals
# from binance.exceptions import BinanceAPIException, BinanceWithdrawException
# try:
#     result = client.withdraw(
#         asset='ETH',
#         address='<eth_address>',
#         amount=100)
# except BinanceAPIException as e:
#     print(e)
# except BinanceWithdrawException as e:
#     print(e)
# else:
#     print("Success")

# # fetch list of withdrawals
# withdraws = client.get_withdraw_history()

# # fetch list of ETH withdrawals
# eth_withdraws = client.get_withdraw_history(asset='ETH')

# # get a deposit address for BTC
# address = client.get_deposit_address(asset='BTC')

# # start aggregated trade websocket for BNBBTC
# def process_message(msg):
#     print("message type: {}".format(msg['e']))
#     print(msg)
#     # do something

# from binance.websockets import BinanceSocketManager
# bm = BinanceSocketManager(client)
# bm.start_aggtrade_socket('BNBBTC', process_message)
# bm.start()

# # get historical kline data from any date range

# # fetch 1 minute klines for the last day up until now
# klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# # fetch 30 minute klines for the last month of 2017
#candles = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

closetime = []

candles = client.get_klines(symbol= 'ETHBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
for candles in candles:
    closetime.append(candles[6])

candles = candles[len(candles)-20:len(candles)-1]

print(closetime)

# # fetch weekly klines since it listed
# klines = client.get_historical_klines("NEOBTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")