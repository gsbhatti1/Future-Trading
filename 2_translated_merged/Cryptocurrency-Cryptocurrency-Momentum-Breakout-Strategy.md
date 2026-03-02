<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Cryptocurrency Momentum Breakout Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/eaab537c14cced3117.png)

[trans]

### Overview

This strategy uses momentum indicators to identify the main trend direction in the cryptocurrency market and establish long positions at breakout points, implementing a trend-following trading approach.

### Strategy Logic  

The strategy uses a custom "Pump&Dump Oscillator" as its sole indicator. This oscillator identifies the main market trend direction using candlestick body sizes. Specifically, it calculates the average of candlestick bodies and multiplies it by a user-defined multiplier. When the body is greater than the moving average, it indicates an uptrend; when the body is less than the moving average, it indicates a downtrend.

Based on the oscillator indicator, this strategy only establishes long positions. When the indicator shows the market is currently in an uptrend, a long position is established at the close of that candlestick. Thereafter, if a downtrend signal appears or a stop loss is triggered, all positions are closed.

The strategy offers two stop loss methods - users can choose one or use both:

1. Percentage stop loss: Users can set the maximum allowable percentage loss per position. If the price falls below this percentage stop loss level, the position is closed.

2. Breakout stop loss: At position entry, record the lowest point of that candlestick. If the price subsequently falls below that point, close the position.

### Advantages Analysis

This strategy has the following advantages:

1. Uses a custom indicator to identify market trends, making it more sensitive and accurate.

2. Long-only approach avoids unlimited loss risks from short selling.

3. Follows the classic trend trading methodology of buying high and selling higher.

4. Provides dual stop loss options for flexible selection of preferred stop loss modes.

5. Simple and clear code that is easy to understand and modify.

6. No dynamic take-profit setup required, avoiding premature profit-taking losses.

### Risk Analysis  

This strategy also carries certain risks:

1. Custom indicators may lack stability and reliability, posing misjudgment risks.

2. Long-only positioning may miss short-term pullback shorting opportunities.

3. Stop loss settings may be overly conservative, preventing holding of longer-term trending positions.

4. Lack of dynamic take-profit requires timely manual profit-taking, introducing operational risks.

5. Though both stop loss methods can be combined, optimal stop loss points may still not be achieved.

6. Trend-following strategies are susceptible to whipsaws in ranging markets, generating excessive invalid trades.

### Optimization Directions

This strategy can be optimized through the following approaches:

1. Try alternative indicators such as KDJ, MACD etc to find more stable and reliable trend identification methods.

2. Add shorting opportunities by allowing short positions during trend reversals to improve strategy returns.

3. Optimize stop loss strategies by testing different parameters to find better stop loss points, or dynamically set stops using indicators like ATR, MA etc.

4. Add dynamic take-profit mechanisms such as trailing stops after breaking previous highs to reduce manual intervention risks.

5. Conduct parameter optimization by adjusting moving average periods, entry conditions etc to find optimal parameter combinations.

6. Add filter conditions such as "Only Long" or bottom reversal indicators to avoid invalid trades.

7. Backtest across different trading pairs to evaluate strategy effectiveness and optimize applicable scope.

8. Use backtesting and paper trading to optimize parameters and stop loss/take profit levels.

### Summary

Overall this is a relatively simple trend-following strategy. It uses a custom momentum indicator to judge market trends, enters long positions at trend initiation stages, and provides dual stop loss methods. Main advantages include clear strategy logic, limited risks, and ease of operation. However there remains room for optimization regarding stop loss strategies and parameter selection. Overall, this strategy provides a foundational trend trading framework for the cryptocurrency market that is very suitable for beginners to learn and practice. But thorough backtesting should still be conducted to verify effectiveness and further optimize before live deployment.
||

### Overview

This strategy utilizes momentum indicators to identify the main trend direction in the Cryptocurrency market and establishes long positions at breakout points, realizing the trading idea of trend following.

### Strategy Logic

The strategy uses a custom "Pump&Dump Oscillator" as the only indicator. The oscillator uses the size of candlestick bodies to identify the main trend direction of the market. Specifically, it calculates the moving average of candlestick bodies and multiplies it by a user-set multiplier. When the body is greater than the moving average, it signals an uptrend. When the body is less than the moving average, it signals a downtrend.

Based on the oscillator indicator, this strategy only establishes long positions. When the indicator shows that the market is currently in an uptrend, a long position is established on the close of that candlestick. Afterwards, if a downtrend signal appears, or the stop loss is triggered, all positions will be closed. 

The strategy provides two stop loss methods, either one or both can be used:

1. Percentage stop loss: Users can set the maximum percentage loss allowed for each position. If the price drops below this percentage stop loss level, the position will be closed.

2. Breakout stop loss: Record the lowest point of the candlestick when opening the position. If the price then drops below this point later, close the position.

### Advantage Analysis 

This strategy has the following advantages:

1. Uses a custom indicator to identify market trends, which is more sensitive and accurate.

2. Only goes long, avoiding the unlimited loss risk of short selling.

3. Adopts the idea of trend trading, which is a classic trend following approach.

4. Provides dual stop loss methods, allowing free choice of the more suitable stop loss mode.

5. Simple and clear code, easy to understand and modify.

6. No need to set dynamic take profit, avoiding premature profit taking leading to lost profits.

### Risk Analysis

This strategy also has some risks:

1. Custom indicators may not be stable and reliable, with the risk of misjudgement. 

2. Only establishing long positions may miss short-term pullback shorting opportunities.

3. Stop loss settings may be too conservative, unable to hold longer trending positions.

4. Lack of dynamic take profit requires timely manual profit taking, with operational risks.

5. Although both stop loss methods can be freely combined, the optimal stop loss point may still not be found.

6. Trend chasing strategies are prone to be misguided by ranging markets, producing excessive invalid trades.

### Optimization Directions

This strategy can be optimized from the following aspects:

1. Try other indicators, such as KDJ, MACD etc, to find more stable and reliable trend identification methods.

2. Increase shorting opportunities by allowing short positions when trends reverse, improving strategy profitability. 

3. Optimize stop loss strategies by testing different parameters to find better stop loss points, or use ATR, MA etc to set dynamic stops.

4. Add dynamic take profit, such as setting profit taking after breaking previous highs, reducing manual operation risks.

5. Conduct parameter optimization by adjusting MA periods, entry conditions etc to find optimal parameter combinations.

6. Add filtering conditions like Only Long or bottom indicators to avoid invalid trades.

7. Test on different products to evaluate strategy effectiveness across major coin pairs and optimize applicability.

8. Utilize backtesting and demo trading to optimize parameters and stop loss/take profit points.

### Summary 

Overall this is a relatively simple trend chasing strategy. It uses a custom momentum indicator to judge market trends, establishes long positions at the start of trends, and provides dual stop loss methods. The main advantages are a clear strategy logic, limited risks, and ease of operation. But there is also room for optimization in areas like stop loss strategies and parameter selection. In general, this strategy provides a fundamental trend trading idea for the Cryptocurrency market, and is very suitable for beginners to learn and practice. But sufficient backtesting should still be conducted to validate its effectiveness and optimize further before applying it in live trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|3|multiplier|
|v_input_2|100|length|
|v_input_3|100|Stop loss, %|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-19 00:00:00
end: 2023-04-13 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
strategy("[BoTo] Pump&Dump Strategy", shorttitle = "[BoTo] P&D Strategy", default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 0)

//Settings
multiplier = input(3.0)
length = input(100)
stop = input(100.0, title = "Stop loss, %")

//Indicator
body = abs(close - open)
sma = sma(body, length) * multiplier
plot(body, color = gray, linewidth = 1, transp = 0, title = "Body")
plot(sma, color = gray, style = area, linewidth = 0, transp = 90, title = "Avg.body * Multiplier")

//Signals
pump = body > sma and close > open
dump = body > sma and close < open
color = pump ? green : dump ? red : na
bgcolor(color, transp = 0)

//Stops
size = strategy.position_size
autostop = 0.0
autostop := pump and size == 0 ? low : autostop[1]
userstop = 0.0
userstop := pump and size == 0 ? close - (close / 100 * stop) : userstop[1]

//Strategy
if pump
    strategy.entry("Pump", strategy.long)
if dump or low < autostop or low < userstop
    strategy.close_all()
```

> Detail

https://www.fmz.com/strategy/430280

> Last Modified

2023-10-26 17:23:20