``` pinescript
/*backtest
start: 2022-04-25 00:00:00
end: 2022-05-24 23:59:00
period: 15m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// 2020 © io72signals / Antorio Bergasdito

//@version=4
study("72s: Adaptive Hull Moving Average+", shorttitle="72s: Adaptive HMA+", overlay=true)

//Optional Inputs
charger     = input("Volatility", title="Choose which charger to adapt to:", options=["Volatility", "Volume"])
src         = input(close, title="Source:")
minLength   = input(172, title="Minimum period:")
maxLength   = input(233, title="Maximum period:")
adaptPct    = 0.03141
```

> Name

72s-Adaptive-Hull-Moving-Average

> Author

ChaoZhang

> Strategy Description

One challenging issue for beginner traders is to differentiate market conditions, whether or not the current market is giving best possibility to stack profits, as earliest, in shortest time possible, or not.

On intraday, we've seen some big actions by big banks are somewhat can be defined --or circling around-- by HMA 200. I've been thinking on to make the visuals more conform to price dynamics (separating major movement and minor noise) to get clearer signs of when it starts to happen. So it will be easier to see in a glance when the strength starts really taken place, with less cluttered chart.

This Adaptive HMA is using the new Pine Script's feature which now support Dynamic Length arguments for several Pine functions. ( read: [https://www.tradingview.com/blog/en/pine-script-dynamic-length-arguments/](https://www.tradingview.com/blog/en/pine-script-dynamic-length-arguments/) ). It hasn't support the built-in HMA() directly, but thankfully we can use its wma() formula to construct. (Note: I tweaked a bit HMA formula already popular here by using plain int() instead of round() on its wma's length, since I find it precisely match tradingview's built-in HMA).

You can choose which aspect the Adaptive HMA period will adapt to.

In this study I present it with two options: Volume and Volatility. It will "moves" faster or slower depends on which situation the aspect is currently into. ie: When volume is generally low or volatile readings are not there, price won't move very much, so the adapting MA will slow down by dynamically lengthening the lookback period, and vice versa, and so on.

Colour-markings in the Adaptive HMA resemble which situation explained above. In addition, I also combine it with slope calculation of the MA to help measuring trend-strength or sideways/choppy conditions.

This way when we use it as dynamic support/resistance it will be more visually-reliable.

Secondly, and more important, it might help us traders with better probability info of whether or not a trade should even worth making. ie: If in the meantime market won't give much movement, any profit would also only as much. In most cases, we might better save our dime for later or place it somewhere else.

**How to Use:**
Aside from better dynamic support/resistance and clearer breakout confirmation, MA is colored as follow:
- **Yellow**: Market is in consolidation or flat. Be it sideways, choppy, or in relatively small movements. If it shows up in a trending market, it may be an earlier sign that the current trend might about to change its direction, or confirming a price broke-out to another side.
- **Light Green or Light Red**: Tells if a trend is forming but still relatively weak (or getting weaker), as it doesn't have volume or volatility to support.
- **Dark Green or Dark Red**: This is where we can expect some good and strong price movement to ride. If it's strong enough, many times it marks the start of a new long-lasting major trend.

**Settings:**
- Charger:
  Choose which aspect your HMA should plug itself into, thus it will adapt to it.
- Minimum Period, Maximum Period:
  172 - 233 is just my own setting to outmatch the static HMA 200 for intraday. I find it --in my style of trading-- best in 15m tf in almost any pair, and 15m to 1H for some stocks. It also works nicely with conventional EMA 200, sometimes as if they somewhat work hand-in-hand in defining where the price should go. But you can, of course, experiment with other ranges, broader or narrower. Especially if you already have an established strategy to follow.
- Consolidation Area Threshold:
  This has to do with slope calculation. The bigger the number means your MA needs a bigger degree to define the market is out of flat (yellow) area. This can be useful if needed to lighten up the filter or vice-versa.
- Background Coloring:
  Just another coloring to help highlighting the difference in market conditions.

**Alerts:**
There are two alerts:
- **Volume Break**: when volume is breaking up above average,
- **Volatility Meter**: when the market more likely is about to have its moment of the big wiggling brush.

**Usage:**
Very very nice BUY entry to catch big up-movement if:
1. Price is above MA. (It is best when price is also not too far distance from the MA, or you can also use distance oscillator to help out too)
2. HMA's color is in darker green. Means it's on the charging plug with your chosen aspect.
3. RSI is above 50. This is to help as additional confirmation.

Clear SELL entry signal is same as above, just the opposite.


**Backtest**
![IMG](https://www.fmz.com/upload/asset/c26d83c2b416482e2d.png)