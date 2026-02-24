> Name

Bit-Maker-30-Arbitrage-Smart-Learning-USDT-Standard-Binance-Single-Platform

> Author

AutoBitMaker-ABM

> Strategy Description

Self-learning Grid:

The self-learning grid is based on the traditional grid strategy but has been optimized over time with live trading and backtesting data. It includes dynamic smart add-on positions and profit-taking levels for parameters such as opening logic, entry timing, stop-loss positions, position ratio, and spacing between grids. This approach mitigates the high risks associated with one-sided markets by using minimal leverage to achieve good risk-reward ratios.

The strategy offers a wide range of customizable configuration options. Our team will assign a dedicated person to tailor unique parameter combinations based on your account's risk and return requirements. Additionally, we provide around-the-clock monitoring through both manual and automated market tracking.

We have developed a proprietary index trading collection. Each index includes multiple high-quality single trading pairs with unique weight distributions. The robot runs the self-learning grid strategy on these indexes to avoid risks associated with individual trading pairs experiencing one-sided markets.
Apart from built-in static indexes, we define dynamic indexes based on various selection models for each index, consisting of top-tier coins in different sectors, further reducing risk.

A single account can simultaneously configure and run multiple single-coin trading pairs and index trading pairs. This setup helps to diversify risks while assisting you in making profits across a wide range of market conditions.

Optimization and Risk Management:
Our historical backtesting server operates 24/7, automatically testing all the latest data to calculate optimal parameters.
The strategy cluster includes over 50 auxiliary servers that check account stop-loss conditions every two seconds. This ensures quick exits when risks arise.

Using Alibaba Cloud, Amazon Cloud, and Microsoft Cloud architectures, we separate management and execution nodes, forming a cluster for redundancy and ensuring smooth business operations and fund security with an integrated hybrid cloud model.

Trial Testing:
We offer a 2-week trial run based on your capital size during which commissions are waived.
Do not perform any actions once the bot takes over your account. If manual positions are detected, all bots will immediately exit.

Commission Details:
This depends on your capital amount. We can discuss this after the trial phase. A lower commission rate is available if you sign up using our recommended link.

Contact Information:
WeChat: DuQi_SEC/autobitmaker/Shawn_gb2312/ABM_DD
Email: liuhongyu.louie@autobitmaker.com/autobitmaker_master@autobitmaker.com

Submit a trial application via WeChat Mini Program:
![WeChat Mini Program QR Code](https://www.fmz.cn![IMG](https://www.fmz.com/upload/asset/1281e73989f891ac26aa9.jpg))

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|baseOriginalBalance|1000|Initial base balance|
|showInfo|false|Show information or not|


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
        Log('ERROR ' + account + ',' + err);
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
        Log('ERROR ' + account + ',' + err);
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
        Log('ERROR ' + account + ',' + err);
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
    var totalProfit = 0.0;
    var table = {
        type: 'table',
        title: 'POSITIONS',
        cols: ['Symbol', 'Type', 'AvgPrice', 'Position', 'Profit'],
        rows: []
    };
    if (showInfo) {
        table.rows.push([{
            body: '* 2020-09-07 之前一直人民币100万实盘运行，现策略更新，自动将合约闲置资金转入币安宝，即提高资金安全性，也可以双边获利，当合约所需保证金上涨或下降时，将自动调整两边余额。因当前FMZ无法监控币安宝余额，所以剥离10W人民币继续运行原策略以做展示。',
            colspan: 5
        }]);
    }
    table.rows.push([{
        body: 'This strategy is USDT-denominated, a mean reversion arbitrage strategy on Binance derivatives with low-risk auxiliary grids in parallel (supporting BTC as the base asset on BitMEX)',
        colspan: 5
    }]);
    table.rows.push([{
        body: 'The main arbitrage pairs are BTC/USDT and ETH/USDT, with grid coverage over all trading pairs of Binance perpetual contracts',
        colspan: 5
    }]);
    for (var index in exchangeInnerArray) {
        var position = exchangeInnerArray[index].GetPosition();
        for (var indexInner in position) {
            var profit = Number(position[indexInner].Info.unRealizedProfit);
            totalProfit += profit;
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
    LogStatus('`' + JSON.stringify(table) + '`');
}
```