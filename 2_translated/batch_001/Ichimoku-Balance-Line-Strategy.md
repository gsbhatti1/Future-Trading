> Name

One-Goal Balance Line Strategy Ichimoku-Balance-Line-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13099eb28f322da696f.png)
[trans]

## Overview  

The One-Goal Balance Line strategy is a trend-following strategy that determines trend direction by calculating moving averages combined with the Ichimoku Kinko Hyo indicator for low-risk trend trading.

## Strategy Principle   

The strategy mainly uses the Ichimoku Kinko Hyo indicator to determine the trend direction. Ichimoku Kinko Hyo, also known as "Ichimoku Cloud," consists of the Tenkan-sen (Conversion Line), Kijun-sen (Base Line), Senkou Span A (Leading Span A), and Senkou Span B (Leading Span B). It forms an equilibrium zone between the front and back called the "Kumo Cloud." When price is above the cloud, it signals an upward trend. A breach below the cloud signals a downward trend.

The strategy combines the price relationship with moving averages to determine the trend direction. It generates a buy signal when the price crosses above the Base Line and Conversion Line. A sell signal is generated when the price breaks below the cloud. This combination helps to filter false breakouts and lock in the trend direction.

## Advantage Analysis  

- Uses Ichimoku Kinko Hyo to determine the trend and avoid false breakouts in ranging markets  
- Customizable moving average parameters for optimization across periods   
- Combination with moving averages helps to effectively lock in trend direction  
- Cloud bands allow low-risk trend trading  

## Risk Analysis   

- Prone to generating false signals in choppy market conditions
- Improper parameter settings may lead to overly frequent or delayed trade signals  
- Manual judgement of trend direction and parameter adjustment required  

## Optimization Directions  

The strategy can be optimized in several ways:  

1. Optimize Ichimoku parameters to suit more timeframes  
2. Incorporate stop loss to limit losses per trade
3. Add indicators to gauge strong and weak trends to avoid whipsaws   
4. Add more entry conditions to avoid opening positions in extreme market conditions  

## Conclusion   

In conclusion, the One-Goal Balance Line Strategy uses the Ichimoku Cloud to determine trend direction, locks in trends effectively, and generates trade signals by combining price relationship with moving averages, allowing low-risk trend trading. The strategy can be adapted to different market environments through parameter tuning and optimizations, making it worthwhile for investors to research and utilize.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2016|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2019|Backtest Stop Year|
|v_input_5|12|Backtest Stop Month|
|v_input_6|31|Backtest Stop Day|
|v_input_7|18|Tenkan|
|v_input_8|60|Kijun|
|v_input_9|30|Senkou B|
|v_input_10|52|Senkou A|
|v_input_11|52|Span Offset|
|v_input_12|true|Show Tenkan|
|v_input_13|true|Show Kijun|
|v_input_14|true|Show Span A|
|v_input_15|true|Show Span B|
|v_input_16|true|Show Chikou|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-12-19 00:00:00
end: 2023-12-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
// Credit for the initial code to nathanhoffer - I simply added the ability to select a time period
//
strategy("Cloud Breakout", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.0)

/////////////// Component Code Start ///////////////
testStartYear = input(2016, "Backtest Start Year") 
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay, 0, 0)

testStopYear = input(2019, "Backtest Stop Year")
testStopMonth = input(12, "Backtest Stop Month")
testStopDay = input(31, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay, 0, 0)

testPeriod() => true

Ten = input(18, minval=1, title="Tenkan")
Kij = input(60, minval=1, title="Kijun")
LeadSpan = input(30, minval=1, title="Senkou B")
Displace = input(52, minval=1, title="Senkou A")
SpanOffset = input(52, minval=1, title="Span Offset")

sts = input(true, title="Show Tenkan")
sks = input(true, title="Show Kijun")
ssa = input(true, title="Show Span A")
ssb = input(true, title="Show Span B")
sc = input(true, title="Show Chikou")

source = close

//Script for Ichimoku Indicator
donchian(len) => avg(lowest(len), highest(len))
TS = donchian(Ten)
KS = donchian(Kij)
SpanA = avg(TS, KS)
SpanB = donchian(LeadSpan)

CloudTop = max(TS, KS)

Chikou = source[Displace]
SpanAA = avg(TS, KS)[SpanOffset]
SpanBB = donchian(LeadSpan)[SpanOffset]

//Kumo Breakout (Long)
SpanA_Top = SpanAA >= SpanBB ? 1 : 0
SpanB_Top = SpanBB >= SpanAA ? 1 : 0

SpanA_Top2 = SpanA >= SpanB ? 1 : 0
SpanB_Top2 = SpanB >= SpanA ? 1 : 0

Spa
```