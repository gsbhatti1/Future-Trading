Name

Moving average strategy python version

Author

Inventor Quantification-Little Dream

Strategy Description

Moving average strategy (python version) is teaching in nature, use it with caution in real trading.

Strategy Arguments


|Argument|Default|Description|
|--------|------|----------|
|FastPeriod|3|Market entry fast period|
|SlowPeriod|7|Slow market entry period|
|EnterPeriod|3|Market observation period|
|ExitFastPeriod|3|Exit Fast Period|
|ExitSlowPeriod|7|Exit Slow Period|
|ExitPeriod|true|Exit observation period|
|PositionRatio|0.8|Position Ratio|
|Interval|10|Polling period|


Source(python)

```python
import types
def main():
    STATE_IDLE = -1
    state = STATE_IDLE
    initAccount = ext.GetAccount()
    while True:
        if state == STATE_IDLE :
            n = ext.Cross(FastPeriod,SlowPeriod) # Indicator cross function
            if abs(n) >= EnterPeriod :
                opAmount = _N(initAccount.Stocks * PositionRatio,3)
                Dict = ext.Buy(opAmount) if n > 0 else ext.Sell(opAmount)
                if Dict:
                    opAmount = Dict['amount']
                    state = PD_LONG if n > 0 else PD_SHORT
                    Log("Opening Details",Dict,"Cross Period",n)
                else:
                    pass
        else:
            n = ext.Cross(ExitFastPeriod,ExitSlowPeriod) # Indicator cross function
            if abs(n) >= ExitPeriod and ((state == PD_LONG and n < 0) or (state == PD_SHORT and n > 0)) :
                nowAccount = ext.GetAccount()
                Dict2 = ext.Sell(nowAccount.Stocks - initAccount.Stocks) if state == PD_LONG else ext.Buy(initAccount.Stocks - nowAccount.Stocks)
                state = STATE_IDLE
                nowAccount = ext.GetAccount()
                LogProfit(nowAccount.Balance - initAccount.Balance,'Money:',nowAccount.Balance,'Coins:',nowAccount.Stocks,'Close details:',Dict2,'Crossover period:',n)
            Sleep(Interval * 1000)


```


Detail

https://www.fmz.com/strategy/21157

Last Modified

2016-09-30 23:25:18