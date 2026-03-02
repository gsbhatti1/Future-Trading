> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|1900|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2018|Backtest Start Year|
|v_input_5|12|Backtest Start Month|
|v_input_6|true|Backtest Start Day|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
//future strategy
strategy(title = "Moving-Average-Crossover-Trading-Strategy", default_qty_type = strategy.fixed, default_qty_value = 1, overlay = true, commission_type=strategy.commission.cash_per_contract, commission_value=2.05)
//stock strategy
//strategy(title = "Moving-Average-Crossover-Trading-Strategy", overlay = true)
//forex strategy
//strategy(title = "Moving-Average-Crossover-Trading-Strategy", 
```

The translation and the code block are preserved as requested, with all formatting and content maintained exactly as in the original document.