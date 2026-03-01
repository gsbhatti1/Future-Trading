``` pinescript
/*backtest
start: 2024-11-10 00:00:00
end: 2024-12-09 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy('MANTHAN BHRAMASTRA', overlay=true)

// Supertrend function
f_supertrend(_period, _multiplier) =>
    atr = ta.sma(ta.tr, _period)
    upTrend = hl2 - _multiplier * atr
    downTrend = hl2 + _multiplier * atr
    var float _supertrend = na
    var int _trendDirection = na
    _supertrend := na(_supertrend[1]) ? hl2 : close[1] > _supertrend[1] ? math.max(upTrend, _supertrend[1]) : math.min(downTrend, _supertrend[1])
    _trendDirection := close > _supertrend ? 1 : -1
    [_supertrend, _trendDirection]

// Supertrend Settings
factor = input(2, title='Supertrend Factor')
atrLength = input(20, title='Supertrend ATR Length')

// Calculate Supertrend
[supertrendValue, direction] = f_supertrend(atrLength, factor)

// MACD Settings
fastLength = input(12, title='MACD Fast Line Length', type=input.integer)
slowLength = input(26, title='MACD Slow Line Length', type=input.integer)
signalSmoothing = input(9, title='MACD Signal Smoothing', type=input.integer)

// Calculate MACD
macdLine = ta.macd(close, fastLength, slowLength, signalSmoothing)[0]
signalLine = ta.macd(close, fastLength, slowLength, signalSmoothing)[1]
histogram = macdLine - signalLine

// Entry Conditions
buyCondition = macdLine > signalLine and direction == 1
sellCondition = macdLine < signalLine and direction == -1

// Risk Management
stopLossPercent = input(0.5 / 100, title='Stop Loss Percentage')
takeProfitPercent = input(99.99 / 100, title='Take Profit Percentage')

// Position Sizing
positionSize = strategy.equity * stopLossPercent

// Place Orders
if (buyCondition)
    strategy.entry('Buy', strategy.long, size=positionSize)

if (sellCondition)
    strategy.close('Buy')

// Plot Indicators
plot(supertrendValue, title='Supertrend Value', color=color.blue)
plot(macdLine, title='MACD Line', color=color.red)
plot(signalLine, title='Signal Line', color=color.green)
plot(histogram, title='Histogram', style=plot.style_histogram, location=location.belowbars)

// Print Logs
strategy.info('Supertrend Direction: ' + str.tostring(direction))
```