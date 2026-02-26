> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|FromMonth|
|v_input_2|true|FromDay|
|v_input_3|2017|FromYear|
|v_input_4|true|ToMonth|
|v_input_5|true|ToDay|
|v_input_6|9999|ToYear|
|v_input_7|true|Enable EMA?|
|v_input_8|false|Enable Stochastik RSI?|
|v_input_9|24|EMA 1|
|v_input_10|90|EMA 2|
|v_input_11|3|RSI K Line|
|v_input_12|3|RSI D Line|
|v_input_13|14|RSI Length|
|v_input_14|14|Stochastik Length|
|v_input_15_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_16|9|Ichi Conversion Line Length|
|v_input_17|26|Ichi Base Line Length|
|v_input_18|52|Ichi Lagging Span 2 Length|
|v_input_19|true|Ichi Displacement|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-17 00:00:00
end: 2023-11-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title="Ichimoku only Long Strategy", shorttitle="Ichimoku only Long", overlay = true, pyramiding = 0, calc_on_order_fills = false, commission_type =  strategy.commission.percent, commission_value = 0, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, initial_capital=10000, currency=currency.USD)

// Time Range
FromMonth=input(defval=1,title="FromMonth",minval=1,maxval=12)
FromDay=input(defval=1,title="FromDay",minval=1,maxval=31)
FromYear=input(defval=2017,title="FromYear",minval=2017)
ToMonth=input(defval=1,title="ToMonth",minval=1,maxval=12)
ToDay=input(defval=1,title="ToDay",minval=1,maxval=31)
ToYear=input(defval=9999,title="ToYear",minval=2017)
start=timestamp(FromYear,FromMonth,FromDay,00,00)
finish=timestamp(ToYear,ToMonth,ToDay,23,59)
window()=>true
// See if this bar's time happened on/after start date
afterStartDate = time >= start and time<=finish?true:false

//Enable RSI
enableema = input(true, title="Enable EMA?")
enablestochrsi = input(false, title="Enable Stochastic RSI?")
```