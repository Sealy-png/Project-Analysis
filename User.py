import Enums as en
import matplotlib.pyplot as plt
import mexc_api as mexc
import Trades as Trade
Reasons = en.Reasons
Currencies = en.Currencies


# api_key = "mx0vglIoQqFLx6wZet", api_secret = "6d73718cedc3423e9fb1217204b5d38e"
class User:
    trades = []
    # stands for: resultREASON, meaning total amount of profit Loss for "REASON"
    rPNL = 0
    rPCE = 0
    rCPI = 0
    rFOMC = 0
    byprofit = []

    # stands for amountREASON, meaning how many trades were made for that reason in total
    aPNL = 0
    aPCE = 0
    aCPI = 0
    aFOMC = 0
    bytrades = []

    bars = ["PNL", "PCE", "CPI", "FOMC"]
    api_key = ""
    api_secret = ""

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.getreadskillbyprofit()
        self.getreadskillbytrades()

    def getTrades_mexc(self):
        test = mexc.get_history_orders(self.api_key, self.api_secret)
        self.trades = test
        return self.trades

    def new_trade(self, trade):
        if isinstance(trade, Trade.Trade):
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

    def best_reason(self):
        best = max(self.rPNL, self.aPCE, self.aFOMC, self.aCPI)
        return best
