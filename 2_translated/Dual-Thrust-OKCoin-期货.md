> Name

Dual-Thrust-OKCoin-Futures

> Author

Zero

> Strategy Description

> Basic Principle

- At the end of the day, calculate two values: the difference between the highest price and closing price, and the difference between the closing price and lowest price. Then take the larger value and multiply it by k to get the trigger value.
- On the next morning's opening, record the opening price. If the price exceeds (opening + trigger value), immediately buy; if the price is lower than (opening - trigger value), immediately short sell.
- This system is a reversal system with no separate stop-loss mechanism. That means a reverse signal is also a close-out signal.

> Diagram

![](https://dn-filebox.qbox.me/ab06814528c0ae8c54c6bebaea4438325968fbe5.jpg)

`Dual Thrust strategy includes complete chart display, dynamic updating of charts, template references, etc., and can be used as a learning template.`

For more detailed strategy information: [http://xueqiu.com/5256769224/32429363](http://xueqiu.com/5256769224/32429363)

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|ContractTypeIdx|0|Contract Type: Current Week|Next Week|Quarter|
|MarginLevelIdx|0|Margin Level: 10|20|
|NPeriod|4|Calculation Period|
|Ks|0.5|Upper Track Coefficient|
|Kx|0.5|Lower Track Coefficient|
|AmountOP|true|Contract Number for Opening Position|
|Interval|2000|Retry Interval (milliseconds)|
|LoopInterval|3|Polling Interval (seconds)|
|PeriodShow|500|Maximum K-line Columns to Display on Chart|


> Source Code (JavaScript)

```javascript
var ChartCfg = {
    __isStock: true,
    title: {
        text: 'Dual Thrust Upper and Lower Track'
    },
    yAxis: {
        plotLines: [{
            value: 0,
            color: 'red',
            width: 2,
            label: {
                text: 'Upper Track',
                align: 'center'
            },
        }, {
            value: 0,
            color: 'green',
            width: 2,
            label: {
                text: 'Lower Track',
                align: 'center'
            },
        }]
    },
    series: [{
        type: 'candlestick',
        name: 'Current Period',
        id: 'primary',
        data: []
    }, {
        type: 'flags',
        onSeries: 'primary',
        data: [],
    }]
};

var STATE_IDLE = 0;
var STATE_LONG = 1;
var STATE_SHORT = 2;
var State = STATE_IDLE;

var LastBarTime = 0;
var UpTrack = 0;
var BottomTrack = 0;
var chart = null;
var InitAccount = null;
var LastAccount = null;
var Counter = {
    w: 0,
    l: 0
};

function _N(v) {
    return Decimal(v).toSD(4, 1).toNumber();
}

function GetPosition(posType) {
    var positions = exchange.GetPosition();
    for (var i = 0; i < positions.length; i++) {
        if (positions[i].Type === posType) {
            return [positions[i].Price, positions[i].Amount];
        }
    }
    return [0, 0];
}

function CancelPendingOrders() {
    while (true) {
        var orders = exchange.GetOrders();
        for (var i = 0; i < orders.length; i++) {
            exchange.CancelOrder(orders[i].Id);
            Sleep(Interval);
        }
        if (orders.length === 0) {
            break;
        }
    }
}

function Trade(currentState, nextState) {
    var pfn = nextState === STATE_LONG ? exchange.Buy : exchange.Sell;
    if (currentState !== STATE_IDLE) {
        exchange.SetDirection(currentState === STATE_LONG ? "closebuy" : "closesell");
        while (true) {
            var amount = GetPosition(currentState === STATE_LONG ? PD_LONG : PD_SHORT)[1];
            if (amount === 0) {
                break;
            }
            // pfn(amount);
            pfn(nextState === STATE_LONG ? _C(exchange.GetTicker).Sell * 1.001 : _C(exchange.GetTicker).Buy * 0.999, amount);
            Sleep(Interval);
            CancelPendingOrders();
        };
        var account = exchange.GetAccount();

        if (account.Stocks > LastAccount.Stocks) {
            Counter.w++;
        } else {
            Counter.l++;
        }

        LogProfit(_N(account.Stocks - InitAccount.Stocks), "Return Rate:", _N((account.Stocks - InitAccount.Stocks) * 100 / InitAccount.Stocks) + '%');
        LastAccount = account;
    }
    exchange.SetDirection(nextState === STATE_LONG ? "buy" : "sell");
    while (true) {
        var pos = GetPosition(nextState === STATE_LONG ? PD_LONG : PD_SHORT);
        if (pos[1] >= AmountOP) {
            Log("Average Price", pos[0], "Quantity:", pos[1]);
            break;
        }
        // pfn(AmountOP - pos[1]);
        pfn(nextState === STATE_LONG ? _C(exchange.GetTicker).Sell * 1.001 : _C(exchange.GetTicker).Buy * 0.999, AmountOP - pos[1]);
        Sleep(Interval);
        CancelPendingOrders();
    }
}

function onTick(exchange) {
    var records = exchange.GetRecords();
    if (!records || records.length <= NPeriod) {
        return;
    }
    var Bar = records[records.length - 1];
    if (LastBarTime !== Bar.Time) {
        var HH = TA.Highest(records, NPeriod, 'High');
        var HC = TA.Highest(records, NPeriod, 'Close');
        var LL = TA.Lowest(records, NPeriod, 'Low');
        var LC = TA.Lowest(records, NPeriod, 'Close');

        var Range = Math.max(HH - LC, HC - LL);

        UpTrack = _N(Bar.Open + (Ks * Range));
        DownTrack = _N(Bar.Open - (Kx * Range));
        if (LastBarTime > 0) {
            var PreBar = records[records.length - 2];
            chart.add(0, [PreBar.Time, PreBar.Open, PreBar.High, PreBar.Low, PreBar.Close], -1);
        } else {
            for (var i = Math.min(records.length, NPeriod * 3); i > 1; i--) {
                var b = records[records.length - i];
                chart.add(0, [b.Time, b.Open, b.High, b.Low, b.Close]);
            }
        }
        chart.add(0, [Bar.Time, Bar.Open, Bar.High, Bar.Low, Bar.Close]);
        ChartCfg.yAxis.plotLines[0].value = UpTrack;
        ChartCfg.yAxis.plotLines[1].value = DownTrack;
        ChartCfg.subtitle = {
            text: 'Upper Track: ' + UpTrack + '  Lower Track: ' + DownTrack
        };
        chart.update(ChartCfg);
        chart.reset(PeriodShow);

        LastBarTime = Bar.Time;
    } else {
        chart.add(0, [Bar.Time, Bar.Open, Bar.High, Bar.Low, Bar.Close], -1);
    }

    LogStatus("Price:", Bar.Close, "Up:", UpTrack, "Down:", DownTrack, "Wins: ", Counter.w, "Losses:", Counter.l, "Date:", new Date());
    var msg;
    if (State === STATE_IDLE || State === STATE_SHORT) {
        if (Bar.Close >= UpTrack) {
            msg = 'Long Triggered at: ' + Bar.Close + ' Upper Track:' + UpTrack;
            Log(msg);
            Trade(State, STATE_LONG);
            State = STATE_LONG;
            chart.add(1, {x: Bar.Time, color: 'red', shape: 'flag', title: 'Long', text: msg});
        }
    }

    if (State === STATE_IDLE || State === STATE_LONG) {
        if (Bar.Close 