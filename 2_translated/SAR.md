---
Name

SAR Parabolic Steering Indicator

Author

Taofen Quantification

Strategy Description

This strategy is modified based on "One Moving Average Trend Demo" by Fengdouzi (https://www.fmz.com/strategy/193609),
Using the signal of the Parabolic SAR as a buying and selling point is a digital currency futures trend strategy.

The drawing code uses Zero's "Line Drawing Library" (https://www.fmz.com/strategy/27293).
Refer to Xiaoxiaomeng's "Example of Drawing K-Line and Moving Average Charts Using Line Drawing Library" (https://www.fmz.com/strategy/125770).

———— Taofen Quantification (WeChat: himandy)

=====I am the low-key dividing line======

A good trading platform can make your strategy skyrocket. If you register through the link, you can get a VIP5 handling fee discount for two months:
(Spot: 0% for pending orders, 0.07% for takers. Contract: 0% for pending orders, 0.04% for takers)
https://www.kucoin.center/ucenter/signup?rcode=1wxJ2fQ&lang=zh_CN&utmsource=VIP_TF

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|Amount|100|Amount|
|time_interval|3600|Customized K-line period (seconds)|


> Source (javascript)

``` javascript
/*backtest
start: 2017-11-01 00:00:00
end: 2020-09-01 00:00:00
Period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_BitMEX","currency":"XBT_USD"}]
args: [["Amount",10000],["time_interval",86400]]
*/

/*
This strategy is modified based on "One Moving Average Trend Demo" (https://www.fmz.com/strategy/193609) by Fengdouzi. It uses the signal of the parabolic turning indicator SAR as the buying and selling point. It is a digital currency futures trend strategy.

The drawing code uses Zero's "Line Drawing Library" (https://www.fmz.com/strategy/27293), and refers to Xiaoxiaomeng's "Example of Drawing K-Line and Moving Average Charts Using Line Drawing Library" (https://www.fmz.com/strategy/125770).

———— Taofen Quantification (WeChat: himandy)
*/

// define object

//for backtesting
if (IsVirtual) {
if (exchange.GetCurrency() == "BTC_USD") {
exchange.SetContractType("quarter"); //Select a contract
} else if (exchange.GetCurrency() == "XBT_USD") {
exchange.SetContractType("XBTUSD"); //Facilitates strategy selection for BitMEX backtesting
}
}

exchange.SetMarginLevel(1)

varLastBarTime = 0,
Idle = -1,
status = Idle;

var preAccount, account, records, ticker, balance, Bar;
var sar, isFirst, PreBarTime, preTime;

// Link to the exchange and obtain relevant information
function UpdateInfo() {
account = exchange.GetAccount()
records = exchange.GetRecords(time_interval)
ticker = exchange.GetTicker()
//balance = account.Stocks
//Bar = records[records.length - 1]
}

//Indicator calculation and acquisition
function Get_SAR() {
sar = talib.SAR(records, 0.02, 0.2);
}

// Rules for opening and closing positions
function onTick() {

ticker = exchange.GetTicker()
if (status === Idle) {
if (ticker.Last > sar[sar.length - 1]) {
exchange.SetDirection("buy")
exchange.Buy(ticker.Sell, Amount)
status = PD_LONG
$.PlotFlag(new Date().getTime(), 'Buy', 'BK');
} else if (ticker.Last < sar[sar.length - 1]) {
exchange.SetDirection("sell")
exchange.Sell(ticker.Buy, Amount)
status = PD_SHORT
$.PlotFlag(new Date().getTime(), 'Sell', 'SK');
}
} else if (status === PD_LONG) {
if (ticker.Last < sar[sar.length - 1]) {
exchange.SetDirection("closebuy")
exchange.Sell(ticker.Buy, Amount)
account = exchange.GetAccount()
status=Idle
$.PlotFlag(new Date().getTime(), 'CloseBuy', 'SP');
}
} else if (status === PD_SHORT) {
if (ticker.Last > sar[sar.length - 1]) {
exchange.SetDirection("closesell")
exchange.Buy(ticker.Sell, Amount)
account = exchange.GetAccount()
status=Idle
$.PlotFlag(new Date().getTime(), 'CloseSell', 'BP');
}
}

}

function PlotMA_Kline(records, isFirst) {

$.PlotRecords(records, "BTC")
if (isFirst) {
for (var i = records.length - 1; i >= 0; i--) {
if (sar[i] !== null) {
$.PlotLine("SAR", sar[i], records[i].Time);
}
}
PreBarTime = records[records.length - 1].Time;
} else {
if (PreBarTime !== records[records.length - 1].Time) {
$.PlotLine('SAR', sar[sar.length - 2], records[records.length - 2].Time);
PreBarTime = records[records.length - 1].Time;
}
$.PlotLine('SAR', sar[sar.length - 1], records[records.length - 1].Time);
}
}

function main() {
preAccount = exchange.GetAccount()
// Link to the exchange and obtain relevant information
UpdateInfo()

// Main function, loop continuously
while (1) {
records = exchange.GetRecords(time_interval)
preTime = records[records.length - 1].Time
//The robot delays and waits until the next K-line cycle, the unit is milliseconds
while (new Date().getTime() < (preTime + time_interval * 1000)) { //Convert K-line period into milliseconds
records = exchange.GetRecords(time_interval)
//Indicator calculation and acquisition
Get_SAR()
// Rules for opening and closing positions
onTick()
//Poll sleep time
Sleep(5 * 1000)
}

//draw line
if (records) {
PlotMA_Kline(records, isFirst);
isFirst = false;
}

// print balance
LogProfit(account.Stocks - preAccount.Stocks, "&")

}
}
```

> Detail

https://www.fmz.com/strategy/224799

> Last Modified

2021-11-02 10:53:24