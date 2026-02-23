> Name

Brrrrr-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]
The stock "Brrrrr" strategy is a trading strategy based on monitoring changes in the issuance of stablecoins and achieving profits by going long and short on cryptocurrency. The name of this strategy comes from "Brrrrr" (the sound of a printer operating), which is intended to express that the strategy's operating principle is to judge the price changes of cryptocurrency by tracking the printing of stable coins.

The basic principle of this strategy is: when stablecoins are issued, the price of Bitcoin rises; when stablecoins are recycled and burned, the price of Bitcoin falls. Based on this principle, we can go long Bitcoin when the stablecoin is issued, close the position when the stablecoin is recycled and burned, or directly short Bitcoin.

In order to filter out too many invalid signals, this strategy uses Donchian channel technology. The long signal is triggered only when the stablecoin issuance exceeds the highest value in the recent 50 days. Only when the stablecoin issuance is lower than the lowest value in the recent 50 days, the closing or shorting signal will be triggered.

The advantage of this strategy is that it captures the market law of the impact of stablecoin issuance on cryptocurrency prices, filters out some noise through technical indicators, and can provide more accurate trading signals at major trend turning points. However, this strategy is only based on a single variable, and the issuance and shrinkage of stablecoins are difficult to predict, so there are certain immediate risks.

Overall, the stock "Brrrrr" strategy is an interesting trading strategy based on monitoring stablecoin issuance and deserves further testing and optimization, but traders need to be cautious and not put all their money on it. The effectiveness of this strategy may be further enhanced by combining various other variables and technical indicators.
[/trans]

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Use short|
|v_input_int_1|50|len|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-13 00:00:00
end: 2023-09-12 00:00:00
Period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title = "Brrrrr strategy", shorttitle = "Brrrrr", overlay = false, default_qty_type = strategy.percent_of_equity, initial_capital = 100, default_qty_value = 100, commission_type = strategy.commission.percent, commission_value = 0.1)

//Settings
short = input(true, title = "Use short")
len = input.int(50, minval = 1, maxval = 1000)

//BRRRRR (USDT Printing)
brrrrr = request.security("GLASSNODE:USDT_SUPPLY", "D", close)

//Donchian channel
h = ta.highest(brrrrr, len)
l = ta.lowest(brrrrr, len)

//Lines
plot(h, color = color.lime)
plot(brrrrr)
plot(l, color = color.red)

//Trading
if brrrrr > h[1]
strategy.entry("Long", strategy.long)
if brrrrr < l[1]
if short
strategy.entry("Short", strategy.short)
if short == false
strategy.close_all()

```

> Detail

https://www.fmz.com/strategy/426582

> Last Modified

2023-09-13 14:53:16