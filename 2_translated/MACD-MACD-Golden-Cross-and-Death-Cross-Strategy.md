``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=5
// @description This strategy uses MACD DIF and DEA lines to generate golden cross and death cross signals for entering and exiting trades. Backtesting shows a win rate of about 40% with an annualized return of 1.05 on BTCUSDT, but it will cause the number of held assets to increase continuously, making it unsuitable as an independent arbitrage strategy.

strategy("MACD Golden Cross Strategy", overlay=true)

fastLength = input(12, "Fast Line Length")
slowLength = input(26, "Slow Line Length")
MACDLength = input(9, "MACD Signal Line Length")

deltaIncreaseOver0 = input(color.green, 'MACD Bar Growth Above 0')
deltaIncreaseUnder0 = input(color.rgb(153, 230, 156), 'MACD Bar Growth Below 0')

deltaDecreaseOver0 = input(color.orange, 'MACD Bar Decline Above 0')
deltaDecreaseUnder0 = input(color.red, 'MACD Bar Decline Below 0')

buySellEnabled = input(true, 'Show Buy and Sell Signals')

// @variable Long Rounds
var longRound = 0
// @variable Short Rounds
var shortRound = 0

DIF = ta.ema(close, fastLength) - ta.ema(close, slowLength) // Fast and Slow EMA difference
EDA = ta.ema(DIF, MACDLength) // EMA of the DIF line
delta = DIF - EDA // MACD bar height

// plot(0, 'Zero', color.black)
plot(DIF, 'DIF', color.yellow)
plot(EDA, "EDA", color.purple)

isDeltaIncreasing = delta[1] < delta
isDeltaOver0 = delta > 0
deltaColor = isDeltaIncreasing ? (isDeltaOver0? deltaIncreaseOver0: deltaIncreaseUnder0) : (isDeltaOver0?
```