> Name

TD Demark Sequence

> Author

btccccrazy

> Description

The strategy is based on the TD Demark sequence, which is used to identify potential turning points in the market. When the sequence reaches certain levels (such as +9, +13, +22 or -9, -13, -22), it suggests overbought or oversold conditions respectively, and trades are executed accordingly.

> Source (Python)

```python
'''backtest
start: 2021-01-01 00:00:00
end: 2021-03-12 00:00:00
Period: 15m
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD"}]
'''

import time
import pandas as pd
import numpy as np

def main():
exchange.SetContractType("quarter")
while True:
#start_time = time.time()
records = exchange.GetRecords(PERIOD_H1)
if len(records) < 100:
Sleep(1000)
return
kline = pd.DataFrame(records)
kline.columns = ['time','open','high','low','close','volume','OpenInterest']
i = 0
j = 0
for x in range(len(kline)-40,len(kline)):
if kline['close'].values[x] > kline['close'].values[x-4]:
i += 1
else:
i = 0
if kline['close'].values[x] < kline['close'].values[x-4]:
j -= 1
else:
j = 0
TDindex = i if i>0 else j
#if 13 > TDindex >= 8 :
#Log('Warm warning, entering the overbought area, you may consider selling to take profit:')
#elif 21 > TDindex >= 13 :
#Log('General warning, entering super overbought area, consider selling to take profit:')
#elif TDindex >= 21 :
#Log('Serious warning, entering super super overbought area, consider clearing positions and taking profits:')
#elif -13 < TDindex <= -8 :
#Log('Warm warning, entering the oversold area, you may consider buying for a rebound:')
#elif -21 < TDindex <= -13 :
#Log('General warning, entering the super oversold area, you may consider adding to your position:')
#elif TDindex <= -21 :
#Log('Serious warning, entering the super super oversold area, you may consider entering the full position:')
position = exchange.GetPosition()
#if len(position) > 0:
#Log(position[0]["Type"])
if TDindex == 9 or TDindex == 13 or TDindex == 22: #and len(position) == 0 :
Log('The TD sequence of the last K line is:',TDindex)
exchange.SetDirection("sell")
id2 = exchange.Sell(-1, 1)

if TDindex == -9 or TDindex == -13 or TDindex == -22: #and len(position) == 0 :
Log('The TD sequence of the last K line is:',TDindex)
exchange.SetDirection("buy")
id2 = exchange.Buy(-1, 1)
if len(position) > 0:
if position[0]["Type"] ==0 and TDindex >= 2 :
#Log(position[0]["Type"])
Log('The TD sequence of the last K line is:',TDindex)
exchange.SetDirection("closebuy")
id2 = exchange.Sell(-1, 1)

if position[0]["Type"] ==1 and TDindex <= -2 :
#Log(position[0]["Type"])
Log('The TD sequence of the last K line is:',TDindex)
exchange.SetDirection("closesell")
id2 = exchange.Buy(-1, 1)
# end_time = time.time()
#spend_time = end_time - start_time
Sleep(1000*900)
```

> Detail

https://www.fmz.com/strategy/262467

> Last Modified

2021-03-16 11:18:47