<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Buying-Dips-MA200-Optimized-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/e3a972c0e317a95312.png)

[trans]

### Overview

This strategy combines a contrarian trading approach (buying dips) with trend-following logic (only when price is above MA200). It aims to identify the most favorable timing for purchasing asset lows to maximize profitability. A price above the long-term moving average enhances the likelihood of profiting from buying assets during temporary weakness.

### Strategy Logic  

The strategy determines whether the price is at a relative low by calculating the overall percentage change of price over a specified lookback period. When the overall percentage change is less than -3%, the price is considered to be at a dip. Additionally, a 200-day simple moving average is used as a trend indicator. Buy signals are only generated when the price is above the 200-day moving average. This way, the strategy leverages both mean reversion and momentum principles to buy dips during uptrends for profit.

### Advantages

This strategy merges the benefits of trend trading and contrarian trading. It uses a long-term moving average to identify trends, preventing blind purchases during downtrends. Meanwhile, buying dips allows for better entry points during short-term adjustments. This combination ensures trading safety while increasing the probability of profits. Furthermore, the strategy offers significant room for parameter optimization, making it adaptable to various markets.

### Risks  

The main risk is that after a buy signal is issued, the price might continue declining, expanding losses. Additionally, prolonged sideways markets where prices fail to breach the moving average can render the strategy ineffective. To mitigate these risks, consider shortening the moving average period and optimizing buy conditions to ensure adequate safety margins.

### Optimization Directions  

The strategy can be improved in several ways: 1) Optimize the moving average period for different markets; 2) Refine buy conditions to ensure sufficient margins; 3) Add stop-loss mechanisms to control losses; 4) Incorporate other indicators to enhance accuracy in identifying trends and dips.

### Conclusion  

Overall, this strategy represents a classic blend of trend-following and contrarian trading philosophies. It ensures trading security while enhancing profitability, offering strong practical value. With further parameter and stop-loss optimizations, its stability and effectiveness in live trading can be significantly enhanced.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|100|MA|
|v_input_2|true|Lookback Period|
|v_input_3|true|From Month|
|v_input_4|true|From Day|
|v_input_5|2020|From Year|
|v_input_6|true|Thru Month|
|v_input_7|true|Thru Day|
|v_input_8|2112|Thru Year|
|v_input_9|true|Show Date Range|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-08 00:00:00
end: 2024-01-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Buy The Dips - MA200 Optimised", overlay=false)

//Moving average
MAinp = input(defval = 100, title = "MA", type = input.integer, minval = 1, step = 1)
MA=sma(close, MAinp)

//Percent change
inp_lkb = input(1, title='Lookback Period')
 
perc_change(lkb) =>
    overall_change = ((close[0] - close[lkb]) / close[lkb]) * 100

// Call the function    
overall = perc_change(inp_lkb)

// === INPUT BACKTEST RANGE ===
fromMonth = input(defval = 1,    title = "From Month",      type = input.integer, minval = 1, maxval = 12)
fromDay   = input(defval = 1,    title = "From Day",        type = input.integer, minval = 1, maxval = 31)
fromYear  = input(defval = 2020, title = "From Year",       type = input.integer, minval = 1970)
thruMonth = input(defval = 1,    title = "Thru Month",      type = input.integer, minval = 1, maxval = 12)
thruDay   = input(defval = 1,    title = "Thru Day",        type = input.integer, minval = 1, maxval = 31)
thruYear  = input(defval = 2112, title = "Thru Year",       type = input.integer, minval = 1970)

showDate  = input(defval = true, title = "Show Date Range", type = input.bool)

start     = timestamp(fromYear, fromMonth, fromDay, 00, 00)        // backtest start window
finish    = timestamp(thruYear, thruMonth, thruDay, 23, 59)        // backtest finish window
window()  => true       // create function "within window of time"

//Entry/Exit
strategy.entry(id="long", long = true, when = window() and overall<-3 and close > MA) 
strategy.close(id="long", when = window() and overall>1)


bgcolor(color = showDate and window() ? color.gray : na, transp = 90) 
plot(overall, color=color.black, title='Overall Percentage Change', linewidth=3)
band1 = hline(1, "Upper Band", color=#C0C0C0)
band0 = hline(-2, "Lower Band", color=#C0C0C0)
fill(band1, band0, color=#9915FF, transp=90, title="Background")
hline(0, title='Center Line', color=color.orange, linestyle=hline.style_solid, linewidth=2)
```

> Detail

https://www.fmz.com/strategy/438063

> Last Modified

2024-01-08 16:54:21