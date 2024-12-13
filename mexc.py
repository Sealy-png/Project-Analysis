import time
import hmac
import hashlib
import requests

# Replace these with your actual API credentials
api_key = 'mx0vglIoQqFLx6wZet'
api_secret = '6d73718cedc3423e9fb1217204b5d38e'

# Prepare the parameters for the request
base_url = 'https://contract.mexc.com/v1/private/order/list/history_orders'
params = {
    'api_key': api_key,
    'recv_window': 5000,
    'timestamp': str(int(time.time() * 1000))  # current timestamp in milliseconds
}

# Create a signature
query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
params['sign'] = signature

# Make the HTTP GET request
response = requests.get(base_url, params=params)

# Check the response
if response.status_code == 200:
    print("Order History:", response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
