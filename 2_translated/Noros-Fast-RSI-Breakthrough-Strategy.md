This article will detail the logic behind Noro's Fast RSI Breakthrough Strategy, explain how trading signals are generated, and analyze the advantages and potential risks of this strategy.

---

**I. Strategy Overview**

This strategy mainly uses the RSI indicator to generate trading signals, combined with candlestick filtering and min/max breakthroughs as auxiliary judgments, forming a complete long/short decision system. The strategy name is "Noro's Fast RSI Breakthrough Strategy".

**II. Strategy Details**

1. **Fast RSI Setting**
   - The strategy uses a length 7 fast RSI to capture signs of market trends through fast RSI oscillations.
   - Upper and lower limits of 70 and 30 are also set for the RSI, triggering signals when breached.

2. **Candlestick Filtering**
   - The strategy filters RSI signals using the candlestick body size SMA, only considering RSI signals on candlesticks with a body size larger than 5-day average body size to avoid whipsaws in volatile markets.

3. **Min/Max Breakthroughs**
   - The strategy checks if min/max breakthroughs happened within recent mmbars, combined with RSI level to determine bottom reversals and top breakdowns.

4. **Trading Signal Summary**
   - **Long Signal:** RSI crosses below 30, body size exceeds average body size, and min breaks supports.
   - **Short Signal:** RSI crosses above 70, body size exceeds average body size, and max breaks resistances.
   - **Exit Signal:** When RSI recrosses limits in the opposite direction of the position.

**III. Advantages of the Strategy**

1. Optimized RSI parameters capture trend change quickly.
2. Combining with candlesticks and min/max prevents unnecessary whipsaws.
3. Stop loss mechanism exits when RSI recrosses limits.

**IV. Risks of the Strategy**

1. RSI prone to false signals, needs auxiliary confirmation.
2. Backtest overfitting risks; optimized parameters may only fit specific market periods.
3. Stop loss mechanism may be too mechanical, unable to control large loss on single stop loss.

**V. Conclusion**

This strategy integrates multiple technical indicators for robust trend following but notes the risks of backtest overfitting and stop loss mechanisms. Live performance should be evaluated cautiously, with fine-tuning of parameters and control of position sizing recommended for live trading.

---

**Strategy Arguments**

|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|true|Use Fast RSI Strategy|
|v_input_4|true|Use Min/Max Strategy|
|v_input_5|true|Use BarColor Strategy|
|v_input_6|false|Use SMA Filter|
|v_input_7|20|SMA Filter Period|
|v_input_8|7|Fast RSI Period|
|v_input_9|30|RSI limit|
|v_input_10_close|0|RSI Price: close, high, low, open, hl2, hlc3, hlcc4, ohlc4|
|v_input_11|true|RSI Bars|
|v_input_12|true|Min/Max Bars|
|v_input_13|false|Show SMA Filter|
|v_input_14|false|Show Arrows|
|v_input_15|2018|From Year|
|v_input_16|2100|To Year|
|v_input_17|true|From Month|
|v_input_18|12|To Month|
|v_input_19|true|From day|
|v_input_20|31|To day|

---

**Source (PineScript)**

```pinescript
// backtest
// start: 2022-09-11 00:00:00
// end: 2023-01-11 00:00:00
// period: 1d
// basePeriod: 1h
// exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]

//@version=3
strategy(title = "Noro's Fast RSI Strategy v1.6", shorttitle = "Fast RSI str 1.6", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, pyramiding = 10)

// Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
usersi = input(true, defval = true, title = "Use Fast RSI Strategy")
usemm = input(true, defval = true, title = "Use Min/Max Strategy")
usebc = input(true, defval = true, title = "Use BarColor Strategy")
usesma = input(false, defval = false, title = "Use SMA Filter")
smaperiod = input(20, defval = 20, minval = 2, maxval = 1000, title = "SMA Filter Period")
fast = input(7, defval = 7, minval = 2, maxval = 50, title = "Fast RSI Period")
limit = input(30, defval = 30, minval = 1, maxval = 100, title = "RSI limit")
rsisrc = input(close, defval = close, title = "RSI Price")
rsibars = input(1, defval = 1, minval = 1, maxval = 20, title = "RSI Bars")
mmbars = input(1, defval = 1, minval = 1, maxval = 5, title = "Min/Max Bars")
showsma = input(false, defval = false, title = "Show SMA Filter")
showarr = input(false, defval = false, title = "Show Arrows")
fromyear = input(2018, defval = 2018, minval = 1900, maxval = 2100, title = "From Year")
toyear = input(2100, defval = 2100, minval = 1900, maxval = 2100, title = "To Year")
frommonth = input(01, defval = 01, minval = 01, maxval = 12, title = "From Month")
tomonth = input(12, defval = 12, minval = 01, maxval = 12, title = "To Month")
fromday = input(01, defval = 01, minval = 01, maxval = 31, title = "From day")
today = input(31, defval = 31, minval = 01, maxval = 31, title = "To day")

// Fast RSI
fastup = rma(max(change(rsisrc), 0), fast)
fastdown = rma(-min(change(rsisrc), 0), fast)
fastrsi = fastdown == 0 ? 100 : fastup == 0 ? 0 : 100 - (100 / (1 + fastup / fastdown
```