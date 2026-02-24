> Name

Bybit-Jaw-Detection-VWAP-BTC

> Author

Flatbean

> Strategy Description

Here we start sharing the original version of the jaw detection strategy for Bybit.
Why is this the main reason? ///
 ![IMG](https://www.fmz.com/upload/asset/95a9985fc126e73d27e9.png) 
 
This is really frustrating...
You say it's open source, but I got upset when sold without knowing...
I hope you won't do this again.
Here we directly open-source it,
It's not a fancy strategy either...

Feel free to play around with it!
Don't buy my crappy code for money.
Just use it! Let's go!!

By the way, a little advertisement:
For more loss-making strategies, please follow our WeChat public account "Quantitative Log of Flatbean"
WX: wangxiaoba

(●'◡'●)

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|start_balance|false|Initial balance|
|long_qty|true|Long USD quantity per trade|
|short_qty|true|Short USD quantity per trade|
|maxPosition|500000|Maximum order volume|
|take_profit|45|Initial take profit (USD)|
|trailing_profit|true|Trailing take profit in USD|
|stop_loss|9|Stop loss percentage|
|long_vwap_offset|2.5|VWAP upper bound percentage|
|short_vwap_offset|2.5|VWAP lower bound percentage|
|GG|3|Leverage multiple (2x-7x recommended, higher leverage means greater risk)|
|stop_step|3600|Time to stop after stop loss in seconds|


> Source Code (JavaScript)

``` javascript
// User authentication based on UID permissions (UID list + getAccount uid validation)
function user_auth() {
    user_list = [775536, 783571, 789086, 819490, 1265698, 1294567, 1299150]
    user_id = account.Info.result[0].user_id
    //Log(user_id)
    if (user_list.indexOf(user_id) == -1) {
        throw new Error('User authentication error, please contact WeChat: wangxiaoba')
    }
}

// Calculate VWAP and its upper/lower bounds on Bybit
function VWAP() {
    // Define Kline and calculate VWAP
    if (records.length > 1440) {
        records.splice(0, 1);
    }
    var n = records.length - 1
    //Log(n)
    var total_sum = 0.0
    var volume_sum = 0
    vwap_arr = []
    vwap_up_arr = []
    vwap_dw_arr = []
    for (var i = 0; i < n + 1; i++) {
        var high_price = records[i].High
        //Log("log high_price " + high_price)
        var low_price = records[i].Low
        var close_price = records[i].Close
        //Log("log low_price " + low_price)
        var price = (high_price + low_price + close_price) / 3
        //Log("price", price)
        var volume = records[i].Volume
        //Log("log volume " + volume)
        total_sum += price * volume
        //Log("log total_sum " + total_sum)
        volume_sum += volume
        //Log("log volume_sum " + volume_sum)
        var re = total_sum / volume_sum
        var re_up = re * (1 + long_vwap_offset / 100)
        var re_dw = re * (1 - short_vwap_offset / 100)
        vwap_arr.push(re)
        vwap_up_arr.push(re_up)
        vwap_dw_arr.push(re_dw)
        //return total_sum / volume_sum
    }
    if (vwap_arr.length > 2000) {
        vwap_arr.splice(0, 1);
    }
    if (vwap_up_arr.length > 2000) {
        vwap_up_arr.splice(0, 1);
    }
    if (vwap_dw_arr.length > 2000) {
        vwap_dw_arr.splice(0, 1);
    }
    vwap = vwap_arr[vwap_arr.length - 1]
    vwap_up = vwap_up_arr[vwap_up_arr.length - 1]
    vwap_dw = vwap_dw_arr[vwap_dw_arr.length - 1]
    //Log("log vwap " + vwap, "log vwap_up " + vwap_up, "log vwap_dw " + vwap_dw)
}

// Plot lines
function PlotMA_Kline(records, isFirst) {
    $.PlotRecords(records, "K")
    if (isFirst) {
        for (var i = records.length - 1; i >= 0; i--) {
            if (vwap_arr[i] !== null) {
                $.PlotLine("vwap", vwap_arr[i], records[i].Time)
                $.PlotLine("vwap_up", vwap_up_arr[i], records[i].Time)
                $.PlotLine("vwap_dw", vwap_dw_arr[i], records[i].Time)
            }
        }
        PreBarTime = records[records.length - 1].Time
    } else {
        if (PreBarTime !== records[records.length - 1].Time) {
            $.PlotLine("vwap", vwap_arr[vwap_arr.length - 2], records[records.length - 2].Time)
            $.PlotLine("vwap_up", vwap_up_arr[vwap_up_arr.length - 2], records[records.length - 2].Time)
            $.PlotLine("vwap_dw", vwap_dw_arr[vwap_dw_arr.length - 2], records[records.length - 2].Time)
            PreBarTime = records[records.length - 1].Time
        }
        $.PlotLine("vwap", vwap_arr[vwap_arr.length - 1], records[records.length - 1].Time)
        $.PlotLine("vwap_up", vwap_up_arr[vwap_up_arr.length - 1], records[records.length - 1].Time)
        $.PlotLine("vwap_dw", vwap_dw_arr[vwap_dw_arr.length - 1], records[records.length - 1].Time)
    }
}

// Place orders for buy and sell on Bybit
// Define Buy function
function buy(Price, Amount, dec) {
    exchange.SetDirection("buy");
    var orderId = null;
    orderId = exchange.Buy(Price, Amount, dec, '@');
    while (!orderId && typeof(orderId) != "undefined" && orderId != 0) {
        Log(orderId);
        Sleep(100);
        orderId = exchange.Buy(Price, Amount, dec, '@');

    }
    return orderId;
}

// Define Sell function
function sell(Price, Amount, dec) {
    exchange.SetDirection("sell");
    var orderId = null;
    orderId = exchange.Sell(Price, Amount, dec, '@');
    while (!orderId && typeof(orderId) != "undefined" && orderId != 0) {
        Log(orderId);
        Sleep(100);
        orderId = exchange.Sell(Price, Amount, dec, '@');

    }
    return orderId;
}

// Account information
function AccountInfo() {
    // Asset information table
    var AccountTab = {
        type: "table",
        title: "Asset Information",
        cols: ["Position", "Direction", "Entry Price", "Current Price", "Liquidation Price", "Leverage", "Position PnL", "Initial Balance", "Total Wallet Balance", "Net Asset Value", "Total PnL"],
        rows: [],
    }
    AccountTab.rows.push([account.Info.result[0].size, CW, account.Info.result[0].entry_price, ticker.Last, account.Info.result[0].liq_price, account.Info.result[0].leverage, account.Info.result[0].unrealised_pnl, start_balance, account.Info.result[0].wallet_balance, jzc, pt])
    LogStatus(_D() + '   STATUS: ' + CW + '\n' +
        'Total available for trade (*leverage): ' + yue + '\n' +
        'index: ' + index + '\n' +
        'VWAP: ' + vwap + '\n' +
        'VWAP_UP: ' + vwap_up + '\n' +
        'VWAP_DW: ' + vwap_dw + '\n' +
        'N: ' + records.length + '\n' +
        'WX: wangxiaoba' + '\n' +
        '`' + JSON.stringify([AccountTab]) + '`' + '\n');
}

// Status check
function Status() {
    if (account.Info.result[0].side === "Buy") {
        status = PD_LONG;
        CW = "LONG";
    } else if (account.Info.result[0].side === "Sell") {
        status = PD_SHORT;
        CW = "SHORT";
    } else {
        status = idle;
        CW = "IDLE";
    }
}

// Trailing take profit initial percentage, U
function TP() {
    var TP_first_long = account.Info.result
``` 

It looks like the `TP` function was cut off. If you need the completion of this function or any other part of the code, please provide more details so I can assist further!