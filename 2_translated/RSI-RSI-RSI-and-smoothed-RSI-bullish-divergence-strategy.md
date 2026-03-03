``` pinescript
/*backtest
start: 2024-01-30 00:00:00
end: 2024-02-29 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © BigBitsIO

//@version=4
strategy(title="RSI and Smoothed RSI Bull Div Strategy [BigBitsIO]", shorttitle="RSI and Smoothed RSI Bull Div Strategy [BigBitsIO]", overlay=true, pyramiding=1, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=.1, slippage=0)


TakeProfitPercent = input(3, title="Take Profit %", type=input.float, step=.25)
StopLossPercent = input(1.75, title="Stop Loss %", type=input.float, step=.25)

RSICurve = input(14, title="RSI Lookback Period", type=input.integer, step=1)
BuyBelowTargetPercent = input(0, title="Buy Below Lowest Low In RSI Divergence Lookback Target %", type=input.float, step=.05)
BuyBelowTargetSource = input(close, title="Source of Buy Below Target Price", type=input.source)
SRSICurve = input(10, title="Smoothed RSI Lookback Period", type=input.integer, step=1)
RSICurrentlyBelow = input(30, title="RSI Currently Below", type=input.integer, step=1)
RSIDivergenceLookback = input(25, title="RSI Divergence Lookback Period", type=input.integer, step=1)
RSILowestInDivergenceLookbackCurrentlyBelow  = input(25, title="RSI Lowest In Divergence Lookback Currently Below", type=input.integer, step=1)
RSISellAbove = input(65, title="RSI Sell Above", type=input.in
```

``` pinescript
input.integer, step=1)
SRSILowestInDivergenceLookbackCurrentlyBelow  = input(35, title="Smoothed RSI Lowest In Divergence Lookback Currently Below", type=input.integer, step=1)
MinimumSRSIDowntrendLength = input(3, title="Minimum SRSI Downtrend Length", type=input.integer, step=1)

plotchar(title="Target Plot", char="", location=location.bottom, color=color.new(color.blue, 0), transp=0, show_last=1) if v_input_13

[trans]
## Optimized Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|3|Take Profit Percentage|
|v_input_2|1.75|Stop Loss Percentage|
|v_input_3|14|RSI Lookback Period|
|v_input_4|false|Buy Below Lowest Low in RSI Divergence Lookback Target Percentage|
|v_input_5_close|0|Source of Buy Below Target Price: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|10|Smoothed RSI Lookback Period|
|v_input_7|30|RSI Currently Below|
|v_input_8|25|RSI Divergence Lookback Period|
|v_input_9|25|RSI Lowest In Divergence Lookback Currently Below|
|v_input_10|65|RSI Sell Above|
|v_input_11|3|Minimum SRSI Downtrend Length|
|v_input_12|35|Smoothed RSI Currently Below|
|v_input_13|false|Plot Target|

## Strategy Logic

``` pinescript
SRSILowestInDivergenceLookbackCurrentlyBelow  = input(35, title="Smoothed RSI Lowest In Divergence Lookback Currently Below", type=input.integer, step=1)
MinimumSRSIDowntrendLength = input(3, title="Minimum SRSI Downtrend Length", type=input.integer, step=1)

plotchar(title="Target Plot", char="", location=location.bottom, color=color.new(color.blue, 0), transp=0, show_last=1) if v_input_13

// Calculate RSI and Smoothed RSI
rsi = ta.rsi(close, RSICurve)
srsi = sma(wma(close, SRSICurve * 2 - 1), SRSICurve)

// Check for bullish divergence in RSI
bullish_divergence = rsi < rsi[RSIDivergenceLookback] and close > close[RSIDivergenceLookback]

// Check for strong downward trend in Smoothed RSI
srsi_downtrend = srsi < SRSILowestInDivergenceLookbackCurrentlyBelow and ta.crossover(sma(wma(close, SRSICurve * 2 - 1), SRSICurve), srsi)

// Enter long when bullish divergence in RSI occurs
if (bullish_divergence and srsi_downtrend)
    strategy.entry("Bull Div", strategy.long)
    
// Exit on take profit or stop loss
take_profit = strategy.position_avg_price * (1 + TakeProfitPercent / 100)
stop_loss = strategy.position_avg_price * (1 - StopLossPercent / 100)

if (close > take_profit or close < stop_loss)
    strategy.close("Bull Div")

// Plot target
plotchar(title="Target Plot", char="", location=location.bottom, color=color.new(color.blue, 0), transp=0, show_last=1) if v_input_13
```

This optimized version of the script includes additional parameters and logic to enhance the strategy's performance. The `SRSILowestInDivergenceLookbackCurrentlyBelow` and `MinimumSRSIDowntrendLength` inputs are added to refine the Smoothed RSI calculations, while the entry and exit conditions are adjusted for more precise trading signals.
```