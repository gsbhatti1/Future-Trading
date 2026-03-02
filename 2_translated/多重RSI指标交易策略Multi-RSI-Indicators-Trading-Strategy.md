> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|100|Lot, %|
|v_input_2|true|Use RSI 1|
|v_input_3|4|RSI 1 Period|
|v_input_4|20|RSI 1 Limit|
|v_input_5|true|Use RSI 2|
|v_input_6|7|RSI 2 Period|
|v_input_7|25|RSI 2 Limit|
|v_input_8|true|Use RSI 3|
|v_input_9|14|RSI 3 Period|
|v_input_10|30|RSI 3 Limit|
|v_input_11|false|Use RSI 4|
|v_input_12|21|RSI 4 Period|
|v_input_13|35|RSI 4 Limit|
|v_input_14|false|Use RSI 5|
|v_input_15|28|RSI 5 Period|
|v_input_16|40|RSI 5 Limit|
|v_input_17|false|Use color filter|
|v_input_18|1900|From Year|
|v_input_19|2100|To Year|
|v_input_20|true|From Month|
|v_input_21|12|To Month|
|v_input_22|true|From Day|
|v_input_23|31|To Day|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-21 00:00:00
end: 2023-11-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Noro
// 2018
//@version=2

strategy(title = "Noro's Symphony Strategy v1.1", shorttitle = "Symphony str 1.1", overlay = false, default_qty_type = strategy.percent_of_equity, default_qty_value = v_input_1, pyramiding = 20)

// Settings

// needlong = input(true, defval = true, title = "Long")
// needshort = input(true, defval = true, title = "Short")

capital = input(v_input_1, defval = v_input_1, minval = 1, maxval = 10000, title = "Lot, %")
usersi1 = input(v_input_2, defval = v_input_2, title = "Use RSI 1")
rsiperiod1 = input(v_input_3, defval = v_input_3, minval = 2, maxval = 100, title = "RSI 1 Period")
rsilimit1 = input(v_input_4, defval = v_input_4, minval = 2, maxval = 50, title = "RSI 1 Limit")
usersi2 = input(v_input_5, defval = v_input_5, title = "Use RSI 2")
rsiperiod2 = input(v_input_6, defval = v_input_6, minval = 2, maxval = 100, title = "RSI 2 Period")
rsilimit2 = input(v_input_7, defval = v_input_7, minval = 2, maxval = 50, title = "RSI 2 Limit")
usersi3 = input(v_input_8, defval = v_input_8, title = "Use RSI 3")
rsiperiod3 = input(v_input_9, defval = v_input_9, minval = 2, maxval = 100, title = "RSI 3 Period")
rsilimit3 = input(v_input_10, defval = v_input_10, minval = 2, maxval = 50, title = "RSI 3 Limit")
usersi4 = input(v_input_11, defval = v_input_11, title = "Use RSI 4")
rsiperiod4 = input(v_input_12, defval = v_input_12, minval = 2, maxval = 100, title = "RSI 4 Period")
rsilimit4 = input(v_input_13, defval = v_input_13, minval = 2, maxval = 50, title = "RSI 4 Limit")
usersi5 = input(v_input_14, defval = v_input_14, title = "Use RSI 5")
rsiperiod5 = input(v_input_15, defval = v_input_15, minval = 2, maxval = 100, title = "RSI 5 Period")
rsilimit5 = input(v_input_16, defval = v_input_16, minval = 2, maxval = 50, title = "RSI 5 Limit")
cf = input(v_input_17, defval = v_input_17, 
```