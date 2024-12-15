import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode, quote
from collections import OrderedDict
from datetime import datetime
from mexc_sdk import *





# Replace these with your actual API credentials
api_key = 'mx0vglIoQqFLx6wZet'
api_secret = '6d73718cedc3423e9fb1217204b5d38e'


# Prepare the parameters for the request
#base_url = 'https://contract.mexc.com/api/v1/contract/ping'
base_url = 'https://contract.mexc.com/api/v1/private/order/list/history_orders'
params = {
    'api_key': api_key,
    'timestamp': str(int(time.time() * 1000)),  # current timestamp in milliseconds
    'recv_window': 20,
    'page_num': 1,
    'page_size': 5

}


stamp = time.time()*1000
sign_params = urlencode(OrderedDict(sorted(params.items())),quote_via=quote)
to_sign = f"{api_key}{stamp}{sign_params}"
sign = hmac.new(api_secret.encode('utf-8'), to_sign.encode('utf-8'),hashlib.sha256).hexdigest()
print(sign)

# Create a signature
#vorher query_string ohne auskommentierten api_key/timestamp
param_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
#signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
signature = (hmac.new(api_secret.encode('utf-8'),
            param_string.encode('utf-8'),
            hashlib.sha256)
            .hexdigest())
"""signature = (hmac.new(
    bytes(api_secret, 'latin-1'),
    msg=bytes(sig_String, 'latin-1'),
    digestmod=hashlib.sha256)
    .hexdigest().upper())"""
#params['sign'] = sign
#print(signature)

client = Spot()
client.all_orders



# Make the HTTP GET request
#response = requests.get(base_url, params=params)
r = requests.get(base_url, sign,params=params)
print(r.url)
# Check the response
if r.status_code == 200:
    print("Order History:", r.__dict__)
else:
    print(f"Error: {r.status_code}, {r.text}")