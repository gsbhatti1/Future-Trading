> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|50|EMA Period|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-02-11 00:00:00
end: 2024-02-17 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("LinoR EMA Pullback Strategy", shorttitle="EPS", overlay=true)

// Define EMA period
emaPeriod = input(50, title="EMA Period")

// Calculate 50 EMA
ema50 = ta.ema(close, emaPeriod)

// Calculate engulfing conditions
engulfingBullish = close[1] < open[1] and close > open and close > close[1] and open < open[1]
engulfingBearish = close[1] > open[1] and open > close and open > open[1] and close < close[1]

// Define a 1-minute timer
var timer = 0
if bar_index > 0
    timer := timer[1] + 1

// Long condition
longCondition = ta.crossover(close, ema50) and engulfingBullish
if longCondition
    strategy.entry("Buy", strategy.long)

// Short condition
shortCondition = ta.crossunder(close, ema50) and engulfingBearish
if shortCondition
    strategy.close("Buy")
```

This PineScript code defines a simple trading strategy called the LinoR EMA Pullback Strategy. The strategy uses a 50-period Exponential Moving Average (EMA) to identify trend reversals using candlestick patterns like engulfing formations. Here is a detailed breakdown of the script:

1. **Strategy Initialization**: 
   - `strategy("LinoR EMA Pullback Strategy", shorttitle="EPS", overlay=true)` initializes the strategy with the name "LinoR EMA Pullback Strategy" and its short title as "EPS". The `overlay=true` parameter allows this strategy to be plotted on top of the main chart.

2. **EMA Period Definition**:
   - `emaPeriod = input(50, title="EMA Period")` sets the default value for the EMA period to 50 and provides a label for it in the user interface.

3. **EMA Calculation**:
   - `ema50 = ta.ema(close, emaPeriod)` calculates the 50-period Exponential Moving Average of the closing prices.

4. **Engulfing Pattern Conditions**:
   - `engulfingBullish` and `engulfingBearish` are boolean variables that check for bullish and bearish engulfing patterns respectively.
     - `engulfingBullish = close[1] < open[1] and close > open and close > close[1] and open < open[1]`
     - `engulfingBearish = close[1] > open[1] and open > close and open > open[1] and close < close[1]`

5. **Timer for Stop Loss**:
   - A 1-minute timer is defined to set a stop loss mechanism after the entry.
     ```pinescript
     var timer = 0
     if bar_index > 0
         timer := timer[1] + 1
     ```
   
6. **Long Condition and Entry**:
   - `longCondition = ta.crossover(close, ema50) and engulfingBullish` checks for a cross above the EMA and an engulfing bullish pattern.
     ```pinescript
     if longCondition
         strategy.entry("Buy", strategy.long)
     ```

7. **Short Condition and Exit**:
   - `shortCondition = ta.crossunder(close, ema50) and engulfingBearish` checks for a cross below the EMA and an engulfing bearish pattern.
     ```pinescript
     if shortCondition
         strategy.close("Buy")
     ```

This code effectively implements the described trading strategy by combining trend identification using EMAs with reversal signals from candlestick patterns.