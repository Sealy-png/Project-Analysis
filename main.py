import mexc_api as mexc
import User as user
import datetime

import json


def extract_trades(response):
    """
    Extracts trades from a JSON-like dictionary structure.

    Args:
        response (dict): The JSON response containing trade data.

    Returns:
        list: A list of trade dictionaries extracted from the response.
    """
    # Ensure the input is a dictionary and contains the 'data' key
    if not isinstance(response, dict) or 'data' not in response:
        raise ValueError("Invalid input: Response must be a dictionary with a 'data' key.")

    # Extract the list of trades
    trades = response.get('data', [])

    # Verify each trade entry is a dictionary
    if not all(isinstance(trade, dict) for trade in trades):
        raise ValueError("Invalid trade format: All trades must be dictionaries.")

    return trades


# zukünftige funktion: was war der höchste kurs zwischen entry und exit? tracken über alle bzw. viele trades
    # dafür nötig:
    # funktion getpeak (class Trade) : kurs zwischen timestamp entry und timestamp exit pullen und höchsten punkt berechnen und verhältniss zu entry point
    # getaveragepeak (class User) : alle getpeaks durch anzahl verglichener trades teilen

    # funktion: wie gut sind die trades zu jeder uhrzeit? (zu jeder session)
    # funktion: winrate
    # funktion: average holding time


#korrekter api call
#trades = mexc.get_history_orders(testuser.api_key, testuser.api_secret, start_time='1733055283000', end_time= '1735647614000', page_size='100',)['data']

def main():

    testuser = user.User("mx0vglXSkzB80u1I6J","0316cee7fe904273990ee44f6c135b50")
    trades = mexc.get_history_orders(testuser.api_key, testuser.api_secret, start_time='1733055283000', end_time= '1735647614000', page_size='100',)['data']
    testtrades = []
    liquids = mexc.get_open_positions(testuser.api_key, testuser.api_secret)['data']
    #print(str(datetime.datetime.fromtimestamp(liquids[0]['createTime'] / 1000.0, tz=datetime.timezone.utc)) + "   ||   ", liquids[0])

    for trade in trades:
        #print(str(datetime.datetime.fromtimestamp(trade['createTime'] / 1000.0, tz=datetime.timezone.utc)) + " || " + str(trade['positionId']))
        #print(trade['createTime'])
        #print(json.dumps(trade, indent=2))
        #if(trade['positionId'] == 624249170):
        testtrades.append(trade)
    n = 100
    i=0
    for trade in testtrades:
        #print(str(trade['positionId']) + "  ||  " + str(datetime.datetime.fromtimestamp(trade['createTime'] / 1000.0, tz=datetime.timezone.utc)))
        if(trade['positionId'] == 611556583 and trade['dealVol'] != 0):
            print(str(datetime.datetime.fromtimestamp(trade['createTime'] / 1000.0, tz=datetime.timezone.utc)) + " || " + str(trade))
        #i+=1
    #print(i)


if __name__ == '__main__':
    main()