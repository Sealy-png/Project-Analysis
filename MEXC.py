import requests
from mexc_sdk import Client

# Example: Initialize the client
client = Client(api_key="your_api_key", api_secret="your_api_secret")

# Example: Fetch market data
response = client.market.get_symbol_info("BTC_USDT")
print(response)
