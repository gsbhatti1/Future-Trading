> Name

Bit-Maker-Real-Time Monitoring of Total USDT Contract Balance for Spot Trading

> Author

AutoBitMaker-ABM

> Strategy Description

**AutoBitMaker** is currently officially releasing a risk-free arbitrage strategy.
The principle behind the strategy involves hedging between spot and contract trading, which can also be manually completed. However, compared to manual operations, the BOT will capture profit opportunities across all trading pairs in the market, with transactions happening hundreds of times daily. This further frees up your hands and reduces market risks.

We are **AutoBitMaker**, commonly known as **ABM Capital**. Please carefully verify our team name, WeChat ID, to distinguish authenticity.
Currently, we only communicate with domestic clients via WeChat and email; other methods such as QQ will not be used.

**ABM Team** currently provides three types of strategies:
* Contract Trading
* Spot Trading
* Arbitrage Trading

The current code is solely for account monitoring. The source code has been publicly disclosed, allowing you to check or use it at your discretion.
It monitors the USDT value from spot trading and USDT contract.

Currently, our team's strategy server cluster has reached 80 machines, with an additional 50 supporting servers. At an average of two checks per second for account stop-loss conditions, we can quickly exit in times of risk.

Using Alibaba Cloud, Amazon Cloud, and Microsoft Cloud architectures with a heterogeneous hybrid cloud model, management nodes are separated from execution nodes, forming clusters to ensure redundancy, securely and effectively achieving smooth business operations and financial security.

Regarding the trial period:
Based on your capital scale, we provide a 2-week test run. During this phase, no commission will be deducted.
Please do not perform any actions after the BOT takes over your account; upon detecting any manual positions, all Bots will immediately exit.

Regarding commissions:
This depends on your capital volume. We can discuss details after the trial period. If you open an account using our recommended link, we will charge a low commission.

Contact Information:
1. Available for face-to-face meetings across China
2. WeChat: DuQi_SEC/autobitmaker/autobitmaker_001/Shawn_gb2312/ABM_DD 
3. Email: liuhongyu.louie@autobitmaker.com/autobitmaker_master@autobitmaker.com

* Special Note (WeChat ID autobitmaker001 is not us! We also do not call ourselves makebit! The correct WeChat ID is autobitmaker_001)

Submit your trial application via the WeChat Mini Program:
![WeChat Mini Program QR Code](https://www.fmz.cn![IMG](https://www.fmz.com/upload/asset/1281e73989f891ac26aa9.jpg))

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|baseOriginalBalance|10000|baseOriginalBalance|


> Source (javascript)

``` javascript
//exchanges[0] is contract
//exchanges[1] is spot

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

function updateAccountDetailChart(ObjChart, totalBalance) {
    var nowTime = new Date().getTime();
    var account = exchanges[0].GetAccount();
    try {
        if (account !== null && account.Info !== null && account.Info.totalMarginBalance > 0) {
            ObjChart.add([0, [nowTime, Number(totalBalance)]]);
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

function getSpotBalanceInUSDT() {
    var ticker = JSON.parse(HttpQuery('https://api.binance.com/api/v1/ticker/24hr'));
    var currentBalance = 0;
    var account = exchanges[1].GetAccount();
    var priceMap = {};
    try {
        if (ticker !== null) {
            for (var index in ticker) {
                priceMap[ticker[index].symbol] = ticker[index].lastPrice;
            }
        }
        if (account !== null && account.Info !== null) {
            for (var index in account.Info.balances) {
                var obj = account.Info.balances[index];
                if (obj.asset !== 'USDT' && priceMap[obj.asset + 'USDT']) {
                    currentBalance += Number(Number(priceMap[obj.asset + 'USDT']) * Number((Number(obj.free) + Number(obj.locked))));
                }
                if (obj.asset === 'USDT') {
                    currentBalance += Number((Number(obj.free) + Number(obj.locked)));
                }
            }
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
    table.rows.push([{
        body: 'This strategy is USDT-centric, based on mean reversion arbitrage between Binance spot and contract trading.',
        colspan: 5
    }]);
    table.rows.push([{
        body: 'Arbitrage covers all trading pairs of Binance perpetual contracts.',
        colspan: 5
    }]);
    var position = exchangeInnerArray[0].GetPosition()
    for (var indexInner in position) {
        var profit = Number(position[indexInner].Info.unRealizedProfit);
        totalProfit = totalProfit + profit
        table.rows.push([position[indexInner].Info.symbol, (position[indexInner].Type == 1 ? 'SHORT #da1b1bab' : 'LONG #1eda1bab'), position[indexInner].Price, position[indexInner].Amount, profit.toFixed(5)]);
    }
    Sleep(168);
    table.rows.push([{
        body: 'TOTAL PROFIT OF CURRENT POSITION',
        colspan: 4
    }]);
```