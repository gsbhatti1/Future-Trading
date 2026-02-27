``` pinescript
/*backtest
start: 2022-10-18 00:00:00
end: 2023-10-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='Price-Gap-and-Trend-Following-Trading-Strategy', shorttitle='PGTFTS', overlay=true)

// Input settings
ccimomCross = input.string('CCI', 'Entry Signal Source', options=['CCI', 'Momentum'])
ccimomLength = input.int(10, minval=1, title='CCI/Momentum Length')
useDivergence = input.bool(false, title='Find Regular Bullish/Bearish Divergence')
rsiOverbought = input.int(65, minval=1, title='RSI Overbought Level')
rsiOversold = input.int(35, minval=1, title='RSI Oversold Level')
rsiLength = input.int(14, minval=1, title='RSI Length')
plotMeanReversion = input.bool(true, 'Plot Mean Reversion Bands on the chart')
emaPeriod = input(200, title='Lookback Period (EMA)')
bandMultiplier = input.float(1.6, title='Outer Bands Multiplier')

// CCI and Momentum
var float cciValue = na
var int ccimomDir = 0

if (ccimomCross == 'CCI')
    [cciValue, _, _] := ta.cci(ccimomLength)
else if (ccimomCross == 'Momentum')
    [_, _, cciValue] := ta.mom(ccimomLength)

// RSI
rsi = ta.rsi(rsiLength)

// Divergence check
bullishDivergence = na
bearishDivergence = na

if (useDivergence)
    if (ccimomCross == 'CCI')
        bullishDivergence := ta.cci_divergence(rsi, rsiLength)
        bearishDivergence := ta.cci_divergence(-rsi, rsiLength)
    else
        bullishDivergence := ta.mom_divergence(rsi, rsiLength)
        bearishDivergence := ta.mom_divergence(-rsi, rsiLength)

// Mean Reversion Bands
bBands = ta.bband(rsi, emaPeriod, bandMultiplier)

longCondition = na(ccimomDir) or (ccimomDir == 1 and cciValue > bBands[0] and rsi < rsiOversold)
shortCondition = na(ccimomDir) or (ccimomDir == -1 and cciValue < bBands[0] and rsi > rsiOverbought)

if (longCondition)
    strategy.entry('Long', strategy.long)
    
if (shortCondition)
    strategy.entry('Short', strategy.short)

// Plotting
plot(bBands, color=color.blue, title='Mean Reversion Bands')
plotshape(series=bullishDivergence, location=location.belowbar, color=color.green, style=shape.labelup, title='Bullish Divergence')
plotshape(series=bearishDivergence, location=location.abovebar, color=color.red, style=shape.labeldown, title='Bearish Divergence')
```

This Pine Script implements the Price-Gap-and-Trend-Following-Trading-Strategy with the specified inputs and logic. The strategy uses CCI or Momentum for entry signals based on user input, checks RSI levels for overbought/oversold conditions, identifies divergences if selected, and enters trades when conditions are met. Mean reversion bands from RSI are plotted to visualize trade opportunities.