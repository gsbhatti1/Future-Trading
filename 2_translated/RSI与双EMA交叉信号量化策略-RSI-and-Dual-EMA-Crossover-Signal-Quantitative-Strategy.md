> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|14|RSI Length|
|v_input_int_2|100|EMA Length (Closing Price)|
|v_input_int_3|20|EMA Length (Low Price)|
|v_input_int_4|30|Oversold Level|
|v_input_int_5|70|Overbought Level|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI-and-Dual-EMA-Crossover-Signal-Quantitative-Strategy", shorttitle="RSI&DualEMA", overlay=true)

// Input Arguments
rsiLength = input.int(14, title="RSI Length")
emaCloseLen = input.int(100, title="EMA Length (Closing Price)")
emaLowLen = input.int(20, title="EMA Length (Low Price)")
oversoldLevel = input.int(30, title="Oversold Level")
overboughtLevel = input.int(70, title="Overbought Level")

// Calculate RSI
rsi = rsi(close, rsiLength)

// Calculate EMAs
emaClose = ta.ema(close, emaCloseLen)
emaLow = ta.ema(low, emaLowLen)

// Buy Condition: Close price falls below both EMAs and RSI is below oversold level
buyCondition = close < emaClose and close < emaLow and rsi < oversoldLevel

// Sell Condition: Close price breaks above both EMAs and RSI is above overbought level
sellCondition = close > emaClose and close > emaLow and rsi > overboughtLevel

// Plot EMAs on chart
plot(emaClose, title="EMA (Closing Price)", color=color.blue)
plot(emaLow, title="EMA (Low Price)", color=color.red)

// Generate Buy Signal
if (buyCondition)
    strategy.entry("Buy", strategy.long)

// Generate Sell Signal
if (sellCondition)
    strategy.close("Buy")

```

This Pine Script defines a trading strategy that uses the RSI and dual EMAs to generate buy and sell signals. It includes input arguments for customizing the RSI length, EMA lengths, and overbought/oversold levels. The script plots the EMAs on the chart and generates trading signals based on the defined conditions.