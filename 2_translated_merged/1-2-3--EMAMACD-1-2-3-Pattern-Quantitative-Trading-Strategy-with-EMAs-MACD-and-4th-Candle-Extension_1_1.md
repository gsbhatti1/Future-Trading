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
buy_candle3_above_first_candle_close = close[1] > close[3]
buy_candle4_above_third_candle_close = close >= close[2]

// Define conditions for the 1-2-3 pattern for sell orders
sell_candle1_below_open = close[3] < open[3]
sell_candle2_above_open = close[2] > open[2]
sell_candle3_below_first_candle_open = close[1] < close[3]
sell_candle4_below_second_candle_close = close <= close[2]

// Calculate the EMAs
ema9 = ta.ema(close, 9)
ema20 = ta.ema(close, 20)

// Calculate MACD and signal line
macd_line = ta.macd(close, 12, 26, 9)[0]
signal_line = ta.sma(macd_line, 9)

// Define buy and sell signals based on the conditions and EMAs/MACD
buy_signal = (buy_candle1_above_open and buy_candle2_below_open and buy_candle3_above_first_candle_close and close >= ema9 and close >= ema20 and macd_line > signal_line)
sell_signal = (sell_candle1_below_open and sell_candle2_above_open and sell_candle3_below_first_candle_open and close <= ema9 and close <= ema20 and macd_line < signal_line)

// Place orders based on the signals
if (buy_signal)
    strategy.entry("Buy", strategy.long)

if (sell_signal)
    strategy.entry("Sell", strategy.short)

// Exit orders when opposite conditions are met or current candle closes in the opposite direction of the position
if (not buy_signal and not sell_signal)
    if (close < open)
        strategy.close("Buy")
    else if (close > open)
        strategy.close("Sell")

```

This Pine Script code implements a trading strategy based on the 1-2-3 pattern, combined with EMAs and MACD indicators. It defines clear buy and sell signals and handles entry and exit conditions accordingly.