Name

MACD Top Escape Strategy

Author

program

Strategy Description

**Introduction:** Sell and hold the currency when MACD volume and price divergence.
**Principle Implementation:** Starting from the current macd value, traverse forward to find the closing price of the k-line corresponding to the index greater than the current macd value, lock the corresponding k-line price to the maximum value within the current closing k-line range, and trigger selling if the current price is greater than the highest price in the area.
Traverse macd data forward. When the maximum retention length is greater than 15, select the nearest macd maximum value.
![IMG](https://www.fmz.com/upload/asset/245a08277f17f12091cf4.png)
**Backtest Data:**
![IMG](https://www.fmz.com/upload/asset/245180e358693ba791ce0.png)

**Note:** The strategy only supports spot trading and can be run in multiple currencies at the same time. The source code is for reference only. Please operate with caution during real-time operations.

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|num|0.1|Sale quantity|


> Source Code (Python)

```python
'''backtest
start: 2023-01-01 00:00:00
end: 2023-05-12 00:00:00
Period: 1d
basePeriod: 1h
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD","stocks":10}]
'''


# from matplotlib import pyplot as plt
# plt.figure()

class ExitTop(object):
    def __init__(self, index):
        self.index = index
        self.totestlist = []  # MACD data
        self.klist = []  # k line data
        self.toplus = []
        self.tocpn = []
        self.Sell = False

    # Get K-line and MACD data
    def GetRecord(self) -> bool:
        self.totestlist = []
        self.klist = []
        self.toplus = []
        self.tocpn = []
        records = exchanges[self.index].GetRecords()
        macd = TA.MACD(records, 12, 26, 9)
        # Determine whether DIF is greater than DEA
        if not macd[0][-2] > macd[1][-2] and macd[0][-3] < macd[1][-3] or not macd[0][-2] > macd[1][-2] and macd[0][-4] < macd[1][-4]:
            return False
        self.totestlist = macd[0][len(macd[0])-80:]
        # Encapsulate k-line data
        for get in range(len(records)):
            self.klist.append(records[get]["Close"])
        self.klist = self.klist[len(self.klist)-80:]
        return True

    def mepath(self):
        if not self.GetRecord():
            return False
        # Traverse forward to find the maximum value
        maxsign = -1000000000000
        for i in range(len(self.totestlist)-1, -1, -1):
            if self.totestlist[i] > maxsign:
                maxsign = self.totestlist[i]
                self.tocpn.append([1, i])
            else:
                if len(self.tocpn) > 0:
                    self.tocpn[-1][0] = self.tocpn[-1][0]+1
        self.toplus.insert(0, maxsign)
        sign = False
        shorttime = [0, 0]  # step size, index
        for i in range(len(self.tocpn)):
            if self.tocpn[i][0] > 15 and sign == False:
                shorttime = [self.tocpn[i][0], self.tocpn[i][1]]
                sign = True
        # If the maximum index is not yourself
        if shorttime[1] < len(self.klist)-4:
            # Lock the highest price in the area
            are = max(self.klist[shorttime[1]:-4])
            # Determine whether there is a value greater than the current macd, if the current price is greater than the highest price in the area
            if self.totestlist[-2]+300 < self.totestlist[shorttime[1]] and self.klist[-2] >= are:
                return True
        return False

    def main(self):
        result = self.mepath()
        if result == True and self.Sell == False:
            exchanges[self.index].Sell(-1, num)
            self.Sell = True
        elif result == False:
            if self.Sell == True:
                self.Sell = False
        # plt.plot(self.totestlist)
        # plt.plot(self.toplus)
        # LogStatus(plt)


def main():
    transaction = []
    for index in range(len(exchanges)):
        transaction.append(ExitTop(index))
    while True:
        for tran in range(len(transaction)):
            transaction[tran].main()
        Sleep(1000*60)
```

> Detail

https://www.fmz.com/strategy/356399

> Last Modified

2023-05-13 21:21:01