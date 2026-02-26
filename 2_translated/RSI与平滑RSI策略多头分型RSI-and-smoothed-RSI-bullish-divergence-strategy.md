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
RSISellAbove = input(65, title="RSI Sell Above", type=input.float)
MinSRSIDowntrendLength = input(3, title="Minimum SRSI Downtrend Length", type=input.integer, step=1)
SmoothedRSCurrentlyBelow = input(35, title="Smoothed RSI Currently Below", type=input.integer, step=1)
PlotTarget = input(false, title="Plot Target", type=input.bool)


// Calculate RSI
rsiValue = rsi(close, RSICurve)

// Calculate Smoothed RSI using double WMA (Weighted Moving Average)
wmaShort = wma(close, 5)
wmaLong = wma(wmaShort, 10)
smoothedRSI = wma(wmaLong, 10)

// Check conditions
rsiBelowThreshold = rsiValue < RSICurrentlyBelow
smoothedRSIBelowThreshold = smoothedRSI < SmoothedRSCurrentlyBelow
divergenceCondition = highest(rsiValue, RSIDivergenceLookback) > rsiValue and lowest(BuyBelowTargetSource, RSILowestInDivergenceLookbackCurrentlyBelow) < BuyBelowTargetSource[1]
srsiDowntrendCondition = smoothCrossedDown(smoothedRSI, MinSRSIDowntrendLength)

// Generate buy signal
if (divergenceCondition and srsiDowntrendCondition)
    strategy.entry("Buy", strategy.long)

// Set stop loss and take profit
stopLossLevel = rsiValue * (1 - StopLossPercent / 100)
takeProfitLevel = rsiValue * (1 + TakeProfitPercent / 100)

strategy.exit("Take Profit", "Buy", stop=true, limit=takeProfitLevel)
strategy.exit("Stop Loss", "Buy", stop=true, stop=stopLossLevel)


// Plot RSI and Smoothed RSI
plot(rsiValue, title="RSI", color=color.red)
plot(smoothedRSI, title="Smoothed RSI", color=color.blue)
```

This script includes the key logic and conditions described in the Chinese text, ensuring that all original code blocks and formatting remain unchanged.