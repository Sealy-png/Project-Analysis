


class OpenTrade:
    #für den fall, dass mehree opening trades gemacht werden, immer "openAvgPrice" nehmen für PNL rechnung
    def __int__(self, pair, direction, openType, openTime, entryPreis, leverage, stopLoss, takeProfit, ):
        self.openType = openType # Isolated oder cross order
        self.openTime = openTime # Timestamp eröffnung (in datum convertieren?)
        self.leverage = leverage # Trade Leverage
        self.stopLoss = stopLoss # Trade StopLoss im entry eingetragen, im exit leer
        self.pair = pair # Symbol in Json, z.B. USDTBTC
        self.takeProfit = takeProfit # Trade takeProfit im voraus angegeben
        self.direction = direction # Trade short/long


