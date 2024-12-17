from enum import Enum



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
