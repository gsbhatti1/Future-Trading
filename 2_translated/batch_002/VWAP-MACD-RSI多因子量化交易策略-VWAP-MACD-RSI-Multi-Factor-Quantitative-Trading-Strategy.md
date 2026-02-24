``` pinescript
/*backtest
start: 2024-10-27 00:00:00
end: 2024-11-26 00:00:00
period: 4h
basePeriod: 4h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("pbs", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

// Input for take-profit and stop-loss
takeProfitPercent = input.float(0.5, title="Take Profit (%)", step=0.1) / 100
stopLossPercent = input.float(0.25, title="Stop Loss (%)", step=0.1) / 100

macdFastLength = input.int(12, title="MACD Fast Length")
macdSlowLength = input.int(26, title="MACD Slow Length")
macdSignalLength = input.int(9, title="MACD Signal Length")

rsiLength = input.int(14, title="RSI Length")
rsiOverbought = input.int(70, title="RSI Overbought Level", step=1)
rsiOversold = input.int(30, title="RSI Oversold Level", step=1)

vwap = ta.vwap(close)

[macdLine, signalLine, _] = ta.macd(close, macdFastLength, macdSlowLength, macdSignalLength)
macdHistogram = macdLine - signalLine

rsi = ta.rsi(close, rsiLength)

plot(vwap, color=color.purple, linewidth=2, title="VWAP")
hline(rsiOverbought, "Overbought", color=color.red, linestyle=hline.style_dotted)
hline(rsiOversold, "Oversold", color=color.green, linestyle=hline.style_dotted)
plot(macdLine, color=color.blue, title="MACD Line")
plot(signalLine, color=color.orange, title="Signal Line")

// Buy Condition
longCondition = ta.crossover(close, vwap) and macdHistogram > 0 and rsi < rsiOverbought

// Sell Condition
shortCondition = ta.crossunder(close, vwap) and macdHistogram < 0 and rsi > rsiOversold

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.exit("Short Exit", "Long", stop=stopLossPercent * close, limit=takeProfitPercent * close)

```