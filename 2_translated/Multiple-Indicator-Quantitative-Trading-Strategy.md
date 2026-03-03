``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='Pinku Buy', overlay=true)

fromMonth = input.int(defval=1, title='From Month', minval=1, maxval=12)
fromDay = input.int(defval=1, title='From Day', minval=1, maxval=31)
fromYear = input.int(defval=2021, title='From Year', minval=1970)
thruMonth = input.int(defval=1, title='Thru Month', minval=1, maxval=12)
thruDay = input.int(defval=1, title='Thru Day', minval=1, maxval=31)
thruYear = input.int(defval=2112, title='Thru Year', minval=1970)

showDate = input(defval=true, title='Show Date Range')

start = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finish = timestamp(thruYear, thruMonth, thruDay, 23, 59)

window() => true

// ema crossover
length1 = input.int(10)
length2 = input.int(20)
ema1 = ta.ema(close, length1)
ema2 = ta.ema(close, length2)

// VWMA
VWMA_len = input.int(20)
vwma = ta.vwma(close, VWMA_len)

// SuperTrend
STR_Period = input.int(22)
STR_Multiplier = input.float(5)
[upperband, lowerband] = ta.supertrend(STR_Period, STR_Multiplier)

// RSI
rsi_period = input.int(14)
over_sold = input.int(44)
over_bought = input.int(56)
rsi = ta.rsi(close, rsi_period)

// MACD
slow_len_macd = input.int(12)
fast_len_macd = input.int(26)
signal_len_macd = input.int(9)
macd_line = ta.macd(close, slow_len_macd, fast_len_macd, signal_len_macd)[0]
macd_signal = ta.macd(close, slow_len_macd, fast_len_macd, signal_len_macd)[1]

// ADX
adx_smooth = input.int(14)
di_length = input.int(14)
adx_value = ta.adx(high, low, close, adx_smooth)

// ATR
adx_greater_than = input.int(25)
atr = ta.atr(14)

// StopLoss and Profit
stopLoss = input.float(0.5)
profitRatio = input.float(1.5)

// Reverse Limit
reverseLimit = input.int(1024)

// Averaging position?
averagingPosition = input.bool(true)

// Strategy Logic
var float buyPrice = na
var int buyTime = 0

if (window())
    if ta.crossover(ema1, ema2)
        strategy.entry("Buy", strategy.long)
        if showDate
            label.new(bar_index, high, str.tostring(time(timestamp)), color=color.green, textcolor=color.white, style=label.style_label_down)

    if close > vwma and rsi < over_sold
        strategy.entry("Buy", strategy.long)

    if upperband < close and macd_line > 0 and macd_signal > 0
        strategy.entry("Buy", strategy.long)
    
    if lowerband > close and macd_line < 0 and macd_signal < 0
        strategy.entry("Buy", strategy.short)

    if rsi > over_bought
        strategy.close("Sell")

// Stop Loss Logic
if (strategy.position_size > 0)
    stopPrice = strategy.position_avg_price * (1 - stopLoss)
    strategy.exit("StopLoss Long", "Buy", stop=stopPrice, limit=strategy.position_avg_price * (1 + profitRatio))

// Reverse Position Logic
if (reverseLimit < 0 and strategy.position_size != 0)
    if rsi < over_sold and macd_line > 0
        strategy.close("Sell")
        
```

This completes the translation while preserving all code blocks, numbers, and formatting.