``` pinescript
/*backtest
start: 2023-11-20 00:00:00
end: 2023-12-20 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// created by Space Jellyfish
//@version=4

strategy("EMA Pullback Strategy", overlay = true, initial_capital=10000, commission_value = 0.075)

target_stop_ratio = input(title="Take Profit Stop Loss ratio", type=input.float, defval=2.06, minval=0.5, maxval=100)
riskLimit_low =  input(title="lowest risk per trade", type=input.float, defval=0.008, minval=0, maxval=100)
riskLimit_high =  input(title="highest risk per trade", type=input.float, defval=0.02, minval=0, maxval=100)
// Adjust position size if the risk is smaller or larger than the limit

ema_pullbackLevel_period = input(title="EMA1 for pullback level Period", type=input.integer, defval=33, minval=1, maxval=10000)
ema_pullbackLimit_period = input(title="EMA2 for pullback limit Period", type=input.integer, defval=165, minval=1, maxval=10000)
ema_trend_period = input(title="EMA3 for trend Period", type=input.integer, defval=365, minval=1, maxval=10000)

startDate = input(title="Start Date", type=input.integer, defval=1, minval=1, maxval=31)
startMonth = input(title="Start Month", type=input.integer, defval=1, minval=1, maxval=12)
startYear = input(title="Start Year", type=input.integer, defval=2018, minval=1970, maxval=2100)

// Calculate EMAs
ema1 = ta.ema(close, ema_pullbackLevel_period)
ema2 = ta.ema(close, ema_pullbackLimit_period)
ema3 = ta.ema(close, ema_trend_period)

longCondition = ta.crossover(close, ema1) and close > ema2
shortCondition = ta.crossunder(close, ema1) and close < ema2

// Position management
if (startDate == 0 or startMonth == 0 or startYear == 0)
    strategy.entry("Long", strategy.long, when=longCondition)
else 
    strategy.entry("Long", strategy.long, when=longCondition and date >= timestamp(startYear, startMonth, startDate))

strategy.exit("Take Profit/Stop Loss", "Long", stop=true, limit=target_stop_ratio * riskLimit_low, trail_offset=riskLimit_high)

// Plot EMAs
plot(ema1, title="EMA1", color=color.blue)
plot(ema2, title="EMA2", color=color.red)
plot(ema3, title="EMA3", color=color.green)
```

This translation maintains the original code and formatting while translating the human-readable text.