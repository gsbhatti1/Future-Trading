<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

EMA-Crossover-Trading-Strategy-with-Dynamic-Take-Profit-and-Stop-Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/15d45103b85794ffdf0.png)
[trans]
#### Overview

This strategy uses the crossover of Exponential Moving Averages (EMAs) to generate trading signals while dynamically setting take-profit and stop-loss levels. When the shorter-period EMA (EMA 12) crosses above the longer-period EMA (EMA 26), a buy signal is generated; conversely, when EMA 12 crosses below EMA 26, a sell signal is generated. The strategy sets different dynamic take-profit and stop-loss levels for long and short positions. For long positions, take-profit is set 8% above the entry price, and stop-loss is set 2.5% below the entry price; for short positions, take-profit is set 8% below the entry price, and stop-loss is set 2.5% above the entry price.

#### Strategy Principle

The core of this strategy is using the crossover of two EMAs with different periods to generate trading signals. EMA is a trend-following indicator that smooths price data and reduces noise. When the shorter-period EMA crosses above the longer-period EMA, it indicates strengthening price momentum and generates a buy signal; conversely, when the shorter-period EMA crosses below the longer-period EMA, it indicates weakening price momentum and generates a sell signal.

Simultaneously, the strategy employs a dynamic take-profit and stop-loss approach, setting different take-profit and stop-loss levels based on the current position direction (long or short). This dynamic adjustment method allows profits to expand fully during strong trends while cutting losses promptly when prices reverse, thus better controlling risk.

#### Strategy Advantages

1. **Simple and Easy to Use**: The strategy uses only the crossover of two EMA lines to generate trading signals, with clear logic that's easy to understand and implement.

2. **Trend Following**: The EMA indicator has excellent trend-following capabilities and can effectively capture major price trends.

3. **Dynamic Take-Profit and Stop-Loss**: Dynamically adjusting take-profit and stop-loss levels based on position direction allows profits to expand fully during strong trends while cutting losses promptly when prices reverse, better controlling risk.

4. **Strong Adaptability**: The strategy is suitable for different market environments and trading instruments, showing strong adaptability and flexibility.

#### Strategy Risks

1. **Parameter Optimization Risk**: The selection of EMA periods and the setting of take-profit and stop-loss ratios need to be optimized according to specific market environments and trading instruments. Inappropriate parameter settings may lead to poor strategy performance.

2. **Frequent Trading Risk**: When the market is in a consolidation phase, EMA crossovers may occur frequently, causing the strategy to generate numerous trading signals, increasing transaction costs and risks.

3. **Trend Reversal Risk**: When the market trend reverses suddenly, the strategy may generate incorrect trading signals, resulting in losses.

#### Strategy Optimization Directions

1. **Introduce Other Technical Indicators**: Consider incorporating other technical indicators such as RSI, MACD, etc., to assist in confirming EMA crossover signals and improve trading signal reliability.

2. **Optimize Parameter Settings**: Through optimization testing of EMA periods and take-profit/stop-loss ratios, find the optimal parameter combination suitable for specific market environments and trading instruments.

3. **Introduce Risk Control Measures**: Consider implementing risk control measures such as position management and capital management to better control trading risks.

4. **Combine with Fundamental Analysis**: Integrate technical analysis with fundamental analysis, comprehensively considering market environment, economic data, and other factors to improve the accuracy of trading decisions.

#### Summary

This strategy uses EMA crossovers to generate trading signals and employs a dynamic take-profit and stop-loss method to control risk. It offers advantages such as simplicity, trend-following capability, and strong adaptability, but also faces challenges including parameter optimization risk, frequent trading risk, and trend reversal risk. By introducing other technical indicators, optimizing parameter settings, implementing risk control measures, and combining with fundamental analysis, the strategy's performance can be further optimized, improving its applicability and profitability in actual trading.

[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2023-05-23 00:00:00
end: 2024-05-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("CDC Action Zone Trading Bot with Dynamic TP/SL", overlay=true)

// ดึงข้อมูลราคาปัจจุบัน
current_price = close

// คำนวณเส้น EMA 12 และ EMA 26
ema12 = ta.ema(current_price, 12)
ema26 = ta.ema(current_price, 26)

// กำหนดเปอร์เซ็นต์ Take Profit และ Stop Loss
takeProfitPercent = 0.080
stopLossPercent = 0.025

// คำนวณระดับ Take Profit และ Stop Loss
longTakeProfit = strategy.position_avg_price * (1 + takeProfitPercent)
longStopLoss = strategy.position_avg_price * (1 - stopLossPercent)

shortTakeProfit = strategy.position_avg_price * (1 - takeProfitPercent)
shortStopLoss = strategy.position_avg_price * (1 + stopLossPercent)

// สัญญาณ Buy
buySignal = (ema12 > ema26) and (ema12[1] <= ema26[1])

// สัญญาณ Sell
sellSignal = (ema12 < ema26) and (ema12[1] >= ema26[1])

// เปิด Position Long
if (buySignal)
    strategy.entry("Long", strategy.long)

// เปิด Position Short
if (sellSignal)
    strategy.entry("Short", strategy.short)

// ปิด Position Long เมื่อถึง Take Profit หรือ Stop Loss
if (strategy.position_size > 0)
    strategy.exit("Long TP/SL", from_entry="Long", limit=longTakeProfit, stop=longStopLoss, comment="TP/SL")

// ปิด Position Short เมื่อถึง Take Profit หรือ Stop Loss
if (strategy.position_size < 0)
    strategy.exit("Short TP/SL", from_entry="Short", limit=shortTakeProfit, stop=shortStopLoss, comment="TP/SL")

// ปิด Position Long เมื่อเกิดสัญญาณขาย
if (strategy.position_size > 0 and sellSignal)
    strategy.close("Long", comment="Sell Signal")

// ปิด Position Short เมื่อเกิดสัญญาณซื้อ
if (strategy.position_size < 0 and buySignal)
    strategy.close("Short", comment="Buy Signal")

// Debugging messages to plot the calculated levels for visual verification
//plot(longTakeProfit, title="Long Take Profit", color=color.green, linewidth=1, style=plot.style_line)
//plot(longStopLoss, title="Long Stop Loss", color=color.red, linewidth=1, style=plot.style_line)
//plot(shortTakeProfit, title="Short Take Profit", color=color.green, linewidth=1, style=plot.style_line)
//plot(shortStopLoss, title="Short Stop Loss", color=color.red, linewidth=1, style=plot.style_line)

```

> Detail

https://www.fmz.com/strategy/452820

> Last Modified

2024-05-29 16:55:22