"""from mexc_sdk import Spot

# Initialize the Spot client with your API credentials
spot = Spot(api_key='mx0vglIoQqFLx6wZet', api_secret='6d73718cedc3423e9fb1217204b5d38e')

# Define parameters (optional)
params = {
   #'symbol': 'MSHEESHAUSDT'  # Uncomment to specify a symbol, leave empty for all symbols
}
#response = spot.exchange_info()
# Fetch all orders
response = spot.all_orders(**params)  # Execute the method by adding ()
print(response)  #ffrint the actual data

"""
"""
{'symbol': 'MSHEESHAUSDT', 'status': '1', 'baseAsset': 'MSHEESHA', 'baseAssetPrecision': 2, 'quoteAsset': 'USDT',
 'quotePrecision': 7, 'quoteAssetPrecision': 7, 'baseCommissionPrecision': 2, 'quoteCommissionPrecision': 7,
 'orderTypes': ['LIMIT', 'MARKET', 'LIMIT_MAKER'], 'isSpotTradingAllowed': True, 'isMarginTradingAllowed': False,
 'quoteAmountPrecision': '1.000000000000000000000000000000', 'baseSizePrecision': '0', 'permissions': ['SPOT'],
 'filters': [], 'maxQuoteAmount': '2000000.000000000000000000000000000000', 'makerCommission': '0.0005',
 'takerCommission': '0.0005', 'quoteAmountPrecisionMarket': '1.000000000000000000000000000000',
 'maxQuoteAmountMarket': '100000.000000000000000000000000000000', 'fullName': 'Sheesha Finance', 'tradeSideType': 1},

"""

import time
from mexc_sdk import Spot
# from mexc_sdk import Future
import requests

# Initialize the Spot client with your API credentials
spot = Spot(api_key='mx0vglIoQqFLx6wZet', api_secret='6d73718cedc3423e9fb1217204b5d38e')
exchange_info = spot.exchange_info()
print(exchange_info)

"""
# Function to enforce rate limiting
def handle_rate_limit():

   Handles the rate limiting logic to avoid hitting the API's rate limits.
   It checks the time elapsed between requests and waits if the rate limit is near.

   # Time interval (in seconds) to wait between requests to avoid exceeding the rate limit
   time_between_requests = 0.021  # For example, make a request every 0.2 seconds to be safe (500 requests per 10 seconds)

   # Wait if necessary to avoid violating the rate limit
   time.sleep(time_between_requests)


try:
   # Fetch all available symbols
   exchange_info = spot.exchange_info()
   symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]

   # Initialize a dictionary to store orders by symbol
   all_orders = {}
   i=0
   # Fetch orders for each symbol
   for symbol in symbols:
      # Check rate limit before making the request
      handle_rate_limit()
      i+=1
      if i%100 == 0:
         print(i)
      # Call API for each symbol and catch rate limit violations
      try:
         orders = spot.all_orders(symbol=symbol)  # Fetch orders for the current symbol
         if not orders:
            continue
         all_orders[symbol] = orders  # Store results
      except requests.exceptions.RequestException as e:
         print(f"API request failed for {symbol}: {e}")
      except Exception as e:
         print(f"Unexpected error occurred for {symbol}: {e}")

      # Optional: Print each symbol's orders
      #print(f"Orders for {symbol}: {orders}")
   if not orders:
      print("No orders found")
   else:
   # Print or process the combined results
      print("All orders fetched:", all_orders)

except Exception as e:
   print(f"Error: {e}")




"""
