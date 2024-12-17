import Enums as en
import User as user
import mexc_api as mexc
import numbers
import json

Reasons = en.Reasons
Currencies = en.Currencies





class Trade:
    ispositive = False

    # Positionsgröße (z.B. bei preis 15 investment von 200€)
    # buy price, sell price, stop loss, currency, take profit, margin, leverage
    # bei trade ohne stop-loss --> stop-loss == liquidation
    # bei trade ohne take profit --> take-profit == realer profit
    def __init__(self, currency, buy_price, sell_price, reasons: Reasons):
        if not isinstance(currency, Currencies):
            raise TypeError("currency must be BTC/ETH/USDT/BNB/SOL")

        if not isinstance(buy_price, numbers.Number):
            raise TypeError("Buy price must be a number")

        if not isinstance(sell_price, numbers.Number):
            raise TypeError("Selling price must be a number")

        self.currency = currency
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.reasons = reasons
        self.ispositive = True if (buy_price < sell_price) else False

    def getprofit(self):
        difference = self.sell_price - self.buy_price
        return difference

    def getinfo(self):
        print("Currency: " + str(self.currency.value) + ", Reasons: " + str(
            list(reason.value for reason in self.reasons)) + ",  buy price: " + str(
            self.buy_price) + ", sell price: " + str(self.sell_price) + ", Profit/Loss: " + str(self.getprofit()))
