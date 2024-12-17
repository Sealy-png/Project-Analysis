import mexc_api as mexc
import User as user

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




def main():

    testuser = user.User("mx0vglIoQqFLx6wZet","6d73718cedc3423e9fb1217204b5d38e")
    trades = extract_trades(mexc.get_history_orders(testuser.api_key, testuser.api_secret))
    print(json.dumps(trades, indent = 2))


if __name__ == '__main__':
    main()

# Press the green button in the gutter to run the script.

# hihihi
# huhuhu
# hohoho
# hahaha
# hehehee


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
