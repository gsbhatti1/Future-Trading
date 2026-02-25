> Name

Bybit-Arbitrage-Pin-Strategy-VWAP-BTC

> Author

Bean Beans

> Strategy Description

Here starts the sharing of the original version of the Pin strategy for Bybit!
What's the main reason?///
 ![IMG](https://www.fmz.com/upload/asset/95a9985fc126e73d27e9.png) 

That's quite frustrating, isn't it...
You promised to make this open-source and now you're upset because someone sold it without permission.
I hope the seniors won't do this anymore.
Here, I'm directly opening source,
This strategy itself is not something amazing...

Feel free to play around with it!
Don't buy my garbage code for money.
Just use it! Let's go!

By the way, a little advertisement:
For more ways to lose money, please follow the WeChat public account "Bean Beans' Quantitative Log."
WX: wangxiaoba

(●'◡'●)

> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|start_balance|false|Initial balance|
|long_qty|true|Single long USD quantity|
|short_qty|true|Single short USD quantity|
|maxPosition|500000|Maximum order size|
|take_profit|45|Initial take profit (USD)|
|trailing_profit|true|Trailing take profit in USD|
|stop_loss|9|Stop loss percentage|
|long_vwap_offset|2.5|VWAP upper boundary percentage|
|short_vwap_offset|2.5|VWAP lower boundary percentage|
|GG|3|Maintenance margin ratio (2x-7x is recommended, the higher the leverage, the greater the risk)|
|stop_step|3600|Stop loss step time (s)|


> Source (javascript)

``` javascript
// Check user authorization (UID list + getAccount UID validation)
function user_auth() {
    user_list = [775536, 783571, 789086, 819490, 1265698, 1294567, 1299150]
    user_id = account.Info.result[0].user_id
    //Log(user_id)
    if (user_list.indexOf(user_id) == -1) {
        throw new Error('User authentication error. Please contact WeChat: wangxiaoba')
    }
}

// Calculate and get VWAP and upper/lower boundaries Bybit
function VWAP() {
    // Define the candlestick, calculate VWAP
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

// Draw lines
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

// Define Buy order
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

// Define Sell order
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
        cols: ["Position Size", "Direction", "Average Entry Price", "Current Price", "Liquidation Price", "Maintenance Margin Ratio", "P/L of Position", "Initial Balance Value", "Total Asset Value", "Net Asset Value", "Total P/L"],
        rows: [],
    }
    AccountTab.rows.push([account.Info.result[0].size, CW, account.Info.result[0].entry_price, ticker.Last, account.Info.result[0].liq_price, account.Info.result[0].leverage, account.Info.result[0].unrealised_pnl, start_balance, account.Info.result[0].wallet_balance, jzc, pt])
    LogStatus(_D() + '   STATUS: ' + CW + '\n' +
        'Total orderable volume (* leverage): ' + yue + '\n' +
        'index: ' + index + '\n' +
        'VWAP: ' + vwap + '\n' +
        'VWAP_UP: ' + vwap_up + '\n' +
        'VWAP_DW: ' + vwap_dw + '\n' +
        'N: ' + records.length + '\n' +
        'WX: wangxiaoba' + '\n' +
        '`' + JSON.stringify([AccountTab]) + '`' + '\n');
}

// Status judgment
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

// Trailing take profit initial percentage, tracking U
function TP() {
    var TP_first_long = account.Info.result
``` 

It looks like the code snippet was cut off. The `TP` function is incomplete and should be continued based on the original context of the strategy implementation. If you need further assistance with completing this or any other part, feel free to ask!