``` pinescript
/*backtest
start: 2022-12-08 00:00:00
end: 2023-12-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy(title="Stochastic RSI", shorttitle="Stoch RSI", overlay = true)
Per = input(5, title="Length", minval=1)
smoothK = input(3, minval=1)
smoothD = input(3, minval=1)
lengthRSI = input(14, minval=1)
lengthStoch = input(14, minval=1)
src = input(close, title="RSI Source")

rsi1 = rsi(src, lengthRSI)
K = sma(stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
D = sma(K, smoothD)

// Calculate RVI
rvi = sum((close - open), Per) / sum(high - low, Per)
sig = sma(rvi, 5)

// Plot indicators (optional for visualization purposes)
plot(rvi, color=green, title="RVI")
plot(sig, color=red, title="Signal")

// Plot K and D values
plot(K, title="K")
plot(D, title="D")

// Buy signal conditions
Dn = K <= D  and K > 70 and rvi <= sig  and rvi[1] >= sig[1]
Up= K >= D  and K < 30 and rvi >= sig  and rvi[1] <= sig[1]

ARROW = Up - Dn
plotarrow(ARROW, title="Down Arrow", colordown=red, transp=0, maxheight=10, minheight=5)
```