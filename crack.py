#  MarketData
from kucoin.client import Market
client = Market(url='https://api.kucoin.com')
# client = Market()



# get symbol kline
klines = client.get_kline('BTC-USDT','1min')

# get symbol ticker
server_time = client.get_server_timestamp()

api_key = '<api_key>'
api_secret = '<api_secret>'
api_passphrase = '<api_passphrase>'

# Trade
from kucoin.client import Trade
client = Trade(key='', secret='', passphrase='', url='')



# place a limit buy order
order_id = client.create_limit_order('BTC-USDT', 'buy', '1', '8000')

# place a market buy order   Use cautiously
order_id = client.create_market_order('BTC-USDT', 'buy', size='1')

# cancel limit order
client.cancel_order('5bd6e9286d99522a52e458de')

# User
from kucoin.client import User
client = User(api_key, api_secret, api_passphrase)



address = client.get_withdrawal_quota('KCS')
