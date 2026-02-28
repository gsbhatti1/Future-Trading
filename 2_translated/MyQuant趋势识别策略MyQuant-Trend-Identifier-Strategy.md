> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|2020|start year|
|v_input_int_2|true|start month|
|v_input_int_3|true|start day|
|v_input_int_4|2025|end year|
|v_input_int_5|true|end month|
|v_input_int_6|true|end day|
|v_input_1|false|Choose Time Interval|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-02-15 00:00:00
end: 2024-02-21 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © spacekadet17
// 
//@version=5

strategy(title="Trend Identifier Strategy", shorttitle="Trend Identifier Strategy", format=format.price, precision=4, overlay = false, initial_capital = 1000, pyramiding = 10, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, commission_type = strategy.commission.percent, commission_value = 0.03)

//start-end time
startyear = input.int(2020,"start year")
startmonth = input.int(1,"start month")
startday = input.int(1,"start day")
endyear = input.int(2025,"end year")
endmonth = input.int(1,"end month")
endday = input.int(1,"end day")

timeEnd = time <= timestamp(syminfo.timezone,endyear,endmonth,endday,0,0)
timeStart = time >= timestamp(syminfo.timezone,startyear,startmonth,startday,0,0)
choosetime = input(false,"Choose Time Interval")
condTime = (choosetime ? (timeStart and timeEnd) : true)

// time frame?
tfc = 1
if timeframe.isdaily
```