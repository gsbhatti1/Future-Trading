> Name

Bit-Maker-30-Arbitrage-Smart-Learning-USDT-Primary-Binance-Single-Platform

> Author

AutoBitMaker-ABM

> Strategy Description

Self-learning Grid:

The self-learning grid is based on the traditional grid strategy but has been optimized over time through live trading and backtesting data for opening logic, additional position timing, take-profit levels, position ratios, grid spacing, and dozens of other parameter configurations. It achieves intelligent dynamic addition models and take-profit positions, mitigating the high risks associated with single-sided markets by utilizing minimal leverage to achieve excellent risk-adjusted returns.

The strategy has an extremely rich set of configurable parameters, which our team will tailor for your account based on your risk tolerance and return requirements, including around-the-clock manual and automated market monitoring.

We have a proprietary self-developed index trading collection, where each index trading bundle includes multiple high-quality single trading pairs with unique weight ratios. The robot runs the self-learning grid strategy on these index bundles to avoid risks associated with single trading pairs in one-sided markets.
In addition to built-in static indices, we define dynamic indices for our index pools based on various selection models, creating diversified indexes that further reduce risk.

A single account can simultaneously configure and run multiple single-coin trading pairs and index trading pairs, both to diversify risk and to aid you in profitable trades across various complex market scenarios.

Regarding optimization + risk management:
Historical backtesting servers operate 24/7, automatically testing all new data and real-time calculation of optimal parameters.
Our strategy cluster consists of over 50 auxiliary servers, checking the account's stop-loss conditions every two seconds to quickly exit in case of a risk event.

Using Alibaba Cloud, Amazon Web Services (AWS), and Microsoft Azure architectures with separate management and execution nodes, multiple nodes form clusters for redundancy and secure, efficient business operations and fund safety.

Regarding trial use:
Based on your capital scale, we provide about 2 weeks of free testing. During the test period, no commissions will be charged.
Do not perform any actions once the bot takes over your account; all bots will exit if any manual positions are detected.

Regarding commissions:
This depends on your capital size. We can discuss this after the trial phase. If you sign up using our recommended link, we will charge very low commissions.

Contact Information:
WeChat: DuQi_SEC/autobitmaker/Shawn_gb2312/ABM_DD
Email: liuhongyu.louie@autobitmaker.com/autobitmaker_master@autobitmaker.com

Submit your trial application via WeChat Mini Program:
![WeChat Mini Program QR Code](https://www.fmz.cn![](https://www.fmz.com/upload/asset/1281e73989f891ac26aa9.jpg))

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|baseOriginalBalance|1000|Base original balance|
|showInfo|false|Show information|

> Source (javascript)

``` javascript
var chart = {
    __isStock: false,
    extension: {
        layout: 'single',
        col: 8,
        height: '300px'
    },
    tooltip: {
        xDateFormat: '%Y-%m-%d %H:%M:%S, %A'
    },
    title: {
        text: 'Account_Balance_Detail'
    },
    xAxis: {
        type: 'datetime'
    },
    yAxis: {
        title: {
            text: 'USDT'
        },
        opposite: false
    },
    series: []
};

function initChart() {
    chart.series.push({
        name: "Account_" + (Number(0)) + "_Detail",
        id: "Account_" + (Number(0)) + "_Detail",
        data: []
    });
}

function getChartPosition(avaliableMargin) {
    return {
        __isStock: false,
        extension: {
            layout: 'single',
            col: 4,
            height: '300px'
        },
        title: {
            text: 'Margin Ratio (%)'
        },
        series: [{
            type: 'pie',
            name: 'one',
            data: [{
                name: 'Available Margin (%)',
                y: avaliableMargin,
                color: '#dff0d8',
                sliced: true,
                selected: true
            }, {
                name: 'Used Margin (%)',
                y: 100 - avaliableMargin,
                color: 'rgb(217, 237, 247)',
                sliced: true,
                selected: true
            }]
        }]
    };
}

function updateAccountDetailChart(ObjChart) {
    var nowTime = new Date().getTime();
    var account = exchanges[0].GetAccount();
    try {
        if (account !== null && account.Info !== null && account.Info.totalMarginBalance > 0) {
            ObjChart.add([0, [nowTime, Number(account.Info.totalMarginBalance)]]);
        }
    } catch (err) {
        Log('ERROR ' + account + ',' + err)
    }
}

function getBalance() {
    var currentBalance = 0;
    var account = exchanges[0].GetAccount();
    try {
        if (account !== null && account.Info !== null && account.Info.totalWalletBalance > 0) {
            currentBalance += Number(account.Info.totalWalletBalance);
        }
    } catch (err) {
        Log('ERROR ' + account + ',' + err)
    }
    Sleep(666);
    return Number(currentBalance).toFixed(6);
}

function getMarginBalance() {
    var currentBalance = 0;
    var account = exchanges[0].GetAccount();
    try {
        if (account !== null && account.Info !== null && account.Info.totalMarginBalance > 0) {
            currentBalance += Number(account.Info.totalMarginBalance);
        }
    } catch (err) {
        Log('ERROR ' + account + ',' + err)
    }
    Sleep(666);
    return Number(currentBalance).toFixed(6);
}

function printProfitInfo(currentBalance) {
    var profit = Number((currentBalance) - baseOriginalBalance).toFixed(5);
    var profitRate = Number((((currentBalance) - baseOriginalBalance) / baseOriginalBalance) * 100).toFixed(4);
    LogProfit(Number(profitRate), '&');
    Log('The current balance is ' + currentBalance + ', the profit is ' + profit + ', the profit rate is ' + profitRate + '%');
}

function printPositionInfo(exchangeInnerArray, totalProfitUSDT, totalProfitRate) {
    var totalProfit = 0.0
    var table = {
        type: 'table',
        title: 'POSITIONS',
        cols: ['Symbol', 'Type', 'AvgPrice', 'Position', 'Profit'],
        rows: []
    }
    if (showInfo) {
        table.rows.push([{
            body: '* 2020-09-07 之前一直人民币100万实盘运行，现策略更新，自动将合约闲置资金转入币安宝，即提高资金安全性，也可以双边获利，当合约所需保证金上涨或下降时，将自动调整两边余额。因当前FMZ无法监控币安宝余额，所以剥离10W人民币继续运行原策略以做展示。',
            colspan: 5
        }]);
    }
    table.rows.push([{
        body: 'This strategy is USDT-based, a mean reversion arbitrage strategy on Binance futures contracts, with low-risk parallel grid operations (BitMEX supports BTC-based grids)',
        colspan: 5
    }]);
    table.rows.push([{
        body: 'Main arbitrage coins are BTC/USDT and ETH/USDT, with the grid covering all trading pairs of Binance perpetual contracts',
        colspan: 5
    }]);
    for (var index in exchangeInnerArray) {
        var position = exchangeInnerArray[index].GetPosition()
        for (var indexInner in position) {
            var profit = Number(position[indexInner].Info.unRealizedProfit);
            totalProfit = totalProfit + profit
            table.rows.push([position[indexInner].Info.symbol, (position[indexInner].Type == 1 ? 'SHORT #da1b1bab' : 'LONG #1eda1bab'), position[indexInner].Price, position[indexInner].Amount, profit.toFixed(5)]);
        }
        Sleep(168);
    }
    table.rows.push([{
        body: 'TOTAL PROFIT OF CURRENT POSITION',
        colspan: 4
    }, totalProfit.toFixed(6) + ' USDT']);
    table.rows.push([{
        body: 'TOTAL PROFIT',
        colspan: 4
    }, totalProfitUSDT + ' USDT']);
    table.rows.push([{
        body: 'TOTAL PROFIT RATE',
        colspan: 4
    }, totalProfitRate + ' %']);
    LogStatus('`' + JSON.stringify(table)