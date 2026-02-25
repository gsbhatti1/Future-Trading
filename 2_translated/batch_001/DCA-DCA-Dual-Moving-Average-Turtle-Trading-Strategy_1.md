> Name

DCA Dual Moving Average Turtle Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/8c106d842892738e54.png)

[trans]
#### Overview
The DCA Dual Moving Average Turtle Trading Strategy is a quantitative trading strategy based on dual moving average crossover and Dollar Cost Averaging (DCA). This strategy uses two Simple Moving Averages (SMAs) with different periods as buy and sell signals, while employing the DCA method to reduce purchase costs. A buy signal is generated when the fast SMA crosses above the slow SMA, and a sell signal is generated when the opposite occurs. The strategy aims to capture medium to long-term market trends while mitigating risks from market volatility through the DCA approach.

#### Strategy Principle
1. Calculate the fast SMA and slow SMA.
2. When the fast SMA crosses above the slow SMA, a buy signal is generated, and the strategy purchases a fixed amount (DCA amount).
3. When the fast SMA crosses below the slow SMA, a sell signal is generated, and the strategy sells all positions.
4. At each DCA interval (e.g., 14 days), the strategy makes another fixed-amount purchase to reduce the average holding cost.
5. The strategy reduces purchase costs through the DCA method while capturing market trends via SMA crossovers.

#### Strategy Advantages
1. Dual moving average crossovers effectively capture medium to long-term market trends.
2. The DCA method can lower purchase costs and reduce risks from market volatility.
3. The strategy logic is simple, making it easy to implement and optimize.
4. It is applicable to most markets and assets, offering strong versatility.

#### Strategy Risks
1. During market consolidation or unclear trends, frequent crossovers may generate excessive trading signals, increasing transaction costs.
2. While the DCA method can reduce average purchase costs, it may increase potential losses in a continuously declining market.
3. The strategy relies on historical data and may become ineffective when significant market changes occur.

#### Strategy Optimization Directions
1. Optimize SMA period parameters to find combinations better suited for specific markets and assets.
2. Introduce other technical indicators such as RSI and MACD to assist in assessing market trends and signal reliability.
3. Adjust the DCA amount and interval according to market characteristics and risk preferences.
4. Add stop-loss and take-profit mechanisms to control the risk and return of individual trades.

#### Summary
The DCA Dual Moving Average Turtle Trading Strategy captures market trends through SMA crossovers and reduces purchase costs and risks using the DCA method. The strategy features simple logic and broad applicability but requires careful parameter optimization and risk management in practice. Further improvements in performance and stability can be achieved by incorporating additional technical indicators, optimizing DCA parameters, and adding stop-loss and take-profit mechanisms.
[/trans]

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Fast SMA Period|
|v_input_2|28|Slow SMA Period|
|v_input_3|100|DCA Amount|
|v_input_4|14|DCA Interval (Days)|

> Source (PineScript)

```pinescript
/*backtest
start: 2024-04-21 00:00:00
end: 2024-04-28 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © loggolitasarim

//@version=5
strategy("DCA YSMA HSMA Stratejisi", overlay=true, calc_on_every_tick=true)

// Parameters
sma_fast = input(14, "Hızlı SMA Dönemi")
sma_slow = input(28, "Yavaş SMA Dönemi")
dca_amount = input(100, "DCA Miktarı")
dca_interval = input(14, "DCA Aralığı (Gün)")

// Fast and slow SMA calculations
fast_sma = ta.sma(close, sma_fast)
slow_sma = ta.sma(close, sma_slow)

// DCA calculations
var float dca_average_price = na
var int dca_count = na

if (bar_index % dca_interval == 0)
    dca_count := nz(dca_count, 0) + 1
    dca_average_price := nz(dca_average_price, close) * (dca_count - 1) + close
    dca_average_price /= dca_count

// Buy and sell signals
longCondition = ta.crossover(fast_sma, slow_sma)
shortCondition = ta.crossunder(fast_sma, slow_sma)

if (longCondition)
    strategy.entry("Alım", strategy.long, qty=dca_amount)
if (shortCondition)
    strategy.entry("Satım", strategy.short)

// Plotting
plot(fast_sma, "Hızlı SMA", color=color.blue)
plot(slow_sma, "Yavaş SMA", color=color.red)

// Alerts
alertcondition(longCondition, "Alım Sinyali", "Alım Sinyali")
alertcondition(shortCondition, "Satım Sinyali", "Satım Sinyali")
```

> Detail

https://www.fmz.com/strategy/449814

> Last Modified

2024-04-29 14:26:59