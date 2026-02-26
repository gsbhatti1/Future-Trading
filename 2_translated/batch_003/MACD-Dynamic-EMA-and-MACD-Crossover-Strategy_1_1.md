> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|3|fastLength|
|v_input_2|11|slowlength|
|v_input_3|27|MACDLength|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-29 00:00:00
end: 2024-02-05 00:00:00
period: 15m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("MACD+EMA crossovers Strategy custom", initial_capital=10000, max_bars_back=150, commission_type=strategy.commission.percent, commission_value=0.1, shorttitle="MACD+EMAcross", pyramiding = 10, default_qty_type=strategy.percent_of_equity, default_qty_value=33, overlay=false)

short = ema(close, v_input_1)
long = ema(close, v_input_2)
long2 = ema(close, v_input_3)
//plot(short, color = red, linewidth = 4)
//plot(long, color = blue, linewidth = 4)
//plot(long2, color = green, linewidth = 4)

isCross1 = crossover(short, long)
isCross2 = crossover(short, long2)
isCrossSell = crossunder(short, long)
//isCross3 = crossover(long, long2)

if (isCross1)
    strategy.entry("Long1", strategy.long)
if (isCross2)
    strategy.entry("Long2", strategy.long)
if (isCrossSell)
    strategy.close("Long1")
```

This PineScript defines a trading strategy based on the dynamic combination of EMA and MACD crossovers. The script uses `v_input_1`, `v_input_2`, and `v_input_3` for the EMA lengths, which are set to default values of 3, 11, and 27 respectively. It also includes logic to handle entry and exit based on these conditions.