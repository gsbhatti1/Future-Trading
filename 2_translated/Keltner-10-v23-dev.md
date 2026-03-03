```markdown
---
Name: Keltner Channel Breakout Stop Loss and Profit Target 10% Long-Term Holding Strategy - v23-dev-Multi-period

Author: nanpian

Strategy Description:
A bullish strategy for purchasing BTC spot. Initially, it uses 1000 USDT in cash.
Every hour, it checks if the price breaks the Keltner channel; if so, a long position is taken.
Exit Strategy:
1. If there's a loss of 6%, the stop-loss is triggered;
2. If the price falls below the MA moving average, exit immediately;
3. If there’s a profit of 10%, use it as a protective cushion and enter another long position. If prices fall by more than 10% over the past 24 hours after making this move, consider it an event and stop out.

I have been testing this strategy in real trading and found the backtest results to be quite promising.
Essentially, it's about minimizing losses while maximizing gains.

---

Source (Python)

```python
'''
start: 2020-01-01 00:00:00
end: 2020-04-24 00:00:00
period: 1h
exchanges: [{"eid":"huobi","currency":"BTC_USDT","stocks":0,"meta":{"AccessKey":"7yngd7gh5g-a7ed9b1a-c05064c3-bab33","SecretKey":"553c2cd1-e229e1d2-25a536cb-db7d3"}}]
'''

import talib as ta
import pandas as pd
from datetime import datetime
from datetime import timedelta
import math
# coding:utf8
import sys

eid = -1
last_price = -1

def main():
    global eid
    global last_price
    global ma

    while True:

        records = exchange.GetRecords(1*60*60)
        e = exchange
        kline1 = pd.DataFrame(records)
        kline1['Time'] = kline1['Time'].map(lambda x: datetime.utcfromtimestamp(x/1000)+timedelta(hours=8))
        kline1.columns = ['time','open','high','low','close','volume','oi']
       
        r = kline1
        # Log('最新k线时间',r.iloc[-1].time, ' 最新价格收盘价', r.iloc[-1].close)
    
        leadLine1 = ta.EMA(r.close, 30)
        leadLine2 = ta.SMA(r.close, 30)
        UT=leadLine2 < leadLine1
        DT=leadLine2 > leadLine1
    
        # Keltner Channel
        ma  = ta.EMA(kline1.close, 80)
        # True range function
        range1 = ta.TRANGE(kline1.high, kline1.low, kline1.close)
        rangema = ta.EMA(range1, 80)
        upper = ma + 3*rangema
        lower = ma - 3*rangema
       
        # ADX/DMI minus and plus
        minus = ta.MINUS_DI(kline1.high,kline1.low, kline1.close,14) 
        plus = ta.PLUS_DI(kline1.high, kline1.low, kline1.close ,14)
                   
        volume0 = r.iloc[-1].volume
        volume1 = r.iloc[-2].volume
        rn = r.iloc[-1]
       
        entry_long = rn.close > upper.iloc[-1] and (r.iloc[-1].volume+ r.iloc[-2].volume) > 1.5 * (r.iloc[-4].volume+ r.iloc[-5].volume)
        long = entry_long
        exit_long = (rn.close < ma.iloc[-1] )
        account = exchange.GetAccount()
        amount = account.Stocks
        # Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
        # If in an empty position state
        if (account['Balance'] >= 600 and amount < 0.001):
            if long==True and account['Balance'] < 400 and amount<0.01:
                Log('balance is ', account['Balance'], ' Insufficient balance of 400, exiting!')
                return
            elif long== True  and account['Balance'] >= 600: # First long position opening
                Log('balance is ', account['Balance'])
                Log('Long position time: ', rn.time, ' open is ', rn.open , ' close is ', rn.close, ' upper is ', upper.iloc[-1], ' volume 0/1 is', volume0 , 'volume 1 is ', 
                ' plus is ',plus.iloc[-1], ' minus is ', minus.iloc[-1], '@')
                exchange.Buy(-1,600)
                last_price = rn.close + 10
                Sleep(1000*60*15)
        # If in a holding state
        if amount > 0.001 :
            if amount > 0.0001 and rn.close <= last_price * 0.94: 
                Log('Stop loss liquidation event: ','balance is ', account['Balance'], ' time: ', rn.time, ' close price: ', rn.close, ' @')
                id = exchange.Sell(-1, amount);
                account = exchange.GetAccount()
                amount = account.Stocks
                Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
                eid = -1
            # If in a long holding state with a major drop, then sell
            elif amount > 0.0001 and rn.close >= last_price * 1.1 and rn.close <= r.iloc[-24].close*0.9:
                Log('Major drop stop loss liquidation event within the holding period: ', 'time: ', rn.time, ' close price: ', rn.close, ' @')
                id = exchange.Sell(-1, amount);
                eid = -1
                account = exchange.GetAccount()
                amount = account.Stocks
                Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
            elif amount > 0.0001 and exit_long == True :
                if rn.close <= last_price:
                    Log('Position reduction liquidation event, loss: amount is ',amount ,' time is ', rn.time, ' price: ',rn.close,' ma is ', ma.iloc[-1], ' open price',last_price,' Loss ratio: ',100*(last_price -rn.close)/last_price ,'% @')
                    eid = exchange.Sell(-1, amount)
#                print(r.tail(10))
#                print('ma is ' ,ma)
                    account = exchange.GetAccount()
                    amount = account.Stocks
                    Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
                elif rn.close > last_price*1.1 :
                    Log('Profit exceeds 10%, continue holding')
                    account = exchange.GetAccount()
                    amount = account.Stocks
                    Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
                    return 
                elif rn.close > last_price  and rn.close <=last_price*1.1:
                    eid = exchange.Sell(-1, amount);
                    account = exchange.GetAccount()
                    amount = account.Stocks
                    Log('Position reduction liquidation event, profit: amount is ',amount, ' time is ', rn.time, ' price: ',rn.close,' ma is ', ma.iloc[-1],' open price',last_price,' Profit ratio: ',100*(rn.close-last_price )/last_price ,'% @' )
                else:
                    id = exchange.Sell(-1, amount);
                    Log('Final position reduction liquidation event, profit: amount is ',amount, ' time is ', rn.time, ' price: ',rn.close,' ma is ', ma.iloc[-1],' open price',last_price,' Profit ratio: ',100*(rn.close-last_price )/last_price ,'% @' )
                    eid = -1
                    account = exchange.GetAccount()
                    amount = account.Stocks
                    Log('Balance is ', account['Balance'], ' Btc amount is ', amount)
            Sleep(1000*60*15)

```

---

Detail: https://www.fmz.com/strategy/313041

Last Modified: 2021-09
```