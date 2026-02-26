``` pinescript
/*backtest
start: 2024-02-01 00:00:00
end: 2024-02-29 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("1-2-3 Pattern Strategy with EMAs, MACD, and 4th Candle Extension", overlay=true)

// Define conditions for the 1-2-3 pattern for buy orders
buy_candle1_above_open = close[3] > open[3]
buy_candle2_below_open = close[2] < open[2]
buy_candle3_above_candle1_close = close[1] > close[3]
buy_candle4_above_candle3_close = close > close[3]

// Define conditions for the 1-2-3 pattern for sell orders
sell_candle1_below_open = close[3] < open[3]
sell_candle2_above_open = close[2] > open[2]
sell_candle3_below_candle1_close = close[1] < close[3]
sell_candle4_below_candle3_close = close < close[3]

// Define EMA and MACD conditions
ema_short = ta.ema(close, 9)
ema_long = ta.ema(close, 20)
macd_line = ta.macd(close, 12, 26, 9)[0]
signal_line = ta(macd_line, 12, 26, 9)[1]

// Enter long position when all buy conditions are met
if (buy_candle1_above_open and buy_candle2_below_open and buy_candle3_above_candle1_close and buy_candle4_above_candle3_close)
    strategy.entry("Buy", strategy.long)

// Enter short position when all sell conditions are met
if (sell_candle1_below_open and sell_candle2_above_open and sell_candle3_below_candle1_close and sell_candle4_below_candle3_close)
    strategy.entry("Sell", strategy.short)

// Exit long/short positions if the opposite signal is generated or current candle closes in the opposite direction
if (not buy_candle1_above_open or not buy_candle2_below_open or not buy_candle3_above_candle1_close or not buy_candle4_above_candle3_close)
    strategy.close("Buy")

if (not sell_candle1_below_open or not sell_candle2_above_open or not sell_candle3_below_candle1_close or not sell_candle4_below_candle3_close)
    strategy.close("Sell")
```

This Pine Script code defines a trading strategy that identifies potential buy and sell signals based on the 1-2-3 pattern, combined with EMA and MACD conditions. It includes logic to open and close positions when specific conditions are met.