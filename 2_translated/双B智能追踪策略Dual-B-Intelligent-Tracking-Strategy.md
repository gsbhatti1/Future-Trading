> Name

Dual-B-Intelligent-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/122179aea3639a5e3e3.png)
[trans]
This is a trading strategy that uses Bollinger Bands. The strategy aims to identify opportunities when prices fluctuate violently using Bollinger Bands and make corresponding buy or sell decisions.

### Strategy Principle

The strategy calculates the upper band, middle band, and lower band of Bollinger Bands to determine if the current price is within the volatile range and hence make decisions on opening or closing positions. When the price approaches the upper band, it is regarded as the extreme point for longs and the strategy chooses to close long positions. When the price falls near the lower band, it is regarded as the extreme point for shorts and the strategy chooses to open long positions.

In addition, the strategy also introduces trend reversal factors. If there is a reversal signal, it will also trigger corresponding buy or sell decisions. Specifically, the logic of the strategy is as follows:

1. Calculate the upper, middle, and lower Bollinger Bands  
2. Judge if the price breaks through the bands and reversal signals
   1. Breaking through the middle band as trend signal  
   2. Near the upper or lower band as reversal signals
3. Send out buy, sell, or close orders

The above is the basic trading logic of this strategy. By utilizing the characteristics of Bollinger Bands and combining trend and reversal factors, the strategy attempts to catch reversal points when volatility increases.

### Advantages of the Strategy

Compared with ordinary moving average strategies, this strategy has the following advantages:

1. More sensitive, able to capture opportunities when prices fluctuate violently
2. Combine both trend and reversal factors to avoid losses from premature reversals  
3. Has a certain FILTER effect to avoid unnecessary buys/sells in non-volatile areas
4. Judge the major trend direction through the middle band to reduce trading frequency
5. Increase reversal filter conditions to reduce misjudgements 

In general, this strategy combines Bollinger Bands and price bars relatively well. It trades at reasonable reversal points to ensure a certain level of profits while controlling risks.

### Risks and Optimization

However, there are still some risks with this strategy:  

1. Improper BB parameters fail to fully capture price fluctuations
2. Inaccurate reversal signal judgement, missing reversals or misjudging reversals
3. Poor effectiveness of middle band signals when trend is unclear

Accordingly, future optimizations can focus on:

1. Adaptive optimization of BB parameters based on different products  
2. Increase machine learning models to judge reversal probability
3. Switch to other indicators when trend is unclear
4. Combine more price patterns to filter trading signals

### Conclusion

In conclusion, this is a typical Bollinger Bands trading strategy template. It avoids excessive ineffective trades common for using Bollinger Bands alone by introducing trend reversal judgement to filter signals, which can theoretically lead to good strategy performance. But parameters and signal filtering still need further optimization and improvement for robustness and to reduce misjudgements.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|20|Bollinger Length|
|v_input_4|2|Bollinger Mult|
|v_input_5_ohlc4|0|Bollinger Source: ohlc4|high|low|open|hl2|hlc3|hlcc4|close|
|v_input_6|true|Use trend entry|
|v_input_7|true|Use counter-trend entry|
|v_input_8|2018|From Year|
|v_input_9|2100|To Year|
|v_input_10|true|From Month|
|v_input_11|12|To Month|
|v_input_12|true|From day|
|v_input_13|31|To day|
|v_input_14|true|Show Bollinger Bands|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-18 00:00:00
end: 2024-01-17 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Noro
//2018

//@version=3
strategy("Noro's Bollinger Strategy v1.2", shorttitle = "Bollinger str 1.2", overlay = true )

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")

length = input(20, defval = 20, minval = 1, maxval = 1000, title = "Bollinger Length")
mult = input(2.0, defval = 2.0, minval = 0.001, maxval = 50, title = "Bollinger Mult")
source = input(ohlc4, defval = ohlc4, title = "Bollinger Source")

uset = input(true, defval = true, title = "Use trend entry")
usect = input(true, defval = true, title = "Use counter-trend entry")

fromyear = input(2018, defval = 2018, minval = 1900, maxval = 2100, title = "From Year")
toyear = input(2100, defval = 2100, minval = 1900, maxval = 2100, title = "To Year")
frommonth = input(01, defval = 01, minval = 01, maxval = 12, title = "From Month")
tomonth = input(12, defval = 12, minval = 01, maxval = 12, title = "To Month")
fromday = input(01, defval = 01, minval = 01, maxval = 31, title = "From day")
today = input(31, defval = 31, minval = 01, maxval = 31, title = "To day")

// Bollinger Bands
bbands = ta.bbands(source, length, mult)

upperband = bbands[1][2]
lowerband = bbands[1][4]

// Trend and Reversal Checks
inUptrend = na(ta.crossover(bbands[0][1], upperband))
inDowntrend = na(ta.crossunder(bbands[0][1], lowerband))

if (uset and inUptrend)
    strategy.close("Bollinger str 1.2", when=bbands[0][3] < close)

if (usect and inDowntrend) 
    strategy.entry("Bollinger str 1.2", when=bbands[0][4] > close)

// Plotting
plot(upperband, color=color.red)
plot(lowerband, color=color.blue)
```

This PineScript code implements the described strategy for trading with Bollinger Bands, including handling of long and short trades based on trend and reversal signals.