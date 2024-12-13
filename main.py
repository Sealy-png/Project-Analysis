import numbers
from enum import Enum

import matplotlib.pyplot as plt


# TESTLINE JAKOB GIT


class Currencies(Enum):
    BTC = "BTC"
    ETH = "ETH"
    USDT = "USDT"
    BNB = "BNB"
    SOL = "SOL"


class Reasons(Enum):
    PNL = "PNL"
    PCE = "PCE"
    CPI = "CPI"
    FOMC = "FOMC"


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

    # zukünftige funktion: was war der höchste kurs zwischen entry und exit? tracken über alle bzw. viele trades
    # dafür nötig:
    # funktion getpeak (class Trade) : kurs zwischen timestamp entry und timestamp exit pullen und höchsten punkt berechnen und verhältniss zu entry point
    # getaveragepeak (class User) : alle getpeaks durch anzahl verglichener trades teilen

    # funktion: wie gut sind die trades zu jeder uhrzeit? (zu jeder session)
    # funktion: winrate
    # funktion: average holding time


class User:
    rPNL = 0
    rPCE = 0
    rCPI = 0
    rFOMC = 0

    byprofit = []

    aPNL = 0
    aPCE = 0
    aCPI = 0
    aFOMC = 0

    bytrades = []

    bars = ["PNL", "PCE", "CPI", "FOMC"]

    def __init__(self, trades: Trade):
        self.trades = trades
        self.getreadskillbyprofit()
        self.getreadskillbytrades()

    def new_trade(self, trade):
        if isinstance(trade, Trade):
            self.trades.append(trade)
        else:
            raise TypeError("not a valid trade")

    def getreadskillbyprofit(self):
        for trade in self.trades:
            for reason in trade.reasons:
                if reason == Reasons.PNL:
                    self.rPNL += trade.getprofit()
                    print(self.rPNL)
                elif reason == Reasons.CPI:
                    self.rCPI += trade.getprofit()
                elif reason == Reasons.PCE:
                    self.rPCE += trade.getprofit()
                elif reason == Reasons.FOMC:
                    self.rFOMC += trade.getprofit()

        self.byprofit = [self.rPNL, self.rPCE, self.rCPI, self.rFOMC]

    def getNetPNL(self):
        net = 0
        for trade in self.trades:
            net += trade.getprofit()
        return net

    def getreadskillbytrades(self):
        for trade in self.trades:
            for reason in trade.reasons:
                if reason == Reasons.PNL:
                    self.aPNL += 1  # if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.CPI:
                    self.aCPI += 1  # if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.PCE:
                    self.aPCE += 1  # if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.FOMC:
                    self.aFOMC += 1  # if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0

        self.bytrades = [self.aPNL, self.aPCE, self.aCPI, self.aFOMC]

    def displaybytrades(self):
        plt.bar(self.bars, self.bytrades, align='center', width=0.5, color='b', label='data')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Bar chart')
        plt.legend()
        plt.show()

    def displaybyprofit(self):
        plt.bar(self.bars, self.byprofit, align='center', width=0.5, color='b', label='data')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Bar chart')
        plt.legend()
        plt.show()

    def best_reason(self, trades):
        best = max(self.rPNL, self.aPCE, self.aFOMC, self.aCPI)
        return best


def main():
    # rs1 - rs4 sind leere Listen für Gründe
    rs1 = []
    rs2 = []
    rs3 = []
    rs4 = []
    reason1 = Reasons.PNL
    reason2 = Reasons.FOMC
    reason3 = Reasons.PCE
    reason4 = Reasons.CPI
    # -----------------------------------------------------------------
    # rsX.append = grund and liste rsX annhängen
    rs1.append(reason1)
    rs1.append(reason3)

    rs2.append(reason2)

    rs3.append(reason4)
    rs3.append(reason3)

    rs4.append(reason4)
    # ----------------------------------------------------------
    c1 = Currencies("BTC")
    c2 = Currencies("ETH")

    # trade1 ist BTC trade mit grund PNL, profit von 5
    trade1 = Trade(c1, 15, 25, rs1)
    # trade 2 ist BTC trade mit grund FOMC, profit von 3
    trade2 = Trade(c1, 22, 25, rs2)
    # trade3 ist ETH trade mit gründen PCE und CPI, verlust von 2
    trade3 = Trade(c2, 18, 30, rs3)
    # trade4 ist ETH trade mit grund CPI, positives outcome
    trade4 = Trade(c2, 12, 20, rs4)
    trade5 = Trade(c2, 14, 22, rs2)
    trade6 = Trade(c2, 12, 15, rs1)

    # Wenn neuer Trade erstellt: trades.append(tradeX)
    trades = []
    trades.append(trade1)
    trades.append(trade2)
    trades.append(trade3)
    trades.append(trade4)
    trades.append(trade5)
    trades.append(trade6)

    testuser = User(trades)

    # Immer eins von beidem Auskommentieren mit # vor der Zeile und dann anderes # löschenn

    # displaybytrades zeigt an wie viele Trades mit welchem Grund gemacht wurden
    # testuser.displaybytrades()

    # displaybyproifit zeit den NET Profit/Verlust von allen Trades mit einem Grund an
    testuser.displaybyprofit()

    for trade in testuser.trades:
        trade.getinfo()


if __name__ == '__main__':
    main()

# Press the green button in the gutter to run the script.

# hihihi
# huhuhu
# hohoho
# hahaha
# hehehee


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
