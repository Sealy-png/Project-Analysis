# Thisbuy=Nonemple Python script.
from enum import Enum
import numbers
import matplotlib.pyplot as plt
import decimal
import numpy as np
import tkinter as tk


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    def __init__(self,currency, buy_price, sell_price, reasons : Reasons):
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
        self.ispositive = True if(buy_price < sell_price) else False

    def getprofit(self):
        difference = self.sell_price - self.buy_price
        return difference

    def getinfo(self):
        print("Currency: " + str(self.currency.value) + ", Reasons: " + str(list(reason.value for reason in self.reasons)) + ",  buy price: " + str(self.buy_price) + ", sell price: " + str(self.sell_price) + ", Profit/Loss: "+str(self.getprofit()))
        #print(list(reason.value for reason in self.reasons))
        #print(str(reason.value for reason in self.reasons))
        # " Reasons: " + str(e.value for e in self.reasons) +



    #zukünftige funktion: was war der höchste kurs zwischen entry und exit? tracken über alle bzw. viele trades
    #dafür nötig:
    #funktion getpeak (class Trade) : kurs zwischen timestamp entry und timestamp exit pullen und höchsten punkt berechnen und verhältniss zu entry point
    #getaveragepeak (class User) : alle getpeaks durch anzahl verglichener trades teilen

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

    bars = ["PNL", "PCE","CPI","FOMC"]



    def __init__(self, trades : Trade):
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

        self.byprofit = [self.rPNL, self.rPCE, self.rCPI,self.rFOMC]

    def getNetPNL(self):
        net = 0
        for trade in self.trades:
            net += trade.getprofit()
        return net


    def getreadskillbytrades(self):
        for trade in self.trades:
            for reason in trade.reasons:
                if reason == Reasons.PNL:
                    self.aPNL += 1 #if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.CPI:
                    self.aCPI += 1 #if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.PCE:
                    self.aPCE += 1 #if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0
                elif reason == Reasons.FOMC:
                    self.aFOMC += 1 #if trade.getprofit() > 0 else -1 if trade.getprofit() < 0 else 0

        self.bytrades = [self.aPNL, self.aPCE, self.aCPI,self.aFOMC]

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

    def best_reason(self,trades):
        best = max(self.rPNL, self.aPCE, self.aFOMC,self.aCPI)
        return best


def main():
    rs1 = []
    rs2 = []
    rs3 = []
    rs4 = []
    reason1 = Reasons.PNL
    rs1.append(reason1)
    reason2 = Reasons.FOMC
    rs2.append(reason2)
    reason3 = Reasons.PCE
    rs3.append(reason3)
    reason4 = Reasons.CPI
    rs3.append(reason4)
    rs4.append(reason4)
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
    trade5 = Trade(c2,14,22, rs2)
    trades = []
    trades.append(trade1)
    trades.append(trade2)
    trades.append(trade3)
    trades.append(trade4)
    trades.append(trade5)

    testuser = User(trades)

    testuser.displaybytrades()
    #testuser.displaybyprofit()


    for trade in testuser.trades:
        trade.getinfo()




    #print(testuser.rPNL)
    """
    
    window = tk.Tk()
    window.geometry("700x500")
    window.title("Trade registration")
    #
    selected = tk.StringVar()
    selected.set(Currencies.BTC.value)

    #button1 = tk.Button(top, text="hallo",)
    window.mainloop()
    """










""" rs = []
   rs.append(Reasons("PNL"))
   tds = []
   t1 = Trade("BTC", 200, 220, rs )
   tds.append(t1)
   u1 = User(tds)
    options = [
        "BTC"
        "ETH"
        "USDT"
        "BNB"
        "SOL"
    ]
   """

if __name__ == '__main__':
    main()





"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
"""
# Press the green button in the gutter to run the script.

#hihihi
#huhuhu
#hohoho
#hahaha
#hehehee





# See PyCharm help at https://www.jetbrains.com/help/pycharm/