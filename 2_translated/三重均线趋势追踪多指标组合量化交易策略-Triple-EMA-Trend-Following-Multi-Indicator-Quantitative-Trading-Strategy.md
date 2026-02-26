``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2025-01-15 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT","balance":49999}]
*/

//@version=5
strategy("Daily Strategy with Triple EMA, DMI, DPO, RSI, and ATR", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Input parameters
fastEmaLength = input.int(10, title="Fast EMA Length")
mediumEmaLength = input.int(25, title="Medium EMA Length")
slowEmaLength = input.int(50, title="Slow EMA Length")
dmiLength = input.int(14, title="DMI Length")
adxSmoothing = input.int(14, title="ADX Smoothing")
dpoLength = input.int(14, title="DPO Length")
rsiLength = input.int(14, title="RSI Length")
atrLength = input.int(14, title="ATR Length")
riskPercentage = input.float(2.0, title="Risk Percentage", step=0.1)
atrMultiplier = input.float(1.5, title="ATR Multiplier for Stop Loss", step=0.1)
tpMultiplier = input.float(2.0, title="ATR Multiplier for Take Profit", step=0.1)

// Calculate EMAs
fastEma = ta.ema(close, fastEmaLength)
mediumEma = ta.ema(close, mediumEmaLength)
slowEma = ta.ema(close, slowEmaLength)

// Calculate other indicators
[adx, diPlus, diMinus] = ta.adx(high, low, close, dmiLength, adxSmoothing)
dpo = ta.dpo(close, dpoLength)
rsi = ta.rsi(close, rsiLength)
atrValue = ta.atr(atrLength)

// Trade logic
longCondition = ta.crossover(fastEma, mediumEma) and fastEma > slowEma and adx > 25 and rsi > 50 and dpo > 0
shortCondition = ta.crossunder(fastEma, mediumEma) and fastEma < slowEma and adx > 25 and rsi < 50 and dpo < 0

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Risk management
positionSize = riskPercentage * account_balance() / atrValue / atrMultiplier
stopLoss = na
takeProfit = na

if (strategy.position_size > 0) // Long position
    stopLoss = strategy.position_avg_price - atrValue * atrMultiplier
    takeProfit = strategy.position_avg_price + atrValue * tpMultiplier

if (strategy.position_size < 0) // Short position
    stopLoss = strategy.position_avg_price + atrValue * atrMultiplier
    takeProfit = strategy.position_avg_price - atrValue * tpMultiplier

// Plot indicators on chart
plot(fastEma, title="Fast EMA", color=color.blue)
plot(mediumEma, title="Medium EMA", color=color.orange)
plot(slowEma, title="Slow EMA", color=color.red)
hline(adx, "ADX", color=color.green, linestyle=hline.style_dotted)
plot(dpo, title="DPO", color=color.purple)
hline(50, "RSI Midpoint", color=color.gray)
plot(rsi, title="RSI", color=color.yellow)
plot(atrValue, title="ATR", color=color.magenta)

```